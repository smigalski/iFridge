# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Hauptfenster.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from subprocess import call
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,)
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence,  QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QLabel, QMainWindow,
    QSizePolicy, QStatusBar, QWidget, QFileDialog)

class Ui_QMainWindow(object):
    def setupUi(self, QMainWindow):
        if not QMainWindow.objectName():
            QMainWindow.setObjectName(u"QMainWindow")
        QMainWindow.resize(800, 800)
        self.centralwidget = QWidget(QMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 801, 801))
        self.label_2.setPixmap(QPixmap(u"../img/K\u00fchlschrank_Bild.jpg"))
        self.commandLinkButton = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(350, 160, 131, 81))
        self.commandLinkButton.setText(u"iFridge")
        icon = QIcon()
        icon.addFile(u"../img/iFridge_klein.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setIconSize(QSize(50, 67))
        self.commandLinkButton.setCheckable(False)
        self.commandLinkButton.setAutoDefault(False)
        QMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(QMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        QMainWindow.setStatusBar(self.statusbar)

        self.commandLinkButton.clicked.connect(self.openNutzerfenster)

        self.retranslateUi(QMainWindow)

        QMetaObject.connectSlotsByName(QMainWindow)

    # setupUi


    def retranslateUi(self, QMainWindow):
        QMainWindow.setWindowTitle(QCoreApplication.translate("QMainWindow", u"iFridge", None))
        self.label_2.setText("")
    # retranslateUi

    def openNutzerfenster(self):
        call(["python", "Nutzerfenster.py"])




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






