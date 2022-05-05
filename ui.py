# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plantar.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QToolButton,
    QVBoxLayout, QWidget)

from pyqtgraph import (ImageView, PlotWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1058, 542)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabsClosable(False)
        self.raw_plot = QWidget()
        self.raw_plot.setObjectName(u"raw_plot")
        self.horizontalLayout = QHBoxLayout(self.raw_plot)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.zone_plot = QVBoxLayout()
        self.zone_plot.setObjectName(u"zone_plot")
        self.plot = QHBoxLayout()
        self.plot.setObjectName(u"plot")
        self.raw = PlotWidget(self.raw_plot)
        self.raw.setObjectName(u"raw")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.raw.sizePolicy().hasHeightForWidth())
        self.raw.setSizePolicy(sizePolicy)

        self.plot.addWidget(self.raw)

        self.heatmap = PlotWidget(self.raw_plot)
        self.heatmap.setObjectName(u"heatmap")
        self.heatmap.setMaximumSize(QSize(350, 16777215))

        self.plot.addWidget(self.heatmap)


        self.zone_plot.addLayout(self.plot)

        self.save = QGroupBox(self.raw_plot)
        self.save.setObjectName(u"save")
        sizePolicy.setHeightForWidth(self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy)
        self.save.setMinimumSize(QSize(660, 60))
        self.save.setMaximumSize(QSize(16777215, 60))
        self.save.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.gridLayout_2 = QGridLayout(self.save)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_8 = QLabel(self.save)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.path = QLineEdit(self.save)
        self.path.setObjectName(u"path")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.path.sizePolicy().hasHeightForWidth())
        self.path.setSizePolicy(sizePolicy2)
        self.path.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.path, 0, 1, 1, 1)

        self.browse = QToolButton(self.save)
        self.browse.setObjectName(u"browse")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.browse.sizePolicy().hasHeightForWidth())
        self.browse.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.browse, 0, 2, 1, 1)

        self.set_save_state = QPushButton(self.save)
        self.set_save_state.setObjectName(u"set_save_state")
        sizePolicy3.setHeightForWidth(self.set_save_state.sizePolicy().hasHeightForWidth())
        self.set_save_state.setSizePolicy(sizePolicy3)
        self.set_save_state.setAutoDefault(False)

        self.gridLayout_2.addWidget(self.set_save_state, 0, 3, 1, 1)

        self.pause_save = QPushButton(self.save)
        self.pause_save.setObjectName(u"pause_save")
        self.pause_save.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.pause_save.sizePolicy().hasHeightForWidth())
        self.pause_save.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.pause_save, 0, 4, 1, 1)


        self.zone_plot.addWidget(self.save)


        self.horizontalLayout.addLayout(self.zone_plot)

        self.zone_settting = QVBoxLayout()
        self.zone_settting.setObjectName(u"zone_settting")
        self.zone_settting.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.logo = QLabel(self.raw_plot)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(162, 81))
        self.logo.setPixmap(QPixmap(u"../../../../.designer/backup/Kmitl.jpg"))

        self.zone_settting.addWidget(self.logo, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.plot_setting = QGroupBox(self.raw_plot)
        self.plot_setting.setObjectName(u"plot_setting")
        self.plot_setting.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.plot_setting.sizePolicy().hasHeightForWidth())
        self.plot_setting.setSizePolicy(sizePolicy4)
        self.plot_setting.setMinimumSize(QSize(200, 220))
        self.plot_setting.setMaximumSize(QSize(220, 16777215))
        self.plot_setting.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.gridLayout_3 = QGridLayout(self.plot_setting)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.set_window_size = QPushButton(self.plot_setting)
        self.set_window_size.setObjectName(u"set_window_size")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.set_window_size.sizePolicy().hasHeightForWidth())
        self.set_window_size.setSizePolicy(sizePolicy5)

        self.gridLayout_3.addWidget(self.set_window_size, 10, 2, 1, 1)

        self.label_10 = QLabel(self.plot_setting)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 6, 0, 1, 1)

        self.window_size = QSpinBox(self.plot_setting)
        self.window_size.setObjectName(u"window_size")
        sizePolicy5.setHeightForWidth(self.window_size.sizePolicy().hasHeightForWidth())
        self.window_size.setSizePolicy(sizePolicy5)
        self.window_size.setAccelerated(True)
        self.window_size.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.window_size.setMinimum(1000)
        self.window_size.setMaximum(10000)
        self.window_size.setSingleStep(100)
        self.window_size.setValue(1000)

        self.gridLayout_3.addWidget(self.window_size, 10, 0, 1, 1)

        self.label_11 = QLabel(self.plot_setting)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)

        self.packet_size = QSpinBox(self.plot_setting)
        self.packet_size.setObjectName(u"packet_size")
        sizePolicy5.setHeightForWidth(self.packet_size.sizePolicy().hasHeightForWidth())
        self.packet_size.setSizePolicy(sizePolicy5)
        self.packet_size.setAccelerated(True)
        self.packet_size.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.packet_size.setMinimum(5)
        self.packet_size.setMaximum(80)
        self.packet_size.setValue(20)

        self.gridLayout_3.addWidget(self.packet_size, 4, 0, 1, 1)

        self.label_7 = QLabel(self.plot_setting)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 1)

        self.sampling_rate = QComboBox(self.plot_setting)
        self.sampling_rate.addItem("")
        self.sampling_rate.addItem("")
        self.sampling_rate.setObjectName(u"sampling_rate")
        sizePolicy5.setHeightForWidth(self.sampling_rate.sizePolicy().hasHeightForWidth())
        self.sampling_rate.setSizePolicy(sizePolicy5)

        self.gridLayout_3.addWidget(self.sampling_rate, 1, 2, 1, 1)

        self.set_packet_size = QPushButton(self.plot_setting)
        self.set_packet_size.setObjectName(u"set_packet_size")
        sizePolicy5.setHeightForWidth(self.set_packet_size.sizePolicy().hasHeightForWidth())
        self.set_packet_size.setSizePolicy(sizePolicy5)

        self.gridLayout_3.addWidget(self.set_packet_size, 4, 2, 1, 1)


        self.zone_settting.addWidget(self.plot_setting, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.set_plot_state = QPushButton(self.raw_plot)
        self.set_plot_state.setObjectName(u"set_plot_state")
        sizePolicy3.setHeightForWidth(self.set_plot_state.sizePolicy().hasHeightForWidth())
        self.set_plot_state.setSizePolicy(sizePolicy3)
        self.set_plot_state.setMaximumSize(QSize(220, 16777215))

        self.zone_settting.addWidget(self.set_plot_state)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.zone_settting.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.zone_settting)

        self.tabWidget.addTab(self.raw_plot, "")
        self.analyze = QWidget()
        self.analyze.setObjectName(u"analyze")
        self.horizontalLayout_2 = QHBoxLayout(self.analyze)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.zone_plot_2 = QVBoxLayout()
        self.zone_plot_2.setObjectName(u"zone_plot_2")
        self.groupBox = QGroupBox(self.analyze)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.load_data_path = QLineEdit(self.groupBox)
        self.load_data_path.setObjectName(u"load_data_path")
        sizePolicy2.setHeightForWidth(self.load_data_path.sizePolicy().hasHeightForWidth())
        self.load_data_path.setSizePolicy(sizePolicy2)
        self.load_data_path.setClearButtonEnabled(False)

        self.horizontalLayout_3.addWidget(self.load_data_path)

        self.load_btn = QPushButton(self.groupBox)
        self.load_btn.setObjectName(u"load_btn")
        sizePolicy3.setHeightForWidth(self.load_btn.sizePolicy().hasHeightForWidth())
        self.load_btn.setSizePolicy(sizePolicy3)
        self.load_btn.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.load_btn)


        self.zone_plot_2.addWidget(self.groupBox)

        self.plot_2 = QHBoxLayout()
        self.plot_2.setObjectName(u"plot_2")
        self.raw_2 = PlotWidget(self.analyze)
        self.raw_2.setObjectName(u"raw_2")
        sizePolicy.setHeightForWidth(self.raw_2.sizePolicy().hasHeightForWidth())
        self.raw_2.setSizePolicy(sizePolicy)

        self.plot_2.addWidget(self.raw_2)

        self.heatmap_2 = ImageView(self.analyze)
        self.heatmap_2.setObjectName(u"heatmap_2")
        self.heatmap_2.setMaximumSize(QSize(350, 16777215))

        self.plot_2.addWidget(self.heatmap_2)


        self.zone_plot_2.addLayout(self.plot_2)


        self.horizontalLayout_2.addLayout(self.zone_plot_2)

        self.gait_param_layout = QVBoxLayout()
        self.gait_param_layout.setObjectName(u"gait_param_layout")
        self.gait_param_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gait_param_group = QGroupBox(self.analyze)
        self.gait_param_group.setObjectName(u"gait_param_group")
        self.gait_param_group.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.gait_param_group.sizePolicy().hasHeightForWidth())
        self.gait_param_group.setSizePolicy(sizePolicy1)
        self.gait_param_group.setMinimumSize(QSize(200, 0))
        self.gait_param_group.setMaximumSize(QSize(220, 16777215))
        self.gait_param_group.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.gridLayout_5 = QGridLayout(self.gait_param_group)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.stance_p_unit = QLabel(self.gait_param_group)
        self.stance_p_unit.setObjectName(u"stance_p_unit")

        self.gridLayout_5.addWidget(self.stance_p_unit, 5, 2, 1, 1)

        self.step_t = QLabel(self.gait_param_group)
        self.step_t.setObjectName(u"step_t")

        self.gridLayout_5.addWidget(self.step_t, 1, 1, 1, 1)

        self.swing_p_label = QLabel(self.gait_param_group)
        self.swing_p_label.setObjectName(u"swing_p_label")

        self.gridLayout_5.addWidget(self.swing_p_label, 7, 0, 1, 1)

        self.swing_p_unit = QLabel(self.gait_param_group)
        self.swing_p_unit.setObjectName(u"swing_p_unit")

        self.gridLayout_5.addWidget(self.swing_p_unit, 7, 2, 1, 1)

        self.stance_p = QLabel(self.gait_param_group)
        self.stance_p.setObjectName(u"stance_p")

        self.gridLayout_5.addWidget(self.stance_p, 5, 1, 1, 1)

        self.stride_t_label = QLabel(self.gait_param_group)
        self.stride_t_label.setObjectName(u"stride_t_label")

        self.gridLayout_5.addWidget(self.stride_t_label, 2, 0, 1, 1)

        self.cadence_unit = QLabel(self.gait_param_group)
        self.cadence_unit.setObjectName(u"cadence_unit")

        self.gridLayout_5.addWidget(self.cadence_unit, 0, 2, 1, 1)

        self.swing_p = QLabel(self.gait_param_group)
        self.swing_p.setObjectName(u"swing_p")

        self.gridLayout_5.addWidget(self.swing_p, 7, 1, 1, 1)

        self.stride_t = QLabel(self.gait_param_group)
        self.stride_t.setObjectName(u"stride_t")

        self.gridLayout_5.addWidget(self.stride_t, 2, 1, 1, 1)

        self.stance_p_label = QLabel(self.gait_param_group)
        self.stance_p_label.setObjectName(u"stance_p_label")

        self.gridLayout_5.addWidget(self.stance_p_label, 5, 0, 1, 1)

        self.stance_t_unit = QLabel(self.gait_param_group)
        self.stance_t_unit.setObjectName(u"stance_t_unit")

        self.gridLayout_5.addWidget(self.stance_t_unit, 3, 2, 1, 1)

        self.stride_t_unit = QLabel(self.gait_param_group)
        self.stride_t_unit.setObjectName(u"stride_t_unit")

        self.gridLayout_5.addWidget(self.stride_t_unit, 2, 2, 1, 1)

        self.stance_t_label = QLabel(self.gait_param_group)
        self.stance_t_label.setObjectName(u"stance_t_label")

        self.gridLayout_5.addWidget(self.stance_t_label, 3, 0, 1, 1)

        self.step_t_unit = QLabel(self.gait_param_group)
        self.step_t_unit.setObjectName(u"step_t_unit")

        self.gridLayout_5.addWidget(self.step_t_unit, 1, 2, 1, 1)

        self.step_t_label = QLabel(self.gait_param_group)
        self.step_t_label.setObjectName(u"step_t_label")

        self.gridLayout_5.addWidget(self.step_t_label, 1, 0, 1, 1)

        self.cadence = QLabel(self.gait_param_group)
        self.cadence.setObjectName(u"cadence")

        self.gridLayout_5.addWidget(self.cadence, 0, 1, 1, 1)

        self.cadence_label = QLabel(self.gait_param_group)
        self.cadence_label.setObjectName(u"cadence_label")

        self.gridLayout_5.addWidget(self.cadence_label, 0, 0, 1, 1)

        self.stance_t = QLabel(self.gait_param_group)
        self.stance_t.setObjectName(u"stance_t")

        self.gridLayout_5.addWidget(self.stance_t, 3, 1, 1, 1)

        self.swing_t_label = QLabel(self.gait_param_group)
        self.swing_t_label.setObjectName(u"swing_t_label")

        self.gridLayout_5.addWidget(self.swing_t_label, 4, 0, 1, 1)

        self.swing_t = QLabel(self.gait_param_group)
        self.swing_t.setObjectName(u"swing_t")

        self.gridLayout_5.addWidget(self.swing_t, 4, 1, 1, 1)

        self.swing_t_unit = QLabel(self.gait_param_group)
        self.swing_t_unit.setObjectName(u"swing_t_unit")

        self.gridLayout_5.addWidget(self.swing_t_unit, 4, 2, 1, 1)


        self.gait_param_layout.addWidget(self.gait_param_group)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gait_param_layout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.gait_param_layout)

        self.tabWidget.addTab(self.analyze, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.sampling_rate.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.save.setTitle(QCoreApplication.translate("MainWindow", u"Save Raw Data", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Path to file", None))
        self.browse.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.set_save_state.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pause_save.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.logo.setText("")
        self.plot_setting.setTitle(QCoreApplication.translate("MainWindow", u"Plot Setting", None))
        self.set_window_size.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Window size", None))
#if QT_CONFIG(whatsthis)
        self.window_size.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.window_size.setSuffix(QCoreApplication.translate("MainWindow", u" sample", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Sampling Rate", None))
#if QT_CONFIG(whatsthis)
        self.packet_size.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.packet_size.setSuffix(QCoreApplication.translate("MainWindow", u" sample", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Packet size", None))
        self.sampling_rate.setItemText(0, QCoreApplication.translate("MainWindow", u"200", None))
        self.sampling_rate.setItemText(1, QCoreApplication.translate("MainWindow", u"100", None))

        self.set_packet_size.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.set_plot_state.setText(QCoreApplication.translate("MainWindow", u"Start Plotting", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.raw_plot), QCoreApplication.translate("MainWindow", u"Visualize", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Load data to analyze", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Path to file", None))
        self.load_btn.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.gait_param_group.setTitle(QCoreApplication.translate("MainWindow", u"Gait parameters", None))
        self.stance_p_unit.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.step_t.setText("")
        self.swing_p_label.setText(QCoreApplication.translate("MainWindow", u"Swing phase", None))
        self.swing_p_unit.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.stance_p.setText("")
        self.stride_t_label.setText(QCoreApplication.translate("MainWindow", u"Stride time", None))
        self.cadence_unit.setText(QCoreApplication.translate("MainWindow", u"steps/min", None))
        self.swing_p.setText("")
        self.stride_t.setText("")
        self.stance_p_label.setText(QCoreApplication.translate("MainWindow", u"Stance phase", None))
        self.stance_t_unit.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.stride_t_unit.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.stance_t_label.setText(QCoreApplication.translate("MainWindow", u"Stance time", None))
        self.step_t_unit.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.step_t_label.setText(QCoreApplication.translate("MainWindow", u"Step time", None))
        self.cadence.setText("")
        self.cadence_label.setText(QCoreApplication.translate("MainWindow", u"Cadence", None))
        self.stance_t.setText("")
        self.swing_t_label.setText(QCoreApplication.translate("MainWindow", u"Swing time", None))
        self.swing_t.setText("")
        self.swing_t_unit.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analyze), QCoreApplication.translate("MainWindow", u"Analyze", None))
    # retranslateUi

