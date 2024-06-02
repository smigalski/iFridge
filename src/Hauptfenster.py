import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtCore import QTimer, Qt

from src.Nutzerfenster import Ui_Nutzerfenster
from src.RGB_Einstellungen import RGBSlider


class Ui_QMainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_QMainWindow, self).__init__()
        uic.loadUi('Hauptfenster.ui', self)

        # Finde den Button aus der UI und verbinde ihn mit der Methode
        self.button = self.findChild(QPushButton, 'pushButton')
        self.button.clicked.connect(self.openNutzerfenster)

        self.labelRGBLeiste = self.findChild(QLabel, 'labelRGBLeiste')

        # Verbinde den Button mit der Methode
        self.button.clicked.connect(self.openRGBEinstellungen)

        self.rgb_einstellungen_window = None

    def updateRGBLeiste(self, color):
        self.labelRGBLeiste.setStyleSheet(f"background-color: {color};")


    def openRGBEinstellungen(self):
            self.rgb_einstellungen_window = RGBSlider()
            self.rgb_einstellungen_window.colorChanged.connect(self.updateRGBLeiste)
            self.rgb_einstellungen_window.show()

    def openNutzerfenster(self):
        self.window = Ui_Nutzerfenster()
        self.window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = Ui_QMainWindow()
    window.show()

    sys.exit(app.exec_())