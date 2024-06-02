import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QPushButton, QLabel, QScrollBar, QDial, QAbstractSlider

from src.RGB_Einstellungen import RGBSlider


class Ui_AllgemeineEinstellungen(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_AllgemeineEinstellungen, self).__init__()
        uic.loadUi('Allgemeine_Einstellungen.ui', self)

        # RGB Einstellungen Button wird gesucht, gefunden und mit der Methode verbunden das RGB_Einstellungen-Fenster zu öffnen
        self.button = self.findChild(QPushButton, 'pushButton')
        self.button.clicked.connect(self.openRGB_Einstellungen)

        # Es wird nach Temperatur Scrollbar gesucht, gefunden. Der gänderte Wert wird an die Ausgabemethode weitergegeben
        self.TempScrollBar = self.findChild(QScrollBar, 'TempScrollBar')
        self.TempScrollBar.valueChanged.connect(self.setTemperatur)

        # Es wird nach dem QLabel mit der Ausgabe gesucht
        self.label = self.findChild(QLabel, 'label_TempAusgabe')
        self.label2 = self.findChild(QLabel, 'label_HellAusgabe')

        #Es wird nach dem Helligkeitsregler (Dial) gesucht. Geänderte Wert wird an Ausgabemethode weitergeleitet
        self.HelligkeitDial = self.findChild(QDial, 'HelligkeitDial')
        self.HelligkeitDial.valueChanged.connect(self.setHelligkeit)


        self.setTemperatur()
    def openRGB_Einstellungen(self):  # Öffnet RGB_Einstellungen-Fenster
        self.window = RGBSlider()
        self.window.show()

    def setTemperatur(self): #Entnimmt den aktuellen Wert des Reglers, wandelt es in einen String um öndert den Text des QLabel
        temp_ausgabe = self.TempScrollBar.value()
        temp_ausgabe_text = str(temp_ausgabe)
        self.label.setText(f"{temp_ausgabe_text}")

    def setHelligkeit(self): #Entnimmt den aktuellen Wert des Reglers, wandelt es in einen String um öndert den Text des QLabel
        hell_ausgabe = self.HelligkeitDial.value()
        hell_ausgabe_text = str(hell_ausgabe)
        self.label2.setText(f'{hell_ausgabe_text}')




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_AllgemeineEinstellungen()
    window.show()
    sys.exit(app.exec_())

