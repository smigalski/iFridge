import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QVBoxLayout


class Ui_QMainWindow(QtWidgets.QMainWindow):                                    # Definiert eine Klasse, die das Hauptfenster der Anwendung repräsentiert

    def __init__(self):                                                         # Konstruktor der Klasse; initialisiert das Hauptfenster
        super(Ui_QMainWindow, self).__init__()
        uic.loadUi('Hauptfenster.ui', self)                                # Lädt die UI-Datei 'Hauptfenster.ui' und wendet sie auf das aktuelle Fenster an


        self.button = self.findChild(QPushButton, 'pushButton')                 # Findet den Button aus der UI und verbindet es mit der Methode openNutzerfenster
        self.button.clicked.connect(self.openNutzerfenster)

        self.labelRGBLeiste = self.findChild(QLabel, 'labelRGBLeiste')          # Findet das Label in der UI


        self.central_layout = QVBoxLayout()                                     # Erstellt ein Layout für den zentralen Bereich des Fensters
        self.central_widget = self.findChild(QWidget, 'centralwidget')
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

        self.current_widget = None                                              # Variable zur Speicherung des aktuell angezeigten Widgets

    def openNutzerfenster(self):                                                # Methode zum Öffnen des Nutzerfensters
        from src.Nutzerfenster import Ui_Nutzerfenster                          # Importiert das Nutzerfenster-Modul (später, um zirkuläre Importe zu vermeiden)
        self.nutzerfenster = Ui_Nutzerfenster(self)
        self._set_central_widget(self.nutzerfenster)

    def openDesktopfenster(self):                                               # Methode zum Öffnen des Desktopfensters
        from src.Desktopfenster import Ui_Desktopfenster
        self.desktopfenster = Ui_Desktopfenster(self)
        self._set_central_widget(self.desktopfenster)

    def openAllgemeineEinstellungen(self):                                      # Methode zum Öffnen der allgemeinen Einstellungen
        from src.Allgemeine_Einstellungen import Ui_AllgemeineEinstellungen
        self.allgemeine_einstellungen = Ui_AllgemeineEinstellungen(self)
        self._set_central_widget(self.allgemeine_einstellungen)

    def openRGB_Einstellungen(self):                                            # Methode zum Öffnen der RGB-Einstellungen
        from src.RGB_Einstellungen import RGBSlider
        self.rgb_einstellungen = RGBSlider(self)
        self._set_central_widget(self.rgb_einstellungen)

    def openMainWindow(self):
        self._set_central_widget(None)                                          # Methode zum Zurücksetzen auf das Hauptfenster (kein zentrales Widget)


    def _set_central_widget(self, widget):                                      # Private Methode zum Wechseln des zentralen Widgets
        if self.current_widget is not None:                                     # Entfernt das aktuelle Widget, falls vorhanden
            self.central_layout.removeWidget(self.current_widget)
            self.current_widget.deleteLater()
        self.current_widget = widget                                            # Setzt das neue Widget als zentrales Widget
        if widget is not None:
            self.central_layout.addWidget(self.current_widget)
            self.current_widget.show()

if __name__ == "__main__":                                                      # Startpunkt der Anwendung
    app = QtWidgets.QApplication(sys.argv)                                      # Erstellt die Anwendung

    window = Ui_QMainWindow()                                                   # Erstellt eine Instanz des Hauptfensters
    window.show()                                                               # Zeigt das Hauptfenster

    sys.exit(app.exec_())                                                       # Startet die Ereignisschleife der Anwendung