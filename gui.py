import sys
import os
from datetime import datetime

import paho.mqtt.client as mqtt

import numpy as np
from scipy.ndimage import gaussian_filter
from scipy.signal import find_peaks, peak_widths, peak_prominences
import matplotlib.pyplot as plt
import cv2

from PySide6 import QtWidgets, QtGui, QtCore
from ui import Ui_MainWindow
import pyqtgraph as pg

class Plantar(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        # Logo
        self.logo.setPixmap(QtGui.QPixmap(u"Kmitl.jpg"))
        
        f = open("data.txt",'a+')
        f.write("\n"+str(datetime.now())+"\n")
        f.close()

        # Save's signaling
        self.browse.clicked.connect(self.browse_file)
        self.set_save_state.clicked.connect(self.set_save_state_fn)
        self.save_state = False
        self.pause_save.clicked.connect(self.pause_save_fn)
        self.pause_state = False

        # Plot's signaling & setting
        self.set_packet_size.clicked.connect(self.esp_set_packet_size)
        self.sampling_rate.currentTextChanged.connect(self.esp_set_sampling_rate)
        self.set_window_size.clicked.connect(self.set_window_size_fn)
        self.plot_size = 1000
        self.set_plot_state.clicked.connect(self.set_plot_state_fn)
        self.plot_state = False

        self.raw.setRange(QtCore.QRectF(0, 0, self.plot_size, 3000))
        self.raw.enableAutoRange()

        self.numbers_of_sensor = 18
        self.set_of_sensor = 6
        
                # preparing fsr position
        self.feet_size = [655, 1475] # [x, y]
        self.fsr_position = {
            1: [[296, 1296, 0], [296, 1167, 6], [279, 946, 12]],
            2: [[401, 1291, 1], [417, 1170, 7], [393, 1042, 13]],
            3: [[256, 738, 2], [224, 539, 8], [344, 465, 14]],
            4: [[425, 886, 3], [421, 733, 9], [455, 587, 15]],
            5: [[193, 373, 4], [163, 264, 10], [147, 145, 16]],
            6: [[481, 416, 5], [507, 272, 11], [340, 317, 17]],
        }
        self.factor = 8
        self.sensor_radius = 45
        self.outline_img = cv2.resize(cv2.cvtColor(cv2.imread('foot_outline.jpg'), cv2.COLOR_BGR2BGRA), (int(self.feet_size[0]/self.factor), int(self.feet_size[1]/self.factor)))
        self.sensor = np.zeros((int(self.feet_size[1]/self.factor), int(self.feet_size[0]/self.factor))) #(y, x)
        
        # self.rawLines = [pg.PlotCurveItem(pen=pg.mkPen(color=pg.intColor(i, hues=self.numbers_of_sensor), width=20), skipFiniteCheck=True) for i in range(self.numbers_of_sensor)]
        # for line in self.rawLines:
        #     self.raw.addItem(line)

        self.cop_his = []
        self.raw_data = [[0] for _ in range(self.numbers_of_sensor)]

        self.zones = {
            "forefoot":[4, 5, 8, 10, 11, 14, 15, 16, 17],
            "mid":[2, 3, 9, 12, 13],
            "heel":[0, 1, 6, 7]
        }

        plot_line_width = 3
        
        # Tab visualize
        self.zone_lines = {
            "forefoot": pg.PlotCurveItem(pen=pg.mkPen(color=pg.intColor(0), width=plot_line_width), skipFiniteCheck=True),
            "mid": pg.PlotCurveItem(pen=pg.mkPen(color=pg.intColor(4), width=plot_line_width), skipFiniteCheck=True),
            "heel": pg.PlotCurveItem(pen=pg.mkPen(color=pg.intColor(8), width=plot_line_width), skipFiniteCheck=True)
        }

        self.zone_data = {
            "forefoot":[0],
            "mid":[0],
            "heel":[0]
        }
        for line in self.zone_lines.values():
            self.raw.addItem(line)
            
        # for display heatmap only
        self.heatmap_img = pg.ImageItem()
        self.heatmap.addItem(self.heatmap_img)
        cm = pg.colormap.get('CET-L20')
        bar = pg.ColorBarItem(values = (0, 3_000), colorMap = cm)
        bar.setImageItem(self.heatmap_img, insert_in=self.heatmap.getPlotItem())

        
        # resize heatmap, display foot outline, display sensor outline and display sensor label
        self.hm_labels = {}

        for ADC_channel in self.fsr_position.keys():
            for idx in range(3):
                self.fsr_position[ADC_channel][idx][0] //= self.factor
                self.fsr_position[ADC_channel][idx][1] //= self.factor
                self.outline_img_circle = cv2.circle(self.outline_img, (self.fsr_position[ADC_channel][idx][0], self.fsr_position[ADC_channel][idx][1]), int(self.sensor_radius/self.factor), (255, 255, 255), 5)
                
                label = pg.TextItem(text=str(self.fsr_position[ADC_channel][idx][2]), anchor=(0, 1), color=(200, 200, 200))
                label.setPos(self.fsr_position[ADC_channel][idx][0], self.feet_size[1]-self.fsr_position[ADC_channel][idx][1])
                self.hm_labels[self.fsr_position[ADC_channel][idx][2]] = label
                self.heatmap.addItem(label)

        self.heatmap_outline = pg.ImageItem(image=np.rot90(self.outline_img_circle, 3))
        self.heatmap_outline.setCompositionMode(QtGui.QPainter.CompositionMode_Overlay)
        self.heatmap.addItem(self.heatmap_outline)

        # for display cop
        self.heatmap_cop = pg.ImageItem()
        self.heatmap_cop.setCompositionMode(QtGui.QPainter.CompositionMode_Exclusion)
        self.heatmap.addItem(self.heatmap_cop)

        self.heatmap.setRange(QtCore.QRectF(0, 0, int(self.feet_size[0]/self.factor), int(self.feet_size[1]/self.factor)))
        self.heatmap.setAspectLocked()
        self.heatmap.enableAutoRange()
        self.heatmap.showAxes(False)
        
        
        # Tab Analyze
        self.raw_2.setRange(QtCore.QRectF(0, 0, self.plot_size, 3000))
        self.raw_2.enableAutoRange()
        self.raw_2.setMouseEnabled(x=True, y=False)
        style = {"color": "#fff","font-size":"16px"}
        self.raw_2.setLabel("left", "Force", units="N", **style)
        self.raw_2.setLabel("bottom", "Time", units="s", **style)
        
        self.region = pg.LinearRegionItem()
        self.region.sigRegionChangeFinished.connect(self.analyze_update)
        self.raw_2.addItem(self.region)
        
        # signaling
        self.load_btn.clicked.connect(self.load_saved_data)
        
        self.zone_2_lines = {
            "forefoot": pg.PlotCurveItem(pen=pg.mkPen(color=pg.intColor(0), width=plot_line_width), skipFiniteCheck=True),
            "mid": pg.PlotCurveItem(pen=pg.mkPen(color=pg.intColor(4), width=plot_line_width), skipFiniteCheck=True),
            "heel": pg.PlotCurveItem(pen=pg.mkPen(color=pg.intColor(8), width=plot_line_width), skipFiniteCheck=True)
        }

        self.zone_2_data = {
            "forefoot":[0],
            "mid":[0],
            "heel":[0]
        }
        for line in self.zone_2_lines.values():
            self.raw_2.addItem(line)
        self.data_for_analyze = []
        self.loaded_data = [[0] for _ in range(self.numbers_of_sensor)]

        # for display heatmap only
        # self.heatmap_2_img = pg.ImageItem()
        # self.heatmap_2.addItem(self.heatmap_2_img)
        cm_2 = pg.colormap.get('CET-L20')
        # bar_2 = pg.ColorBarItem(values = (0, 100), colorMap = cm_2)
        # bar_2.setImageItem(self.heatmap_2_img, insert_in=self.heatmap_2.getPlotItem())
        self.heatmap_2.setColorMap(cm_2)

        
        # resize heatmap, display foot outline, display sensor outline and display sensor label
        # self.heatmap_2_outline = pg.ImageItem(image=np.rot90(self.outline_img, 3))
        # self.heatmap_2_outline.setCompositionMode(QtGui.QPainter.CompositionMode_Overlay)
        # self.heatmap.addItem(self.heatmap_2_outline)

        # # for display cop
        # self.heatmap_cop = pg.ImageItem()
        # self.heatmap_cop.setCompositionMode(QtGui.QPainter.CompositionMode_Exclusion)
        # self.heatmap.addItem(self.heatmap_cop)

        # self.heatmap_2.setRange(QtCore.QRectF(0, 0, int(self.feet_size[0]/self.factor), int(self.feet_size[1]/self.factor)))
        # self.heatmap_2.setAspectLocked()
        # self.heatmap_2.enableAutoRange()
        # self.heatmap_2.showAxes(False)
        

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)

        # Advance
        # self.timer2 = QtCore.QTimer()
        # self.timer2.timeout.connect(self.check_esp_status)
        # self.timer2.start(10000)

    def open_connection(self):
        # Connection
        self.broker_address = "127.0.0.1" 
        self.client  = mqtt.Client("P1") 
        self.client.on_message = self.on_message
        self.client.connect(self.broker_address)
        self.client.subscribe("esp32/data")
        self.client.subscribe("esp32/status")
        self.client.loop_start()
        self.esp_set_transmission_state(1)

    def close_connection(self):
        self.esp_set_transmission_state(0)
        self.client.loop_stop()
        self.client.disconnect()

    def esp_set_packet_size(self):
        self.client.publish("esp32/Nsampling", self.packet_size.value())
        
    def esp_set_sampling_rate(self):
        self.client.publish("esp32/sampling_rate", self.sampling_rate.currentText())

    def esp_set_transmission_state(self, state):
        self.client.publish("esp32/transmission_state", state)

    def on_message(self, client, userdata, message):
        if message.topic == "esp32/data":
            # no thread required here, the delay is in accaptable range.
            self.data(message)
            
    def data(self, message):
        pl = str(message.payload.decode("utf-8"))
        samples = pl.split('\n')
        
        f = open("data.txt",'a+')
        f.write(pl)
        f.close()

        for sample in samples:
            if len(sample) != 0:
                temp = sample.split(',')
                for key in self.zones.keys():
                    self.zone_data[key].append(0)
                for channel in range(self.numbers_of_sensor):
                    calibrated_value = self.ADC_value_mapping(int(temp[channel+1]))
                    
                    self.raw_data[channel].append(calibrated_value)
                    for key, zone in self.zones.items():
                        if channel in zone:
                            self.zone_data[key][-1] += calibrated_value

        if len(self.raw_data[0]) > self.plot_size:
            for channel in range(self.numbers_of_sensor):
                self.raw_data[channel] = self.raw_data[channel][-self.plot_size:]
            for key in self.zones.keys():
                self.zone_data[key] = self.zone_data[key][-self.plot_size:]
                    
    def update(self):
        for key, zone_line in self.zone_lines.items():
            zone_line.setData(np.array(self.zone_data[key]))
        self.hm()
        
    def ADC_value_mapping(self, x: int):
        return ((0.024619*np.exp(0.00259135*x)) + (0.0014355*x))*9.81
        
    def hm(self):
        circle = self.sensor.copy()
        c_x = 0
        c_y = 0
        value_sum = 0

        for ADC_channel in self.fsr_position.keys():
            for idx in range(3):
                circle = cv2.circle(circle, (self.fsr_position[ADC_channel][idx][0], self.fsr_position[ADC_channel][idx][1]), int(self.sensor_radius/self.factor), self.raw_data[self.fsr_position[ADC_channel][idx][2]][-1], -1)
                self.hm_labels[self.fsr_position[ADC_channel][idx][2]].setText(str(self.raw_data[self.fsr_position[ADC_channel][idx][2]][-1]))
                c_x += self.raw_data[self.fsr_position[ADC_channel][idx][2]][-1]*self.fsr_position[ADC_channel][idx][0]
                c_y += self.raw_data[self.fsr_position[ADC_channel][idx][2]][-1]*self.fsr_position[ADC_channel][idx][1]
                value_sum += self.raw_data[self.fsr_position[ADC_channel][idx][2]][-1]

        c_x /= value_sum+1
        c_y /= value_sum+1
        
        circle = gaussian_filter(circle, sigma=6, mode='constant')
        self.cop_his.append((int(c_x), int(c_y)))

        if len(self.cop_his) >= 15:
            self.cop_his.pop(0)
        # draw Center of Pressure
        cop = self.sensor.copy()
        for item in self.cop_his:
            cop = cv2.circle(cop, item, int(self.sensor_radius/(self.factor*3)), (255, 255, 255), -1)
        
        self.heatmap_img.setImage(np.rot90(circle, 3))
        self.heatmap_cop.setImage(np.rot90(cop, 3))
        
    def set_window_size_fn(self):
        self.plot_size = int(self.window_size.value())

    def set_plot_state_fn(self):
        self.plot_state = not self.plot_state
        if self.plot_state:
            self.set_plot_state.setText("Stop plotting")
            self.timer.start(0)
        else:
            self.set_plot_state.setText("Start plotting")
            self.timer.stop()

    def analyze_update(self):
        start, stop = self.region.getRegion()
        start *= int(self.sampling_rate.currentText())
        stop *= int(self.sampling_rate.currentText())
        whole_region = int(stop - start)
        x = np.array(self.data_for_analyze[int(start):int(stop)])
        
        peaks, _ = find_peaks(x, prominence=60, width=60)

        results_full = peak_widths(x, peaks, rel_height=1)
        stance_times, widths_height, left_pos, right_pos = results_full
        len_w = len(stance_times)
        
        stance_time = np.mean(stance_times)/int(self.sampling_rate.currentText())
        swing_time = (whole_region - np.sum(stance_times)) / (len_w*int(self.sampling_rate.currentText()))
        stride_time = stance_time + swing_time
        step_time = stride_time/2
        cadence = int(60/step_time)
        
        self.stance_t.setText("{:.2f}".format(stance_time))
        self.swing_t.setText("{:.2f}".format(swing_time))
        self.stride_t.setText("{:.2f}".format(stride_time))
        self.step_t.setText("{:.2f}".format(step_time))
        self.cadence.setText("{:.2f}".format(cadence))
        self.stance_p.setText("{:.2f}".format(stance_time*100/stride_time))
        self.swing_p.setText("{:.2f}".format(swing_time*100/stride_time))
        
        images = []
        for i, j in zip(left_pos, right_pos):
            data = self.loaded_data[:, int(i):int(j)]
            s = np.sum(data, 1)
            
            circle = self.sensor.copy()
            # c_x = 0
            # c_y = 0
            # value_sum = 0

            for ADC_channel in self.fsr_position.keys():
                for idx in range(3):
                    circle = cv2.circle(circle, (self.fsr_position[ADC_channel][idx][0], self.fsr_position[ADC_channel][idx][1]), int(self.sensor_radius/self.factor), int(s[self.fsr_position[ADC_channel][idx][2]]), -1)
                    # self.hm_labels[self.fsr_position[ADC_channel][idx][2]].setText(str(self.raw_data[self.fsr_position[ADC_channel][idx][2]][-1]))
                    # c_x += self.raw_data[self.fsr_position[ADC_channel][idx][2]][-1]*self.fsr_position[ADC_channel][idx][0]
                    # c_y += self.raw_data[self.fsr_position[ADC_channel][idx][2]][-1]*self.fsr_position[ADC_channel][idx][1]
                    # value_sum += self.raw_data[self.fsr_position[ADC_channel][idx][2]][-1]

            # c_x /= value_sum+1
            # c_y /= value_sum+1
            
            circle = gaussian_filter(circle, sigma=6, mode="constant")
            # self.cop_his.append((int(c_x), int(c_y)))

            # if len(self.cop_his) >= 15:
            #     self.cop_his.pop(0)
            # # draw Center of Pressure
            # cop = self.sensor.copy()
            # for item in self.cop_his:
            #     cop = cv2.circle(cop, item, int(self.sensor_radius/(self.factor*3)), (255, 255, 255), -1)
            images.append(np.fliplr(np.rot90(circle, 3)))
            
        self.heatmap_2.setImage(np.array(images))
        # self.heatmap_cop.setImage(np.rot90(cop, 3))
        
        
    def load_saved_data(self):
        fnames = str(QtWidgets.QFileDialog.getOpenFileName(caption="Open saved data", filter="Data (*.txt)")[0])

        data = []
        with open(fnames, 'r') as file:
            data = file.readlines()
        
        self.data_for_analyze = []
        for sample in data:
            if len(sample) != 0:
                temp = sample.split(',')
                self.data_for_analyze.append(sum([int(channel) for channel in temp[1:]]))
                for key in self.zones.keys():
                    self.zone_2_data[key].append(0)
                for channel in range(self.numbers_of_sensor):
                    calibrated_value = self.ADC_value_mapping(int(temp[channel+1]))
                    
                    self.loaded_data[channel].append(calibrated_value)
                    for key, zone in self.zones.items():
                        if channel in zone:
                            self.zone_2_data[key][-1] += calibrated_value
        self.loaded_data = np.array(self.loaded_data)    
        for key, zone_line in self.zone_2_lines.items():
            zone_line.setData(np.linspace(0, len(data)/int(self.sampling_rate.currentText()), len(data)+1),np.array(self.zone_2_data[key]))
        
    def browse_file(self):
        fname = str(QtWidgets.QFileDialog.getSaveFileName()[0])
        self.full_path = ""
        if fname == '':
            path = os.path.expanduser("~\\Documents\\KMITL\\Plantar\\")
            if not os.path.exists(path):
                os.makedirs(path)
            fname = "default_filename.txt"
            self.path.setText(path+fname)
            self.full_path = path+fname
        elif fname.endswith(".txt"):
            self.path.setText(fname)
            self.full_path = fname
        else:
            self.path.setText(fname+".txt")
            self.full_path = fname+".txt"
        print(self.full_path)

    def set_save_state_fn(self):
        self.save_state = not self.save_state
        if self.save_state:
            self.set_save_state.setText("Stop")
            self.pause_save.setEnabled(True)
        else:
            self.set_save_state.setText("Start")
            self.pause_save.setDisabled(True)
            self.pause_save.setText("Pause")
            self.pause_state = False

    def pause_save_fn(self):
        self.pause_state = not self.pause_state
        if self.pause_state:
            self.pause_save.setText("Resume")
        else:
            self.pause_save.setText("Pause")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Plantar()
    # window.open_connection()
    window.show()
    app.exec()
    # window.close_connection()
