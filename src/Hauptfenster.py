# -*- coding: utf-8 -*-
import subprocess

from PyQt5.uic.properties import QtCore
################################################################################
## Form generated from reading UI file 'Hauptfenster.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_QMainWindow(object):
    def setupUi(self, QMainWindow):
        if not QMainWindow.objectName():
            QMainWindow.setObjectName(u"QMainWindow")
        QMainWindow.resize(800, 800)
        self.centralwidget = QWidget(QMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(340, 60, 121, 61))
        self.pushButton.setStyleSheet(u"font: 700 12pt \"Terminal\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 80, 131, 31))
        self.label_3.setStyleSheet(u"font: 700 9pt \"Terminal\";")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 40, 801, 801))
        self.label.setPixmap(QPixmap(u"../img/K\u00fchlschrank_Bild.jpg.png"))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 791, 801))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        QMainWindow.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.statusbar = QStatusBar(QMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        QMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(QMainWindow)

        self.pushButton.setDefault(False)

        self.pushButton.clicked.connect(self.openNutzerfenster)


    def openNutzerfenster(self):
        if self.pushButton.isChecked():
            app = QApplication(sys.argv)

            ui_file_name = "Nutzerfenster.py"
            ui_file = QFile(ui_file_name)
            if not ui_file.open(QIODevice.ReadOnly):
                print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
                sys.exit(-1)
            loader = QUiLoader()
            window = loader.load(ui_file)
            ui_file.close()
            if not window:
                print(loader.errorString())
                sys.exit(-1)
            window.show()

            sys.exit(app.exec())




        QMetaObject.connectSlotsByName(QMainWindow)


    def retranslateUi(self, QMainWindow):
        QMainWindow.setWindowTitle(QCoreApplication.translate("QMainWindow", u"iFridge", None))
        self.pushButton.setText(QCoreApplication.translate("QMainWindow", u"iFridge", None))
        self.label_3.setText(QCoreApplication.translate("QMainWindow", u"click here ------> ", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("QMainWindow", u"TextLabel", None))
    # retranslateUi

import sys
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QLabel, QMainWindow,
    QSizePolicy, QStatusBar, QWidget, QFileDialog)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "Hauptfenster.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    sys.exit(app.exec())