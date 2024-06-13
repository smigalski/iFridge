import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QVBoxLayout

from src.test_2 import Ui_Nutzerfenster
from src.Desktopfenster import Ui_Desktopfenster

class Ui_QMainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_QMainWindow, self).__init__()
        uic.loadUi('Hauptfenster.ui', self)

        # Finde den Button aus der UI und verbinde ihn mit der Methode
        self.button = self.findChild(QPushButton, 'pushButton')
        self.button.clicked.connect(self.openNutzerfenster)

        self.labelRGBLeiste = self.findChild(QLabel, 'labelRGBLeiste')

        # Layout für den zentralen Widget-Bereich erstellen
        self.central_layout = QVBoxLayout()
        self.central_widget = self.findChild(QWidget, 'centralwidget')
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

        self.current_widget = None

    def openNutzerfenster(self):
        self.nutzerfenster = Ui_Nutzerfenster(self)
        self._set_central_widget(self.nutzerfenster)

    def openDesktopfenster(self):
        self.desktopfenster = Ui_Desktopfenster(self)
        self._set_central_widget(self.desktopfenster)

    def openMainWindow(self):
        self._set_central_widget(None)

    def _set_central_widget(self, widget):
        if self.current_widget is not None:
            self.central_layout.removeWidget(self.current_widget)
            self.current_widget.deleteLater()
        self.current_widget = widget
        if widget is not None:
            self.central_layout.addWidget(self.current_widget)
            self.current_widget.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = Ui_QMainWindow()
    window.show()

    sys.exit(app.exec_())


