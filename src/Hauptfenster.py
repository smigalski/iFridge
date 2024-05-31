import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

from src.Nutzerfenster import Ui_Nutzerfenster


class Ui_QMainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_QMainWindow, self).__init__()
        uic.loadUi('Hauptfenster.ui', self)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("QMainWindow")
        self.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        # noinspection PyArgumentList
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openNutzerfenster())
        self.pushButton.setGeometry(QtCore.QRect(340, 60, 121, 61))
        self.pushButton.setStyleSheet("font: 700 12pt \"Terminal\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 80, 131, 31))
        self.label_3.setStyleSheet("font: 700 9pt \"Terminal\";")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 40, 801, 801))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../img/Kühlschrank_Bild.jpg.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 791, 801))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def openNutzerfenster(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Nutzerfenster()
        self.ui.setupUi(self.window)
        self.window.show()




    def retranslateUi(self, QMainWindow):
        _translate = QtCore.QCoreApplication.translate
        QMainWindow.setWindowTitle(_translate("QMainWindow", "iFridge"))
        self.pushButton.setText(_translate("QMainWindow", "iFridge"))
        self.label_3.setText(_translate("QMainWindow", "click here ------> "))
        self.label_2.setText(_translate("QMainWindow", "TextLabel"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_QMainWindow()
    window.show()
    sys.exit(app.exec_())

#if __name__ == "__main__":
    #app = QtWidgets.QApplication(sys.argv)
    #QMainWindow = QtWidgets.QMainWindow()
    #ui = Ui_QMainWindow()
    #ui.setupUi(QMainWindow)
    #QMainWindow.show()
    #sys.exit(app.exec_())
