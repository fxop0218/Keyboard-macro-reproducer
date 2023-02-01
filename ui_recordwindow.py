# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recordwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 390)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionExit_2 = QAction(MainWindow)
        self.actionExit_2.setObjectName(u"actionExit_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 40, 437, 260))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lMacroTitle = QLabel(self.widget)
        self.lMacroTitle.setObjectName(u"lMacroTitle")

        self.verticalLayout.addWidget(self.lMacroTitle)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.teNameMacro = QLineEdit(self.widget)
        self.teNameMacro.setObjectName(u"teNameMacro")

        self.verticalLayout.addWidget(self.teNameMacro)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lExitButton = QLabel(self.widget)
        self.lExitButton.setObjectName(u"lExitButton")

        self.verticalLayout.addWidget(self.lExitButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bStartRecord = QPushButton(self.widget)
        self.bStartRecord.setObjectName(u"bStartRecord")

        self.horizontalLayout.addWidget(self.bStartRecord)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bStopRecord = QPushButton(self.widget)
        self.bStopRecord.setObjectName(u"bStopRecord")

        self.horizontalLayout.addWidget(self.bStopRecord)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.bSaveRecord = QPushButton(self.widget)
        self.bSaveRecord.setObjectName(u"bSaveRecord")

        self.horizontalLayout.addWidget(self.bSaveRecord)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 21))
        self.menuProfiles = QMenu(self.menubar)
        self.menuProfiles.setObjectName(u"menuProfiles")
        self.menuCreate_macro = QMenu(self.menubar)
        self.menuCreate_macro.setObjectName(u"menuCreate_macro")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuProfiles.menuAction())
        self.menubar.addAction(self.menuCreate_macro.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuSettings.addAction(self.actionExit)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionExit_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Select key to exit", None))
        self.actionExit_2.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.lMacroTitle.setText(QCoreApplication.translate("MainWindow", u"Macro name", None))
        self.lExitButton.setText(QCoreApplication.translate("MainWindow", u"Stop recording key: Esc", None))
        self.bStartRecord.setText(QCoreApplication.translate("MainWindow", u"Start recording", None))
        self.bStopRecord.setText(QCoreApplication.translate("MainWindow", u"Stop recording", None))
        self.bSaveRecord.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuProfiles.setTitle(QCoreApplication.translate("MainWindow", u"Profiles", None))
        self.menuCreate_macro.setTitle(QCoreApplication.translate("MainWindow", u"Create macro", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

