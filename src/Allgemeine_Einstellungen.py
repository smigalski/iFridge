from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/icon_Einstellungen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 811))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../img/iFridge_klein.png"))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.horizontalScrollBar = QtWidgets.QScrollBar(Form)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(80, 110, 191, 631))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 261, 20))
        self.label_2.setStyleSheet("font: 12pt \"Terminal\";\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 760, 221, 31))
        self.label_3.setStyleSheet("font: 75 12pt \"Terminal\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(440, 220, 201, 20))
        self.label_4.setStyleSheet("font: 12pt \"Terminal\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.dial = QtWidgets.QDial(Form)
        self.dial.setGeometry(QtCore.QRect(350, 250, 371, 361))
        self.dial.setMaximum(10)
        self.dial.setObjectName("dial")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(350, 620, 221, 31))
        self.label_5.setStyleSheet("font: 75 12pt \"Terminal\";")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(610, 30, 151, 81))
        self.pushButton.setStyleSheet("font: 75 9pt \"Terminal\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../img/icon_RGB_Einstellungen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(48, 48))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Allgmeine Einstellungen"))
        self.label_2.setText(_translate("Form", "Temperatur in Celsius"))
        self.label_3.setText(_translate("Form", "Eingestellt:"))
        self.label_4.setText(_translate("Form", "Helligkeit"))
        self.label_5.setText(_translate("Form", "Eingestellt:"))
        self.pushButton.setText(_translate("Form", "RGB Einstellungen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
