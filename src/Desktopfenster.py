import sys
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QPushButton

from src.Allgemeine_Einstellungen import Ui_AllgemeineEinstellungen

class Ui_Desktopfenster(QtWidgets.QWidget):

    def __init__(self, main_window):
        super(Ui_Desktopfenster, self).__init__()
        uic.loadUi("Desktopfenster.ui", self)

        self.main_window = main_window

#------------HIER WERDEN DIE METHODEN REINGESCHRIEBEN, DIE ZU DEN FENSTERN (WIDGETS) MIT EUREN FUNKTIONEN WEITERLEITEN------------
        self.buttonAllgemeineEinstellungen = self.findChild(QPushButton, "pushButtonAllgemeineEinstellungen")
        self.buttonAllgemeineEinstellungen.clicked.connect(self.btnAllgemeineEinstellungen)

        self.buttonEiskaffee = self.findChild(QPushButton, "pushButtonEiskaffee")
        self.buttonEiskaffee.clicked.connect(self.btnEiskaffee)

        self.backbutton = self.findChild(QPushButton, 'backButton')
        self.backbutton.clicked.connect(self.back_button_clicked)

    #hier werden die Methoden reingeschrieben, die die Methoden in der Konstruktormethode (__init__) ausführen
    def btnAllgemeineEinstellungen(self):
        self.main_window.openAllgemeineEinstellungen()

    def btnEiskaffee(self):
        subprocess.run(['python', 'Eiskaffee_front_page_2.py'])

    def back_button_clicked(self):
        self.main_window.openNutzerfenster()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Desktopfenster(None)
    window.show()
    sys.exit(app.exec_())

