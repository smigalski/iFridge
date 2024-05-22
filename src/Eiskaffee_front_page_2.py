# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Eiskaffee_front_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Ausgabe_Page import Ui_Ausgabe_Window

#Im Folgenden wird zunächst die Front-Page des Eiskaffeemenüs konfiguriert
class Ui_MainWindow(object):                        #Klasse des Fensters erstellen. Benutzeroberfläche des Hauptfensters wird konfiguriert.
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 437)                                                     #Größe des Fensters festlegen
        MainWindow.setStyleSheet("selection-background-color: rgb(197, 141, 92);")      #Hintergrundfarbe festlegen
        self.centralwidget = QtWidgets.QWidget(MainWindow)                              #Erstellung des Zentralen Widget im MainWindow
        self.centralwidget.setObjectName("centralwidget")                               #Name des Widget


#Konfigurieren des Ausgabe Buttons
        self.Ausgabe_Button = QtWidgets.QPushButton(self.centralwidget)                 #Gehört ins CentralWidget
        self.Ausgabe_Button.setGeometry(QtCore.QRect(170, 270, 141, 61))                #Größe und Geometrie des Buttons
        self.Ausgabe_Button.setObjectName("Ausgabe_Button")                             #Name des Buttons
        self.Ausgabe_Button.setStyleSheet("background-color: rgb(252, 126, 0);")        #Hintergrundfarbe des Buttons
        self.Ausgabe_Button.clicked.connect(self.showAusgabePage)

#Konfigurieren des Eiswürfelsliders
        self.EiswuerfelSlider = QtWidgets.QSlider(self.centralwidget)                   #Gehört ins CentralWidget
        self.EiswuerfelSlider.setGeometry(QtCore.QRect(190, 220, 160, 22))              #Größe und Geometrie des Sliders
        self.EiswuerfelSlider.setOrientation(QtCore.Qt.Horizontal)
        self.EiswuerfelSlider.setObjectName("EiswuerfelSlider")                         #Name des Sliders erstellen
        self.EiswuerfelSlider.setStyleSheet("QSlider::handle:horizontal { background-color: red; }")    #Hintergrundfarbe des Sliders ändern
        self.EiswuerfelSlider.setMinimum(0)
        self.EiswuerfelSlider.setMaximum(6)
        self.EiswuerfelSlider.valueChanged.connect(self.getEiskaffeeValues)             #Werte des Sliders in die Methode getEiskaffeeValues geben

# Konfigurieren des Kaffeesliders
        self.KaffeeSlider = QtWidgets.QSlider(self.centralwidget)                       #Gehört ins CentralWidget
        self.KaffeeSlider.setGeometry(QtCore.QRect(190, 180, 160, 22))                  #Größe und Geometrie des Sliders
        self.KaffeeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.KaffeeSlider.setObjectName("KaffeeSlider")                                 #Name des Sliders erstellen
        self.KaffeeSlider.setStyleSheet("QSlider::handle:horizontal { background-color: red; }")        #Hintergrundfarbe des Sliders ändern
        self.KaffeeSlider.setMinimum(0)                                                 #Minimumwert
        self.KaffeeSlider.setMaximum(400)                                               #Maximumwert
        self.KaffeeSlider.valueChanged.connect(self.getEiskaffeeValues)

# Konfigurieren des Milchsliders
        self.MilchSlider = QtWidgets.QSlider(self.centralwidget)                        #Gehört ins CentralWidget
        self.MilchSlider.setGeometry(QtCore.QRect(190, 140, 160, 22))                   #Größe und Geometrie des Sliders
        self.MilchSlider.setOrientation(QtCore.Qt.Horizontal)
        self.MilchSlider.setObjectName("MilchSlider")                                   #Name des Sliders erstellen
        self.MilchSlider.setStyleSheet("QSlider::handle:horizontal { background-color: red; }")        #Hintergrundfarbe des Sliders ändern
        self.MilchSlider.setMinimum(0)                                                  #Minimumwert
        self.MilchSlider.setMaximum(100)                                                #Maximumwert
        self.MilchSlider.valueChanged.connect(self.getEiskaffeeValues)

#Zwischenüberschrift erstellen
        self.Zwischenuberschrift = QtWidgets.QLabel(self.centralwidget)                 #Gehört ins CentralWidget
        self.Zwischenuberschrift.setGeometry(QtCore.QRect(80, 100, 461, 31))            #Größe und Geometrie der Überschrift
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")                                                #Schriftart wählen
        font.setBold(True)                                                              #fett drucken
        font.setWeight(75)                                                              #Größe
        self.Zwischenuberschrift.setFont(font)
        self.Zwischenuberschrift.setObjectName("Zwischenuberschrift")

#Milchlabel/Text erstellen und neben den MilchSlider stellen. Inhalt des Textfeldes ist noch nicht definiert.
#Erstellung, Lage und Name
        self.MilchLabel = QtWidgets.QLabel(self.centralwidget)
        self.MilchLabel.setGeometry(QtCore.QRect(80, 140, 41, 31))
        self.MilchLabel.setObjectName("MilchLabel")

#Kaffeelabel erstellen und neben den KaffeeSlider stellen. Inhalt des Textfeldes ist noch nicht definiert.
#Erstellung, Lage und Name
        self.KaffeeLabel = QtWidgets.QLabel(self.centralwidget)
        self.KaffeeLabel.setGeometry(QtCore.QRect(80, 180, 41, 31))
        self.KaffeeLabel.setObjectName("KaffeeLabel")

#Eiswürfellabel erstellen und neben den EiswürfelSlider stellen. Inhalt des Textfeldes ist noch nicht definiert.
#Erstellung, Lage und Name
        self.EiswuerfelLabel = QtWidgets.QLabel(self.centralwidget)
        self.EiswuerfelLabel.setGeometry(QtCore.QRect(80, 220, 51, 31))
        self.EiswuerfelLabel.setObjectName("EiswuerfelLabel")

#die Minimumangabe neben die Slider schreiben: min = 0
#Definition von weiteren drei Textfeldern, die links neben den Slidern stehen. Erst mal ohne Inhalt.
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 140, 21, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 180, 21, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 220, 21, 31))
        self.label_7.setObjectName("label_7")

#Erstellen von drei weiteren Textfeldern (rechts der Slider), die noch keinen Inhalt haben.
        self.sixpieces = QtWidgets.QLabel(self.centralwidget)
        self.sixpieces.setGeometry(QtCore.QRect(360, 220, 51, 31))
        self.sixpieces.setObjectName("sixpieces")
        self.hundred = QtWidgets.QLabel(self.centralwidget)
        self.hundred.setGeometry(QtCore.QRect(360, 140, 41, 31))
        self.hundred.setObjectName("hundred")
        self.fourhundred = QtWidgets.QLabel(self.centralwidget)
        self.fourhundred.setGeometry(QtCore.QRect(360, 180, 51, 31))
        self.fourhundred.setObjectName("fourhundred")


#Erstellen von Zwischen- und Überschriften für das Eiskaffeehauptmenü
        self.Uberschrift = QtWidgets.QLabel(self.centralwidget)
        self.Uberschrift.setGeometry(QtCore.QRect(80, 30, 491, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")                                #Schriftart auswählen
        font.setPointSize(12)                                           #Größe auswählen
        font.setBold(True)                                              #Fett schreiben
        font.setWeight(75)
        self.Uberschrift.setFont(font)
        self.Uberschrift.setObjectName("Uberschrift")                   #Name der Überschrift definiert

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 618, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


#Slider, Textfelder und Zwischenüberschriften bekommen ihren anzuzeigenden Inhalt.
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Ausgabe_Button.setText(_translate("MainWindow", "Eiskaffee ausgeben"))
        self.Zwischenuberschrift.setText(_translate("MainWindow", "Wähle Deine Zusammensetzung indem Du die Slider nach Deinen Wünschen \n"
                "verschiebst:"))
        self.MilchLabel.setText(_translate("MainWindow", "Milch"))
        self.KaffeeLabel.setText(_translate("MainWindow", "Kaffee"))
        self.EiswuerfelLabel.setText(_translate("MainWindow", "Eiswürfel"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "0"))
        self.sixpieces.setText(_translate("MainWindow", "6 Stück"))
        self.hundred.setText(_translate("MainWindow", "100ml"))
        self.fourhundred.setText(_translate("MainWindow", "400ml"))
        self.Uberschrift.setText(_translate("MainWindow", "Hi!\n"
            "Du bist noch einen Klick von Deiner Erfrischung entfernt!"))


#Start des Hauptprogramms

#Die Funktion getEiswürfelValues speichert die eingestellten Werte aus den Slidern in Variablen.
    def getEiskaffeeValues(self):
        eiswuerfel_value = self.EiswuerfelSlider.value()
        kaffee_value = self.KaffeeSlider.value()
        milch_value = self.MilchSlider.value()
        print("Eiswürfel:", eiswuerfel_value)
        print("Kaffee:", kaffee_value)
        print("Milch:", milch_value)

    #Die Funktion showAusgabePage ruft die AusgabePage auf und zeigt sie an.
    def showAusgabePage(self):
        self.Ausgabe_Window = QtWidgets.QMainWindow()
        ui = Ui_Ausgabe_Window()
        ui.setupUi(self.Ausgabe_Window)
        self.Ausgabe_Window.show()

#Dieser Code initialisiert die GUI-Anwendung, startet die Hauptanwendungsschleife und zeigt das Anwendungsfenster an.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



