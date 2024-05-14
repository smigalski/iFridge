# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Nutzerfenster.ui'
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
    QSizePolicy, QStatusBar, QWidget, QFileDialog, QPushButton,)
class Ui_Nutzerfenster(object):
    def setupUi(self, Nutzerfenster):
        if not Nutzerfenster.objectName():
            Nutzerfenster.setObjectName(u"Nutzerfenster")
        Nutzerfenster.resize(800, 800)
        self.label = QLabel(Nutzerfenster)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 800, 800))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(Nutzerfenster)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 51, 71))
        self.label_2.setPixmap(QPixmap(u"../img/iFridge_klein.png"))
        self.pushButton = QPushButton(Nutzerfenster)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 600, 111, 71))

        self.retranslateUi(Nutzerfenster)

        QMetaObject.connectSlotsByName(Nutzerfenster)
    # setupUi

    def retranslateUi(self, Nutzerfenster):
        Nutzerfenster.setWindowTitle(QCoreApplication.translate("Nutzerfenster", u"iFridge", None))
        self.label.setText("")
        self.label_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("Nutzerfenster", u"Nutzer_1", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "Nutzerfenster.ui"
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

