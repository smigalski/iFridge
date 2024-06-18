import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton


class RGBSlider(QtWidgets.QWidget):


    def __init__(self, main_window):
        super(RGBSlider, self).__init__()
        uic.loadUi('RGB_Einstellungen.ui', self)

        self.main_window = main_window

        self.back_button = self.findChild(QPushButton, 'backButton')
        self.back_button.clicked.connect(self.back_button_clicked)

        # Verbinde die Slider mit der updateColor Methode
        self.Slider_rot1.valueChanged.connect(self.updateColor)
        self.Slider_gruen1.valueChanged.connect(self.updateColor)
        self.Slider_blau1.valueChanged.connect(self.updateColor)

        self.Slider_rot2.valueChanged.connect(self.updateColor)
        self.Slider_gruen2.valueChanged.connect(self.updateColor)
        self.Slider_blau2.valueChanged.connect(self.updateColor)

        self.updateColor()


    def updateColor(self):
        red1 = self.Slider_rot1.value()
        green1 = self.Slider_gruen1.value()
        blue1 = self.Slider_blau1.value()

        red2 = self.Slider_rot2.value()
        green2 = self.Slider_gruen2.value()
        blue2 = self.Slider_blau2.value()

        color1 = QColor(red1, green1, blue1)
        colorString1 = color1.name()

        color2 = QColor(red2, green2, blue2)
        colorString2 = color2.name()

        self.labelColor1.setStyleSheet(f"background-color: {colorString1};  color: white;  padding: 10px;  border-radius: 15px;")
        self.labelColor2.setStyleSheet(f"background-color: {colorString2};  color: white;  padding: 10px;  border-radius: 15px;")


    def back_button_clicked(self):
        self.main_window.openAllgemeineEinstellungen()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = RGBSlider(None)
    window.show()
    sys.exit(app.exec_())