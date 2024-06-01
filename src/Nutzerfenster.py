import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QPushButton

from src.Desktopfenster import Ui_Desktopfenster


class Ui_Nutzerfenster(QtWidgets.QWidget):

    def __init__(self):
        super(Ui_Nutzerfenster, self).__init__()
        uic.loadUi('Nutzerfenster.ui', self)

        self.button_1 = self.findChild(QPushButton, 'pushButton_1')
        self.button_2 = self.findChild(QPushButton, 'pushButton_2')

        self.button_1.clicked.connect(self.button_1_clicked)
        self.button_2.clicked.connect(self.button_2_clicked)

    def button_1_clicked(self):
        self.window = Ui_Desktopfenster()
        self.window.show()

    def button_2_clicked(self):
        self.window = Ui_Desktopfenster()
        self.window.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Nutzerfenster()
    window.show()
    sys.exit(app.exec_())
