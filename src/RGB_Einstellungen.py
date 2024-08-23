import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton, QApplication
class RGBSlider(QtWidgets.QWidget):

    def __init__(self, main_window):
        super(RGBSlider, self).__init__()
        uic.loadUi('RGB_Einstellungen.ui', self)                          # Lädt die Benutzeroberfläche aus der .ui-Datei

        self.main_window = main_window
        self.hauptfenster = None                                                # Referenz auf das Hauptfenster

        self.back_button = self.findChild(QPushButton, 'backButton')            # Sucht und speichert den Zurück-Button
        self.back_button.clicked.connect(self.back_button_clicked)              # Verbindet den Zurück-Button mit der entsprechenden Klick-Methode


        self.Slider_rot1.valueChanged.connect(self.updateColor)                 # Verbindet die Slider mit der updateColor Methode
        self.Slider_gruen1.valueChanged.connect(self.updateColor)
        self.Slider_blau1.valueChanged.connect(self.updateColor)

        self.Slider_rot2.valueChanged.connect(self.updateColor)                 # Verbindet den Rot-Slider 2 mit der Farbaktualisierungsmethode
        self.Slider_gruen2.valueChanged.connect(self.updateColor)
        self.Slider_blau2.valueChanged.connect(self.updateColor)

        self.Slider_rot2.valueChanged.connect(self.openMainWindow_RGB)          # Verbindet den Rot-Slider 2 mit der Methode, um das Hauptfenster zu öffnen
        self.Slider_gruen2.valueChanged.connect(self.openMainWindow_RGB)
        self.Slider_blau2.valueChanged.connect(self.openMainWindow_RGB)

        self.updateColor()                                                      # Aktualisiert die Farbe direkt bei der Initialisierung

    def openMainWindow_RGB(self):
        if self.hauptfenster is None:

            self.hauptfenster = uic.loadUi('Hauptfenster.ui')                   # Laden des Hauptfensters

            current_geometry = self.geometry()                                  # Position des aktuellen Fensters abrufen
            current_x = current_geometry.x()
            current_y = current_geometry.y()
            current_width = current_geometry.width()

            new_x = current_x + current_width + 10                              # Position des neuen Fensters neben dem aktuellen Fenster setzen
            new_y = current_y
            self.hauptfenster.move(new_x, new_y)

            self.hauptfenster.show()                                            # Anzeigen des neuen Fensters


        self.updateMainWindowLabelColor()                                       # Aktualisiert die Farbe des Labels im Hauptfenster

    def updateColor(self):                                                      # Liest die Werte der Slider und aktualisiert die Farben
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

        self.labelColor1.setStyleSheet(f"background-color: {colorString1};  color: white;  padding: 10px;  border-radius: 15px;") # Setzt die Hintergrundfarbe der Labels in der aktuellen Benutzeroberfläche
        self.labelColor2.setStyleSheet(f"background-color: {colorString2};  color: white;  padding: 10px;  border-radius: 15px;")

        if self.hauptfenster is not None:
            self.updateMainWindowLabelColor()                                   # Aktualisiere die Farbe des Labels im Hauptfenster

    def updateMainWindowLabelColor(self):
        if self.hauptfenster is not None:                                       # Aktualisiere die Farbe des QLabel im Hauptfenster, wenn vorhanden
            color2 = QColor(self.Slider_rot2.value(), self.Slider_gruen2.value(), self.Slider_blau2.value())
            colorString2 = color2.name()
            label_in_main_window = self.hauptfenster.findChild(QtWidgets.QLabel, 'labelRGBLeiste')
            if label_in_main_window is not None:
                label_in_main_window.setStyleSheet(f"background-color: {colorString2};")

    def back_button_clicked(self):                                              # Öffnet das Fenster für allgemeine Einstellungen, wenn der Zurück-Button geklickt wird
        self.main_window.openAllgemeineEinstellungen()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RGBSlider(None)
    window.show()
    sys.exit(app.exec_())                                                       # Startet die Anwendung und zeigt das Fenster an