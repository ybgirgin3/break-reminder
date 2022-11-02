# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'break_timerKsVBZo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 177)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.break_time_length_label = QLabel(self.centralwidget)
        self.break_time_length_label.setObjectName("break_time_length_label")
        self.break_time_length_label.setGeometry(QRect(9, 72, 151, 17))
        self.work_time_length_label = QLabel(self.centralwidget)
        self.work_time_length_label.setObjectName("work_time_length_label")
        self.work_time_length_label.setGeometry(QRect(9, 40, 123, 17))
        self.session_name_label = QLabel(self.centralwidget)
        self.session_name_label.setObjectName("session_name_label")
        self.session_name_label.setGeometry(QRect(9, 9, 168, 17))
        self.work_time_spin_box = QDoubleSpinBox(self.centralwidget)
        self.work_time_spin_box.setObjectName("work_time_spin_box")
        self.work_time_spin_box.setGeometry(QRect(180, 40, 65, 26))
        self.session_name_input = QLineEdit(self.centralwidget)
        self.session_name_input.setObjectName("session_name_input")
        self.session_name_input.setGeometry(QRect(183, 9, 151, 25))
        self.work_time_dropdown = QComboBox(self.centralwidget)
        self.work_time_dropdown.setObjectName("work_time_dropdown")
        self.work_time_dropdown.setGeometry(QRect(250, 40, 86, 25))
        self.break_time_spin_box = QDoubleSpinBox(self.centralwidget)
        self.break_time_spin_box.setObjectName("break_time_spin_box")
        self.break_time_spin_box.setGeometry(QRect(180, 70, 65, 26))
        self.break_time_dropdown = QComboBox(self.centralwidget)
        self.break_time_dropdown.setObjectName("break_time_dropdown")
        self.break_time_dropdown.setGeometry(QRect(250, 70, 86, 25))
        self.is_full_day = QCheckBox(self.centralwidget)
        self.is_full_day.setObjectName("is_full_day")
        self.is_full_day.setGeometry(QRect(350, 10, 141, 23))
        self.start_button_label = QPushButton(self.centralwidget)
        self.start_button_label.setObjectName("start_button_label")
        self.start_button_label.setGeometry(QRect(320, 100, 91, 25))
        self.close_button_label = QPushButton(self.centralwidget)
        self.close_button_label.setObjectName("close_button_label")
        self.close_button_label.setGeometry(QRect(420, 100, 91, 25))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 529, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.break_time_length_label.setText(
            QCoreApplication.translate("MainWindow", "Break Time Length:", None)
        )
        self.work_time_length_label.setText(
            QCoreApplication.translate("MainWindow", "Work Time Length:", None)
        )
        self.session_name_label.setText(
            QCoreApplication.translate("MainWindow", "Session Name (optional): ", None)
        )
        self.session_name_input.setText("")
        self.session_name_input.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Default Session Name", None)
        )
        self.is_full_day.setText(
            QCoreApplication.translate("MainWindow", "Full Day Of Work", None)
        )
        self.start_button_label.setText(
            QCoreApplication.translate("MainWindow", "Start", None)
        )
        self.close_button_label.setText(
            QCoreApplication.translate("MainWindow", "Close", None)
        )

    # retranslateUi
