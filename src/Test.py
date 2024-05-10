from PyQt5 import QtCore, QtGui, QtWidgets
from Eiskaffee import Eiskaffee

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 437)
        MainWindow.setStyleSheet("selection-background-color: rgb(197, 141, 92);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Erstellen der Eiskaffee-Instanz
        self.eiskaffee = Eiskaffee(0, 0, 0)

        # Konfigurieren des Ausgabe Buttons
        self.Ausgabe_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Ausgabe_Button.setGeometry(QtCore.QRect(170, 270, 141, 61))
        self.Ausgabe_Button.setObjectName("Ausgabe_Button")
        self.Ausgabe_Button.setStyleSheet("background-color: rgb(252, 126, 0);")

        # Konfigurieren des Eiswürfelsliders
        self.EiswuerfelSlider = QtWidgets.QSlider(self.centralwidget)
        self.EiswuerfelSlider.setGeometry(QtCore.QRect(190, 220, 160, 22))
        self.EiswuerfelSlider.setOrientation(QtCore.Qt.Horizontal)
        self.EiswuerfelSlider.setObjectName("EiswuerfelSlider")
        self.EiswuerfelSlider.setStyleSheet("QSlider::handle:horizontal { background-color: red; }")
        self.EiswuerfelSlider.setMinimum(0)
        self.EiswuerfelSlider.setMaximum(6)
        self.EiswuerfelSlider.valueChanged.connect(self.updateEiskaffeeValues)

        # Konfigurieren des Kaffeesliders
        self.KaffeeSlider = QtWidgets.QSlider(self.centralwidget)
        self.KaffeeSlider.setGeometry(QtCore.QRect(190, 180, 160, 22))
        self.KaffeeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.KaffeeSlider.setObjectName("KaffeeSlider")
        self.KaffeeSlider.setStyleSheet("QSlider::handle:horizontal { background-color: red; }")
        self.KaffeeSlider.setMinimum(0)
        self.KaffeeSlider.setMaximum(400)
        self.KaffeeSlider.valueChanged.connect(self.updateEiskaffeeValues)

        # Konfigurieren des Milchsliders
        self.MilchSlider = QtWidgets.QSlider(self.centralwidget)
        self.MilchSlider.setGeometry(QtCore.QRect(190, 140, 160, 22))
        self.MilchSlider.setOrientation(QtCore.Qt.Horizontal)
        self.MilchSlider.setObjectName("MilchSlider")
        self.MilchSlider.setStyleSheet("QSlider::handle:horizontal { background-color: red; }")
        self.MilchSlider.setMinimum(0)
        self.MilchSlider.setMaximum(100)
        self.MilchSlider.valueChanged.connect(self.updateEiskaffeeValues)

        # Zwischenüberschrift erstellen
        self.Zwischenuberschrift = QtWidgets.QLabel(self.centralwidget)
        self.Zwischenuberschrift.setGeometry(QtCore.QRect(80, 100, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setWeight(75)
        self.Zwischenuberschrift.setFont(font)
        self.Zwischenuberschrift.setObjectName("Zwischenuberschrift")

        # Milchlabel erstellen und neben den MilchSlider stellen
        self.MilchLabel = QtWidgets.QLabel(self.centralwidget)
        self.MilchLabel.setGeometry(QtCore.QRect(80, 140, 41, 31))
        self.MilchLabel.setObjectName("MilchLabel")

        # Kaffeelabel erstellen und neben den KaffeeSlider stellen
        self.KaffeeLabel = QtWidgets.QLabel(self.centralwidget)
        self.KaffeeLabel.setGeometry(QtCore.QRect(80, 180, 41, 31))
        self.KaffeeLabel.setObjectName("KaffeeLabel")

        # Eiswürfellabel erstellen und neben den EiswürfelSlider stellen
        self.EiswuerfelLabel = QtWidgets.QLabel(self.centralwidget)
        self.EiswuerfelLabel.setGeometry(QtCore.QRect(80, 220, 51, 31))
        self.EiswuerfelLabel.setObjectName("EiswuerfelLabel")

        # die Minimumangabe neben die Slider schreiben: min = 0
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 140, 21, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 180, 21, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 220, 21, 31))
        self.label_7.setObjectName("label_7")

        # Maxmimum der Slider neben diese schreiben
        self.sixpieces = QtWidgets.QLabel(self.centralwidget)
        self.sixpieces.setGeometry(QtCore.QRect(360, 220, 51, 31))
        self.sixpieces.setObjectName("sixpieces")
        self.hundred = QtWidgets.QLabel(self.centralwidget)
        self.hundred.setGeometry(QtCore.QRect(360, 140, 41, 31))
        self.hundred.setObjectName("hundred")
        self.fourhundred = QtWidgets.QLabel(self.centralwidget)
        self.fourhundred.setGeometry(QtCore.QRect(360, 180, 51, 31))
        self.fourhundred.setObjectName("fourhundred")

        self.Uberschrift = QtWidgets.QLabel(self.centralwidget)
        self.Uberschrift.setGeometry(QtCore.QRect(80, 30, 491, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Uberschrift.setFont(font)
        self.Uberschrift.setObjectName("Uberschrift")
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

# Inhalte der Textfelder, Buttons und Slider definieren
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


    def updateEiskaffeeValues(self):
        # Aktualisieren der Werte von Eiskaffee mit den Slider-Werten
        self.eiskaffee.eiswuerfel = self.EiswuerfelSlider.value()
        self.eiskaffee.kaffee = self.KaffeeSlider.value()
        self.eiskaffee.milch = self.MilchSlider.value()

        # Aktualisieren der Beschriftungen neben den Slidern mit den aktuellen Werten
        self.label_5.setText(str(self.MilchSlider.minimum()))
        self.label_6.setText(str(self.KaffeeSlider.minimum()))
        self.label_7.setText(str(self.EiswuerfelSlider.minimum()))
        self.hundred.setText(str(self.MilchSlider.maximum()) + "ml")
        self.fourhundred.setText(str(self.KaffeeSlider.maximum()) + "ml")
        self.sixpieces.setText(str(self.EiswuerfelSlider.maximum()) + " Stück")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

