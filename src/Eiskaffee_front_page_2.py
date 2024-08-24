from PyQt5 import QtCore, QtGui, QtWidgets
import ui_Usermanagement
import Inventory

eiswuerfel_value = 0
kaffee_value = 0
milch_value = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 437)
        MainWindow.setStyleSheet("selection-background-color: rgb(197, 141, 92);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        ui_Usermanagement.UserManagementInstanz = ui_Usermanagement.UserManagement()
        users = ui_Usermanagement.UserManagementInstanz.add_user("Yasmine", 20)
        print(ui_Usermanagement.UserManagementInstanz.get_all_users())

        self.Auswahl_Benutzername = QtWidgets.QComboBox(self.centralwidget)
        self.Auswahl_Benutzername.setGeometry(QtCore.QRect(80, 270, 131, 22))
        self.Auswahl_Benutzername.setObjectName("Auswahl_Benutzername")
        self.Auswahl_Benutzername.addItems(ui_Usermanagement.UserManagementInstanz.get_all_users().keys())


        self.Ausgabe_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Ausgabe_Button.setGeometry(QtCore.QRect(170, 320, 141, 61))
        self.Ausgabe_Button.setObjectName("Ausgabe_Button")
        self.Ausgabe_Button.setStyleSheet("background-color: rgb(252, 126, 0);")
        self.Ausgabe_Button.clicked.connect(self.showAusgabeWindow)
        self.Ausgabe_Button.clicked.connect(MainWindow.close)
        self.Ausgabe_Button.clicked.connect(lambda: ui_Usermanagement.UserManagementInstanz.withdraw(self.Auswahl_Benutzername.currentText(), 1.5, False))
        self.Ausgabe_Button.clicked.connect(lambda: print(ui_Usermanagement.UserManagementInstanz.get_all_users()))


        self.EiswuerfelSlider = QtWidgets.QSlider(self.centralwidget)
        self.EiswuerfelSlider.setGeometry(QtCore.QRect(190, 220, 160, 22))
        self.EiswuerfelSlider.setOrientation(QtCore.Qt.Horizontal)
        self.EiswuerfelSlider.setObjectName("EiswuerfelSlider")
        self.EiswuerfelSlider.setStyleSheet("QSlider::handle:horizontal { background-color: red; }")
        self.EiswuerfelSlider.setMinimum(0)
        self.EiswuerfelSlider.setMaximum(6)
        self.EiswuerfelSlider.valueChanged.connect(self.getEiskaffeeValues)


        self.KaffeeSlider = QtWidgets.QSlider(self.centralwidget)
        self.KaffeeSlider.setGeometry(QtCore.QRect(190, 180, 160, 22))
        self.KaffeeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.KaffeeSlider.setObjectName("KaffeeSlider")
        self.KaffeeSlider.setStyleSheet("QSlider::handle:horizontal { background-color: red; }")
        self.KaffeeSlider.setMinimum(0)
        self.KaffeeSlider.setMaximum(400)
        self.KaffeeSlider.valueChanged.connect(self.getEiskaffeeValues)


        self.MilchSlider = QtWidgets.QSlider(self.centralwidget)
        self.MilchSlider.setGeometry(QtCore.QRect(190, 140, 160, 22))
        self.MilchSlider.setOrientation(QtCore.Qt.Horizontal)
        self.MilchSlider.setObjectName("MilchSlider")
        self.MilchSlider.setStyleSheet("QSlider::handle:horizontal { background-color: red; }")
        self.MilchSlider.setMinimum(0)
        self.MilchSlider.setMaximum(100)
        self.MilchSlider.valueChanged.connect(self.getEiskaffeeValues)


        self.Auswahl_Benutzername = QtWidgets.QComboBox(self.centralwidget)
        self.Auswahl_Benutzername.setGeometry(QtCore.QRect(80, 270, 131, 22))
        self.Auswahl_Benutzername.setObjectName("Auswahl_Benutzername")
        self.Auswahl_Benutzername.addItems(ui_Usermanagement.UserManagementInstanz.get_all_users().keys())


        self.Zwischenuberschrift = QtWidgets.QLabel(self.centralwidget)
        self.Zwischenuberschrift.setGeometry(QtCore.QRect(80, 100, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setWeight(75)
        self.Zwischenuberschrift.setFont(font)
        self.Zwischenuberschrift.setObjectName("Zwischenuberschrift")


        self.MilchLabel = QtWidgets.QLabel(self.centralwidget)
        self.MilchLabel.setGeometry(QtCore.QRect(80, 140, 41, 31))
        self.MilchLabel.setObjectName("MilchLabel")


        self.KaffeeLabel = QtWidgets.QLabel(self.centralwidget)
        self.KaffeeLabel.setGeometry(QtCore.QRect(80, 180, 41, 31))
        self.KaffeeLabel.setObjectName("KaffeeLabel")


        self.EiswuerfelLabel = QtWidgets.QLabel(self.centralwidget)
        self.EiswuerfelLabel.setGeometry(QtCore.QRect(80, 220, 51, 31))
        self.EiswuerfelLabel.setObjectName("EiswuerfelLabel")


        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 140, 21, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 180, 21, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 220, 21, 31))
        self.label_7.setObjectName("label_7")


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



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Eiskaffee"))
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




    def getEiskaffeeValues(self):
        global eiswuerfel_value
        global kaffee_value
        global milch_value
        eiswuerfel_value = self.EiswuerfelSlider.value()
        kaffee_value = self.KaffeeSlider.value()
        milch_value = self.MilchSlider.value()
        print("Eiswürfel:", eiswuerfel_value)
        print("Kaffee:", kaffee_value)
        print("Milch:", milch_value)

    def showAusgabeWindow(self):
        self.Ausgabe_Window = QtWidgets.QMainWindow()
        ui = Ui_Ausgabe_Window()
        ui.setupUi(self.Ausgabe_Window)
        self.Ausgabe_Window.show()


class Ui_Ausgabe_Window(object):
    def setupUi(self, Ausgabe_Window):
        Ausgabe_Window.setObjectName("Ausgabe_Window")
        Ausgabe_Window.resize(618, 437)
        self.centralwidget = QtWidgets.QWidget(Ausgabe_Window)
        self.centralwidget.setObjectName("centralwidget")

        self.geniesse_title = QtWidgets.QLabel(self.centralwidget)
        self.geniesse_title.setGeometry(QtCore.QRect(80, 100, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.geniesse_title.setFont(font)
        self.geniesse_title.setObjectName("geniesse_title")

        self.Eiswuerfel_Ausgabe = QtWidgets.QLabel(self.centralwidget)
        self.Eiswuerfel_Ausgabe.setGeometry(QtCore.QRect(80, 150, 131, 31))
        self.Eiswuerfel_Ausgabe.setObjectName("Eiswuerfel_Ausgabe")

        self.Kaffee_Ausgabe = QtWidgets.QLabel(self.centralwidget)
        self.Kaffee_Ausgabe.setGeometry(QtCore.QRect(80, 180, 131, 31))
        self.Kaffee_Ausgabe.setObjectName("Kaffee_Ausgabe")

        self.Milch_Ausgabe = QtWidgets.QLabel(self.centralwidget)
        self.Milch_Ausgabe.setGeometry(QtCore.QRect(80, 210, 131, 31))
        self.Milch_Ausgabe.setObjectName("Milch_Ausgabe")

        Ausgabe_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Ausgabe_Window)
        self.statusbar.setObjectName("statusbar")
        Ausgabe_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Ausgabe_Window)
        QtCore.QMetaObject.connectSlotsByName(Ausgabe_Window)


    def retranslateUi(self, Ausgabe_Window):
        _translate = QtCore.QCoreApplication.translate
        Ausgabe_Window.setWindowTitle(_translate("Ausgabe_Window", "Eiskaffeeausgabe"))
        self.geniesse_title.setText(_translate("Ausgabe_Window", "Du kannst jetzt Deinen perfekten Eiskaffee genießen!\n"
                                                                    "Er besteht aus:"))
        self.Eiswuerfel_Ausgabe.setText(_translate("Ausgabe_Window", "Eiswürfel: " + str(eiswuerfel_value) + " Stück"))
        self.Kaffee_Ausgabe.setText(_translate("Ausgabe_Window", "Kaffee: " + str(kaffee_value) + "ml"))
        self.Milch_Ausgabe.setText(_translate("Ausgabe_Window", "Milch: " + str(milch_value) + "ml"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



