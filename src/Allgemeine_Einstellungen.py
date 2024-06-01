import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QPushButton

from src.RGB_Einstellungen import RGBSlider

class Ui_AllgemeineEinstellungen(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_AllgemeineEinstellungen, self).__init__()
        uic.loadUi('Allgemeine_Einstellungen.ui', self)

        self.button = self.findChild(QPushButton, 'pushButton')
        self.button.clicked.connect(self.openRGB_Einstellungen)

    def openRGB_Einstellungen(self):
        self.window = RGBSlider()
        self.window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_AllgemeineEinstellungen()
    window.show()
    sys.exit(app.exec_())
