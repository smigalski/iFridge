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
        self.button_3 = self.findChild(QPushButton, 'pushButton_3')
        self.button_4 = self.findChild(QPushButton, 'pushButton_4')
        self.button_5 = self.findChild(QPushButton, 'pushButton_5')
        self.button_6 = self.findChild(QPushButton, 'pushButton_6')
        self.button_7 = self.findChild(QPushButton, 'pushButton_7')
        self.button_8 = self.findChild(QPushButton, 'pushButton_8')
        self.button_9 = self.findChild(QPushButton, 'pushButton_9')
        self.button_10 = self.findChild(QPushButton, 'pushButton_10')  # Sucht und speichert den zweiten Button
        self.back_button = self.findChild(QPushButton, 'backButton')    # Sucht und speichert den Zurück-Button

        self.button_1.clicked.connect(self.button_1_clicked)            # Verbindet den ersten Button mit der entsprechenden Klick-Methode
        self.button_2.clicked.connect(self.button_2_clicked)            # Verbindet den zweiten Button mit der entsprechenden Klick-Methode
        self.button_3.clicked.connect(self.button_3_clicked)
        self.button_4.clicked.connect(self.button_4_clicked)
        self.button_5.clicked.connect(self.button_5_clicked)
        self.button_6.clicked.connect(self.button_6_clicked)
        self.button_7.clicked.connect(self.button_7_clicked)
        self.button_8.clicked.connect(self.button_8_clicked)
        self.button_9.clicked.connect(self.button_9_clicked)
        self.button_10.clicked.connect(self.button_10_clicked)

        self.back_button.clicked.connect(self.back_button_clicked)      # Verbindet den Zurück-Button mit der entsprechenden Klick-Methode

        self.set_Text_of_buttons()                                      # Ändert den Text der Buttons zu den Namen aus der Userinformation.txt

    def set_Text_of_buttons(self):
        buttons = [self.button_1, self.button_2, self.button_3, self.button_4, self.button_5,
                   self.button_6, self.button_7, self.button_8, self.button_9, self.button_10]  # Liste der Buttons

        try:
            with open('Userinformationen.txt', 'r') as file:
                lines = file.readlines()                                # Liest alle Zeilen der Datei ein

                for i in range(10):                                     # Geht durch die ersten 10 Zeilen (falls vorhanden)
                    if i < len(lines):
                        buttons[i].setText(
                            lines[i].strip())                           # Setzt den Text des Buttons auf den Inhalt der jeweiligen Zeile
                    else:
                        buttons[i].setText(
                            f"Kein Eintrag {i + 1}")                    # Falls es nicht genug Einträge gibt, Standardtext setzen

        except FileNotFoundError:
            for button in buttons:
                button.setText(
                    "Datei nicht gefunden")                             # Falls die Datei nicht gefunden wird, Standardtext für alle Buttons setzen
        except Exception as e:
            for button in buttons:
                button.setText(f"Fehler: {e}")                          # Allgemeiner Fehlerfall, Standardtext für alle Buttons setzen

    def button_1_clicked(self):
        self.main_window.openDesktopfenster()                           # Öffnet das Desktop-Fenster, wenn der erste Button geklickt wird

    def button_2_clicked(self):
        self.main_window.openDesktopfenster()                           # Öffnet das Desktop-Fenster, wenn der zweite Button geklickt wird

    def button_3_clicked(self):
        self.main_window.openDesktopfenster()

    def button_4_clicked(self):
        self.main_window.openDesktopfenster()                           # Öffnet das Desktop-Fenster, wenn der erste Button geklickt wird

    def button_5_clicked(self):
        self.main_window.openDesktopfenster()                           # Öffnet das Desktop-Fenster, wenn der zweite Button geklickt wird

    def button_6_clicked(self):
        self.main_window.openDesktopfenster()

    def button_7_clicked(self):
        self.main_window.openDesktopfenster()  # Öffnet das Desktop-Fenster, wenn der zweite Button geklickt wird

    def button_8_clicked(self):
        self.main_window.openDesktopfenster()

    def button_9_clicked(self):
        self.main_window.openDesktopfenster()  # Öffnet das Desktop-Fenster, wenn der erste Button geklickt wird

    def button_10_clicked(self):
        self.main_window.openDesktopfenster()  # Öffnet das Desktop-Fenster, wenn der zweite Button geklickt wird

    def back_button_clicked(self):
        self.main_window.openMainWindow()                               # Öffnet das Hauptfenster, wenn der Zurück-Button geklickt wird

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui_Nutzerfenster(None)
    window.show()
    sys.exit(app.exec_())                                               # Startet die Anwendung und zeigt das Fenster an
