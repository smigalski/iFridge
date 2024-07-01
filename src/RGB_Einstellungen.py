import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton, QApplication


class RGBSlider(QtWidgets.QWidget):

    def __init__(self, main_window):
        super(RGBSlider, self).__init__()
        uic.loadUi('RGB_Einstellungen.ui', self)

        self.main_window = main_window
        self.hauptfenster = None  # Referenz auf das Hauptfenster

        self.back_button = self.findChild(QPushButton, 'backButton')
        self.back_button.clicked.connect(self.back_button_clicked)

        # Verbinde die Slider mit der updateColor Methode
        self.Slider_rot1.valueChanged.connect(self.updateColor)
        self.Slider_gruen1.valueChanged.connect(self.updateColor)
        self.Slider_blau1.valueChanged.connect(self.updateColor)

        self.Slider_rot2.valueChanged.connect(self.updateColor)
        self.Slider_gruen2.valueChanged.connect(self.updateColor)
        self.Slider_blau2.valueChanged.connect(self.updateColor)

        self.Slider_rot2.valueChanged.connect(self.openMainWindow_RGB)
        self.Slider_gruen2.valueChanged.connect(self.openMainWindow_RGB)
        self.Slider_blau2.valueChanged.connect(self.openMainWindow_RGB)

        self.updateColor()

    def openMainWindow_RGB(self):
        if self.hauptfenster is None:
            # Laden des Hauptfensters
            self.hauptfenster = uic.loadUi('Hauptfenster.ui')

            # Position des aktuellen Fensters abrufen
            current_geometry = self.geometry()
            current_x = current_geometry.x()
            current_y = current_geometry.y()
            current_width = current_geometry.width()

            # Position des neuen Fensters neben dem aktuellen Fenster setzen
            new_x = current_x + current_width + 10  # 10 Pixel Abstand
            new_y = current_y
            self.hauptfenster.move(new_x, new_y)

            # Anzeigen des neuen Fensters
            self.hauptfenster.show()

        # Aktualisiere die Farbe des Labels im Hauptfenster
        self.updateMainWindowLabelColor()

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

        if self.hauptfenster is not None:
            # Aktualisiere die Farbe des Labels im Hauptfenster
            self.updateMainWindowLabelColor()

    def updateMainWindowLabelColor(self):
        # Aktualisiere die Farbe des QLabel im Hauptfenster, wenn vorhanden
        if self.hauptfenster is not None:
            color2 = QColor(self.Slider_rot2.value(), self.Slider_gruen2.value(), self.Slider_blau2.value())
            colorString2 = color2.name()
            label_in_main_window = self.hauptfenster.findChild(QtWidgets.QLabel, 'labelRGBLeiste')
            if label_in_main_window is not None:
                label_in_main_window.setStyleSheet(f"background-color: {colorString2};")

    def back_button_clicked(self):
        self.main_window.openAllgemeineEinstellungen()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RGBSlider(None)
    window.show()
    sys.exit(app.exec_())
