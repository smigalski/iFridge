import sys
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QPushButton

from src.Allgemeine_Einstellungen import Ui_AllgemeineEinstellungen

class Ui_Desktopfenster(QtWidgets.QWidget):                                                 # Definition einer Klasse für das Desktopfenster, die von QWidget erbt

    def __init__(self, main_window):                                                        # Konstruktor der Klasse, wird beim Erstellen eines Objekts aufgerufen
        super(Ui_Desktopfenster, self).__init__()                                           # Initialisierung der Basisklasse (QWidget)
        uic.loadUi("Desktopfenster.ui", self)                                         # Lädt das Benutzeroberflächenlayout aus der .ui-Datei und verbindet es mit diesem Objekt

        self.main_window = main_window                                                      # Referenz auf das Hauptfenster speichern, um später darauf zugreifen zu können

#------------HIER WERDEN DIE METHODEN REINGESCHRIEBEN, DIE ZU DEN FENSTERN (WIDGETS) MIT EUREN FUNKTIONEN WEITERLEITEN------------
        self.buttonAllgemeineEinstellungen = self.findChild(QPushButton, "pushButtonAllgemeineEinstellungen")
        self.buttonAllgemeineEinstellungen.clicked.connect(self.btnAllgemeineEinstellungen)

        self.buttonEiskaffee = self.findChild(QPushButton, "pushButtonEiskaffee")           # Mit der findChild-Methode kann das Objekt (pushbutton) namens pushButtonEiskaffee gefunden werden und einer Variable zugewiesen werden.
        self.buttonEiskaffee.clicked.connect(self.btnEiskaffee)

        self.buttonEinkaufen = self.findChild(QPushButton, "pushButtonEinkaufen")
        self.buttonEinkaufen.clicked.connect(self.btnEinkaufen)                             # Das Objekt wird beim Klicken mit der Methode btnEinkaufen verbunden.

        self.buttonInventory = self.findChild(QPushButton, "pushButtonInventory")
        self.buttonInventory.clicked.connect(self.btnInventory)

        self.buttonKalender = self.findChild(QPushButton, "pushButtonKalender")
        self.buttonKalender.clicked.connect(self.btnKalender)

        self.buttonNutzer = self.findChild(QPushButton, "pushButtonNutzerverw")
        self.buttonNutzer.clicked.connect(self.btnNutzerverwaltung)

        self.backbutton = self.findChild(QPushButton, 'backButton')
        self.backbutton.clicked.connect(self.back_button_clicked)

#------------HIER WERDEN DIE METHODEN REINGESCHRIEBEN, DIE DIE METHODEN IN DER KONSTRUKTORMETHODE (__init__) AUSFÜHREN------------
    def btnAllgemeineEinstellungen(self):
        self.main_window.openAllgemeineEinstellungen()

    def btnEiskaffee(self):                                                                 # Diese Methode führt einen subprocess aus, der eine Python-Datei in Python ausführt.
        subprocess.run(['python', 'Eiskaffee_front_page_2.py'])

    def btnEinkaufen(self):
        subprocess.run(['python', 'Produktauswahl.py'])

    def btnInventory(self):
        subprocess.run(['python', 'Einkaufsmanagement.py'])

    def btnKalender(self):
        subprocess.run(['python', 'if_Kalender.py'])

    def btnNutzerverwaltung(self):
        subprocess.run(['python', 'ui_Usermanagement.py'])

    def back_button_clicked(self):
        self.main_window.openNutzerfenster()                                                # Beim Klicken des Zurück-Buttons, setzen des Nutzerfenster-Widgets als MainWindow

if __name__ == "__main__":                                                                  # Überprüft, ob das Skript direkt ausgeführt wird (nicht importiert).
    app = QtWidgets.QApplication(sys.argv)                                                  # Erstellt eine Qt-Anwendung, die für alle GUI-Anwendungen erforderlich ist.
    window = Ui_Desktopfenster(None)                                                        # Erstellt ein Fensterobjekt (vermutlich die Haupt-GUI).
    window.show()                                                                           # Zeigt das Fenster an.
    sys.exit(app.exec_())                                                                   # Startet die Hauptschleife der Anwendung und sorgt für einen sauberen Programmabbruch.

