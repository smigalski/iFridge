import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication

class Ui_Nutzerfenster(QWidget):

    def __init__(self, main_window):
        super(Ui_Nutzerfenster, self).__init__()
        uic.loadUi('Nutzerfenster.ui', self)                       # Lädt die Benutzeroberfläche aus der .ui-Datei

        self.main_window = main_window

        self.button_1 = self.findChild(QPushButton, 'pushButton_1')     # Sucht und speichert den ersten Button
        self.button_2 = self.findChild(QPushButton, 'pushButton_2')     # Sucht und speichert den zweiten Button
        self.back_button = self.findChild(QPushButton, 'backButton')    # Sucht und speichert den Zurück-Button

        self.button_1.clicked.connect(self.button_1_clicked)            # Verbindet den ersten Button mit der entsprechenden Klick-Methode
        self.button_2.clicked.connect(self.button_2_clicked)            # Verbindet den zweiten Button mit der entsprechenden Klick-Methode
        self.back_button.clicked.connect(self.back_button_clicked)      # Verbindet den Zurück-Button mit der entsprechenden Klick-Methode

    def button_1_clicked(self):
        self.main_window.openDesktopfenster()                           # Öffnet das Desktop-Fenster, wenn der erste Button geklickt wird

    def button_2_clicked(self):
        self.main_window.openDesktopfenster()                           # Öffnet das Desktop-Fenster, wenn der zweite Button geklickt wird

    def back_button_clicked(self):
        self.main_window.openMainWindow()                               # Öffnet das Hauptfenster, wenn der Zurück-Button geklickt wird

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui_Nutzerfenster(None)
    window.show()
    sys.exit(app.exec_())                                               # Startet die Anwendung und zeigt das Fenster an
