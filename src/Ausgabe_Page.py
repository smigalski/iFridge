# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ausgabe_Page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ausgabe_Window(object):
    def setupUi(self, Ausgabe_Window):
        Ausgabe_Window.setObjectName("Ausgabe_Window")
        Ausgabe_Window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Ausgabe_Window)
        self.centralwidget.setObjectName("centralwidget")

        self.geniesse_title = QtWidgets.QLabel(self.centralwidget)
        self.geniesse_title.setGeometry(QtCore.QRect(130, 120, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.geniesse_title.setFont(font)
        self.geniesse_title.setObjectName("geniesse_title")

        self.Eiswuerfel_Ausgabe = QtWidgets.QLabel(self.centralwidget)
        self.Eiswuerfel_Ausgabe.setGeometry(QtCore.QRect(140, 240, 131, 31))
        self.Eiswuerfel_Ausgabe.setObjectName("Eiswuerfel_Ausgabe")

        self.Kaffee_Ausgabe = QtWidgets.QLabel(self.centralwidget)
        self.Kaffee_Ausgabe.setGeometry(QtCore.QRect(140, 260, 131, 31))
        self.Kaffee_Ausgabe.setObjectName("Kaffee_Ausgabe")

        self.Milch_Ausgabe = QtWidgets.QLabel(self.centralwidget)
        self.Milch_Ausgabe.setGeometry(QtCore.QRect(140, 300, 131, 31))
        self.Milch_Ausgabe.setObjectName("Milch_Ausgabe")

        Ausgabe_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Ausgabe_Window)
        self.statusbar.setObjectName("statusbar")
        Ausgabe_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Ausgabe_Window)
        QtCore.QMetaObject.connectSlotsByName(Ausgabe_Window)


    def retranslateUi(self, Ausgabe_Window):
        _translate = QtCore.QCoreApplication.translate
        Ausgabe_Window.setWindowTitle(_translate("Ausgabe_Window", "Ausgabe_Window"))
        self.geniesse_title.setText(_translate("Ausgabe_Window", "Du kannst jetzt Deinen perfekten Eiskaffee genießen!\n"
                                                                    "Er besteht aus:"))
        self.Eiswuerfel_Ausgabe.setText(_translate("Ausgabe_Window", "Eiswürfel:"))
        self.Kaffee_Ausgabe.setText(_translate("Ausgabe_Window", "Kaffee:"))
        self.Milch_Ausgabe.setText(_translate("Ausgabe_Window", "Milch:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ausgabe_Window = QtWidgets.QMainWindow()
    ui = Ui_Ausgabe_Window()
    ui.setupUi(Ausgabe_Window)
    Ausgabe_Window.show()
    sys.exit(app.exec_())
