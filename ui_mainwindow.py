# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(339, 327)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lSelectProfile = QLabel(self.centralwidget)
        self.lSelectProfile.setObjectName(u"lSelectProfile")
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(12)
        self.lSelectProfile.setFont(font)

        self.verticalLayout.addWidget(self.lSelectProfile)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.cbSelectMacro = QComboBox(self.centralwidget)
        self.cbSelectMacro.setObjectName(u"cbSelectMacro")

        self.horizontalLayout_3.addWidget(self.cbSelectMacro)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.sbNumberRepeats = QSpinBox(self.centralwidget)
        self.sbNumberRepeats.setObjectName(u"sbNumberRepeats")

        self.horizontalLayout_3.addWidget(self.sbNumberRepeats)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.cbRepeat = QCheckBox(self.centralwidget)
        self.cbRepeat.setObjectName(u"cbRepeat")

        self.verticalLayout.addWidget(self.cbRepeat)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.bStartMacro = QPushButton(self.centralwidget)
        self.bStartMacro.setObjectName(u"bStartMacro")

        self.horizontalLayout.addWidget(self.bStartMacro)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bDeleteMacro = QPushButton(self.centralwidget)
        self.bDeleteMacro.setObjectName(u"bDeleteMacro")

        self.horizontalLayout.addWidget(self.bDeleteMacro)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 339, 21))
        self.menuProfiles = QMenu(self.menubar)
        self.menuProfiles.setObjectName(u"menuProfiles")
        self.menuCreate_profiles = QMenu(self.menubar)
        self.menuCreate_profiles.setObjectName(u"menuCreate_profiles")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuProfiles.menuAction())
        self.menubar.addAction(self.menuCreate_profiles.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lSelectProfile.setText(QCoreApplication.translate("MainWindow", u"Select profile", None))
        self.cbRepeat.setText(QCoreApplication.translate("MainWindow", u"Repeat", None))
        self.bStartMacro.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.bDeleteMacro.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.menuProfiles.setTitle(QCoreApplication.translate("MainWindow", u"Profiles", None))
        self.menuCreate_profiles.setTitle(QCoreApplication.translate("MainWindow", u"Create macro", None))
    # retranslateUi

