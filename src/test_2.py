import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication

from src.Desktopfenster import Ui_Desktopfenster

class Ui_Nutzerfenster(QWidget):

    def __init__(self, main_window):
        super(Ui_Nutzerfenster, self).__init__()
        uic.loadUi('Nutzerfenster.ui', self)

        self.main_window = main_window

        self.button_1 = self.findChild(QPushButton, 'pushButton_1')
        self.button_2 = self.findChild(QPushButton, 'pushButton_2')
        self.back_button = self.findChild(QPushButton, 'backButton')

        self.button_1.clicked.connect(self.button_1_clicked)
        self.button_2.clicked.connect(self.button_2_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)

    def button_1_clicked(self):
        self.main_window.openDesktopfenster()

    def button_2_clicked(self):
        self.main_window.openDesktopfenster()

    def back_button_clicked(self):
        self.main_window.openMainWindow()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui_Nutzerfenster(None)
    window.show()
    sys.exit(app.exec_())
