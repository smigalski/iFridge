import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QPushButton, QLabel, QScrollBar, QDial

class Ui_AllgemeineEinstellungen(QtWidgets.QWidget):
    def __init__(self, main_window):
        super(Ui_AllgemeineEinstellungen, self).__init__()
        uic.loadUi('Allgemeine_Einstellungen.ui', self)

        self.main_window = main_window

        self.backbutton = self.findChild(QPushButton, 'backButton')                         # Verbindet den Zurück-Button mit der Rückkehr zum Hauptfenster
        self.backbutton.clicked.connect(self.back_button_clicked)

        self.button = self.findChild(QPushButton, 'pushButton')                             # RGB Einstellungen Button wird gesucht, gefunden und mit der Methode verbunden das RGB_Einstellungen-Fenster zu öffnen
        self.button.clicked.connect(self.btnOpenRGB_Einstellungen)

        self.TempScrollBar = self.findChild(QScrollBar, 'TempScrollBar')                    # Es wird nach Temperatur Scrollbar gesucht, gefunden. Der gänderte Wert wird an die Ausgabemethode weitergegeben
        self.TempScrollBar.valueChanged.connect(self.setTemperatur)

        self.label = self.findChild(QLabel, 'label_TempAusgabe')                            # Es wird nach dem QLabel mit der Ausgabe gesucht
        self.label2 = self.findChild(QLabel, 'label_HellAusgabe')


        self.HelligkeitDial = self.findChild(QDial, 'HelligkeitDial')                       # Es wird nach dem Helligkeitsregler (Dial) gesucht. Geänderte Wert wird an Ausgabemethode weitergeleitet
        self.HelligkeitDial.valueChanged.connect(self.setHelligkeit)

        self.setTemperatur()                                                                # Aktualisiert die Temperaturanzeige
    def btnOpenRGB_Einstellungen(self):                                                     # Öffnet RGB_Einstellungen-Fenster
        self.main_window.openRGB_Einstellungen()

    def back_button_clicked(self):
        self.main_window.openDesktopfenster()

    def setTemperatur(self):                                                                # Entnimmt den aktuellen Wert des Reglers, wandelt es in einen String um öndert den Text des QLabel
        temp_ausgabe = self.TempScrollBar.value()
        temp_ausgabe_text = str(temp_ausgabe)
        self.label.setText(f"{temp_ausgabe_text}")

    def setHelligkeit(self):                                                                # Entnimmt den aktuellen Wert des Reglers, wandelt es in einen String um öndert den Text des QLabel
        hell_ausgabe = self.HelligkeitDial.value()
        hell_ausgabe_text = str(hell_ausgabe)
        self.label2.setText(f'{hell_ausgabe_text}')




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_AllgemeineEinstellungen(None)
    window.show()
    sys.exit(app.exec_())

