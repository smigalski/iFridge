import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QPushButton

from src.Allgemeine_Einstellungen import Ui_AllgemeineEinstellungen

class Ui_Desktopfenster(QtWidgets.QWidget):

    def __init__(self):
        super(Ui_Desktopfenster, self).__init__()
        uic.loadUi("Desktopfenster.ui", self)

        #hier werden die Methoden reingeschrieben, die zu den Fenstern mit eueren Funktionen weiterleiten
        self.buttonAllgemeineEinstellungen = self.findChild(QPushButton, "pushButtonAllgemeineEinstellungen")
        self.buttonAllgemeineEinstellungen.clicked.connect(self.openAllgemeineEinstellungen)

    #hier werden die Methoden reingeschrieben, die die Methoden in der Konstruktormethode (__init__) ausführen
    def openAllgemeineEinstellungen(self):
        self.window = Ui_AllgemeineEinstellungen()
        self.window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Desktopfenster()
    window.show()
    sys.exit(app.exec_())
