# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recordwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PyQt5.QtCore import QThread, QObject, pyqtSignal

from pynput import keyboard
import sys
import csv
import threading
import datetime
import pandas as pd
from PyQt5.QtCore import QRunnable, QThreadPool, pyqtSignal

# import keyboard


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 40, 437, 260))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lMacroTitle = QtWidgets.QLabel(self.widget)
        self.lMacroTitle.setObjectName("lMacroTitle")
        self.verticalLayout.addWidget(self.lMacroTitle)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem2)
        self.teNameMacro = QtWidgets.QLineEdit(self.widget)
        self.teNameMacro.setObjectName("teNameMacro")
        self.verticalLayout.addWidget(self.teNameMacro)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem3)
        self.lExitButton = QtWidgets.QLabel(self.widget)
        self.lExitButton.setObjectName("lExitButton")
        self.verticalLayout.addWidget(self.lExitButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.bStartRecord = QtWidgets.QPushButton(self.widget)
        self.bStartRecord.setObjectName("bStartRecord")
        self.bStartRecord.clicked.connect(self.start_recording)

        self.horizontalLayout.addWidget(self.bStartRecord)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem4)
        self.bStopRecord = QtWidgets.QPushButton(self.widget)
        self.bStopRecord.setObjectName("bStopRecord")
        self.bStopRecord.clicked.connect(self.stop_recording)
        self.horizontalLayout.addWidget(self.bStopRecord)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem5)
        self.bSaveRecord = QtWidgets.QPushButton(self.widget)
        self.bSaveRecord.setObjectName("bSaveRecord")
        self.horizontalLayout.addWidget(self.bSaveRecord)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        self.menuProfiles = QtWidgets.QMenu(self.menubar)
        self.menuProfiles.setObjectName("menuProfiles")
        self.menuCreate_macro = QtWidgets.QMenu(self.menubar)
        self.menuCreate_macro.setObjectName("menuCreate_macro")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.menuSettings.addAction(self.actionExit)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionExit_2)
        self.menubar.addAction(self.menuProfiles.menuAction())
        self.menubar.addAction(self.menuCreate_macro.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lMacroTitle.setText(_translate("MainWindow", "Macro name"))
        self.lExitButton.setText(_translate("MainWindow", "Stop recording key: Esc"))
        self.bStartRecord.setText(_translate("MainWindow", "Start recording"))
        self.bStopRecord.setText(_translate("MainWindow", "Stop recording"))
        self.bSaveRecord.setText(_translate("MainWindow", "Save"))
        self.menuProfiles.setTitle(_translate("MainWindow", "Profiles"))
        self.menuCreate_macro.setTitle(_translate("MainWindow", "Create macro"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionExit.setText(_translate("MainWindow", "Select key to exit"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))

    def start_recording(self):
        file_name = self.teNameMacro.text() + ".csv"
        if file_name:
            print(f"Print: {file_name}")
            self.keyboard_recorder = KeyboardRecorderWrapper(
                file_name,
            )
            self.bStartRecord.setEnabled(False)
            self.bStopRecord.setEnabled(True)
            self.keyboard_recorder.start_recording()

    def stop_recording(self):
        try:
            self.keyboard_recorder.stop_recording()
            self.bStartRecord.setEnabled(True)
            self.bStopRecord.setEnabled(False)
        except Exception as e:
            print(f"Error stoping: {e}")


# TODO create thread class to use the layaout when the record code is being executed


# class KeyboardRecorder(QObject):
#     finished = pyqtSignal()

#     def __init__(self, file_name):
#         super().__init__()
#         self.file_name = file_name
#         self.recording = False
#         self.thread = None
#         self.keys = []

#     def start_recording(self):
#         self.recording = True
#         self.thread = QThread()
#         self.moveToThread(self.thread)
#         self.thread.started.connect(self._record_keyboard)
#         self.thread.start()

#     def stop_recording(self):
#         self.recording = False
#         self.thread.quit()
#         self.thread.wait()
#         df = pd.DataFrame(self.keys)
#         df.to_csv(self.file_name, index=False)
#         self.finished.emit()

#     def _record_keyboard(self):
#         with keyboard.Listener(on_press=self._on_press) as listener:
#             listener.join()

#     def _on_press(self, key):
#         self.keys.append(str(key))
#         print(f"Key {key} pressed")

#         if key == keyboard.Key.esc:
#             self.stop_recording()


class KeyboardRecorderSignals(QObject):
    finished = pyqtSignal()


class KeyboardRecorder(QRunnable):
    def __init__(self, file_name):
        super().__init__()
        self.signals = KeyboardRecorderSignals()
        self.file_name = file_name
        self.recording = False
        self.keys = []

    def run(self):
        with keyboard.Listener(on_press=self._on_press) as listener:
            listener.join()
        df = pd.DataFrame(self.keys)
        df.to_csv(self.file_name, index=False)
        self.signals.finished.emit()

    def _on_press(self, key):
        self.keys.append(str(key))
        print(f"Key {key} pressed")

        if key == keyboard.Key.esc:
            self.recording = False


class KeyboardRecorderWrapper:
    def __init__(self, file_name):
        self.file_name = file_name
        self.recording = False
        self.thread_pool = QThreadPool()

    def start_recording(self):
        self.recording = True
        worker = KeyboardRecorder(self.file_name)
        self.thread_pool.start(worker)

    def stop_recording(self):
        self.recording = False


def simulate_key_press(key):
    try:
        print(f"Key pressed: {key}")
        keyboard.press(key)
        keyboard.release(key)
    except AttributeError:
        print("Special key")
        special_keys = {
            "Key.alt_l": keyboard.Key.alt_l,
            "Key.alt_r": keyboard.Key.alt_r,
            "Key.backspace": keyboard.Key.backspace,
            "Key.cmd": keyboard.Key.cmd,
            "Key.ctrl_l": keyboard.Key.ctrl_l,
            "Key.ctrl_r": keyboard.Key.ctrl_r,
            "Key.delete": keyboard.Key.delete,
            "Key.down": keyboard.Key.down,
            "Key.end": keyboard.Key.end,
            "Key.enter": keyboard.Key.enter,
            "Key.esc": keyboard.Key.esc,
            "Key.f1": keyboard.Key.f1,
            "Key.f2": keyboard.Key.f2,
            "Key.f3": keyboard.Key.f3,
            "Key.f4": keyboard.Key.f4,
            "Key.f5": keyboard.Key.f5,
            "Key.f6": keyboard.Key.f6,
            "Key.f7": keyboard.Key.f7,
            "Key.f8": keyboard.Key.f8,
            "Key.f9": keyboard.Key.f9,
            "Key.f10": keyboard.Key.f10,
            "Key.f11": keyboard.Key.f11,
            "Key.f12": keyboard.Key.f12,
            "Key.home": keyboard.Key.home,
            "Key.left": keyboard.Key.left,
            "Key.page_down": keyboard.Key.page_down,
            "Key.page_up": keyboard.Key.page_up,
            "Key.right": keyboard.Key.right,
            "Key.shift_l": keyboard.Key.shift_l,
            "Key.shift_r": keyboard.Key.shift_r,
            "Key.space": keyboard.Key.space,
            "Key.tab": keyboard.Key.tab,
            "Key.up": keyboard.Key.up,
        }
        keyboard.press(special_keys[key])
        keyboard.release(special_keys[key])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
