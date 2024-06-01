import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QPushButton

from src.Nutzerfenster import Ui_Nutzerfenster


class Ui_QMainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_QMainWindow, self).__init__()
        uic.loadUi('Hauptfenster.ui', self)

        # Finde den Button aus der UI und verbinde ihn mit der Methode
        self.button = self.findChild(QPushButton, 'pushButton')
        self.button.clicked.connect(self.openNutzerfenster)

    def openNutzerfenster(self):
        self.window = Ui_Nutzerfenster()
        self.window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_QMainWindow()
    window.show()
    sys.exit(app.exec_())