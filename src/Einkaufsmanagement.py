# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Einkaufsmanagement.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RefillWindow(object):
    def setupUi(self, RefillWindow):
        RefillWindow.setObjectName("RefillWindow")
        RefillWindow.resize(706, 721)
        self.centralwidget = QtWidgets.QWidget(RefillWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(290, 20, 81, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.comboBox_AufAuswahl = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_AufAuswahl.setGeometry(QtCore.QRect(10, 70, 151, 22))
        self.comboBox_AufAuswahl.setObjectName("comboBox_AufAuswahl")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 121, 16))
        self.label_2.setObjectName("label_2")
        self.doubleSpinBox_AufAnzahl = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_AufAnzahl.setGeometry(QtCore.QRect(180, 70, 62, 22))
        self.doubleSpinBox_AufAnzahl.setObjectName("doubleSpinBox_AufAnzahl")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 50, 55, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_AufHinzu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_AufHinzu.setGeometry(QtCore.QRect(270, 70, 93, 41))
        self.pushButton_AufHinzu.setObjectName("pushButton_AufHinzu")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 140, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(280, 150, 91, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 180, 171, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_HinzuProduktname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_HinzuProduktname.setGeometry(QtCore.QRect(10, 200, 181, 22))
        self.lineEdit_HinzuProduktname.setObjectName("lineEdit_HinzuProduktname")
        self.pushButton_HinzuAnlegen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_HinzuAnlegen.setGeometry(QtCore.QRect(270, 220, 91, 41))
        self.pushButton_HinzuAnlegen.setObjectName("pushButton_HinzuAnlegen")
        self.listView_Inventaranzeige = QtWidgets.QListView(self.centralwidget)
        self.listView_Inventaranzeige.setGeometry(QtCore.QRect(20, 350, 331, 341))
        self.listView_Inventaranzeige.setObjectName("listView_Inventaranzeige")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 300, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(280, 310, 91, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 20, 91, 21))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 150, 51, 21))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(0, 310, 71, 21))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.radioButton_countable = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_countable.setGeometry(QtCore.QRect(10, 280, 95, 20))
        self.radioButton_countable.setChecked(True)
        self.radioButton_countable.setObjectName("radioButton_countable")
        self.radioButton_countinous = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_countinous.setGeometry(QtCore.QRect(120, 280, 95, 20))
        self.radioButton_countinous.setObjectName("radioButton_countinous")
        self.dateEdit_HinzuAblaufdatum = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_HinzuAblaufdatum.setGeometry(QtCore.QRect(10, 250, 110, 22))
        self.dateEdit_HinzuAblaufdatum.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_HinzuAblaufdatum.setObjectName("dateEdit_HinzuAblaufdatum")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 230, 171, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 171, 16))
        self.label_8.setObjectName("label_8")
        self.dateEdit_AufAblaufdatum = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_AufAblaufdatum.setGeometry(QtCore.QRect(10, 120, 110, 22))
        self.dateEdit_AufAblaufdatum.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_AufAblaufdatum.setObjectName("dateEdit_AufAblaufdatum")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(360, 30, 20, 691))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(480, 10, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(370, 20, 91, 21))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(620, 20, 81, 21))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.pushButton_EinkaufslisteAusgabe = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_EinkaufslisteAusgabe.setGeometry(QtCore.QRect(380, 60, 311, 28))
        self.pushButton_EinkaufslisteAusgabe.setObjectName("pushButton_EinkaufslisteAusgabe")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(370, 150, 101, 21))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(490, 140, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(580, 150, 131, 21))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.comboBox_IstSoll_Produktauswahl = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_IstSoll_Produktauswahl.setGeometry(QtCore.QRect(380, 200, 121, 22))
        self.comboBox_IstSoll_Produktauswahl.setObjectName("comboBox_IstSoll_Produktauswahl")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(380, 180, 131, 16))
        self.label_11.setObjectName("label_11")
        self.doubleSpinBox_IstSoll_SollFestlegen = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_IstSoll_SollFestlegen.setGeometry(QtCore.QRect(550, 200, 131, 22))
        self.doubleSpinBox_IstSoll_SollFestlegen.setObjectName("doubleSpinBox_IstSoll_SollFestlegen")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(550, 180, 111, 16))
        self.label_12.setObjectName("label_12")
        self.pushButton_IstSoll_AufSollSetzen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_IstSoll_AufSollSetzen.setGeometry(QtCore.QRect(380, 240, 311, 28))
        self.pushButton_IstSoll_AufSollSetzen.setObjectName("pushButton_IstSoll_AufSollSetzen")
        self.pushButton_IstSoll_AllesAufSoll = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_IstSoll_AllesAufSoll.setGeometry(QtCore.QRect(380, 280, 311, 28))
        self.pushButton_IstSoll_AllesAufSoll.setObjectName("pushButton_IstSoll_AllesAufSoll")
        RefillWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RefillWindow)
        self.statusbar.setObjectName("statusbar")
        RefillWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RefillWindow)
        QtCore.QMetaObject.connectSlotsByName(RefillWindow)

    def retranslateUi(self, RefillWindow):
        _translate = QtCore.QCoreApplication.translate
        RefillWindow.setWindowTitle(_translate("RefillWindow", "Einkaufsmanagement"))
        self.label.setText(_translate("RefillWindow", "Produkte auffüllen"))
        self.label_2.setText(_translate("RefillWindow", "Produkt auswählen:"))
        self.label_3.setText(_translate("RefillWindow", "Anzahl:"))
        self.pushButton_AufHinzu.setText(_translate("RefillWindow", "Hinzufügen"))
        self.label_4.setText(_translate("RefillWindow", "Produkte hinzufügen"))
        self.label_5.setText(_translate("RefillWindow", "Produktname angeben:"))
        self.pushButton_HinzuAnlegen.setText(_translate("RefillWindow", "Anlegen"))
        self.label_6.setText(_translate("RefillWindow", "Aktuelles Inventar:"))
        self.radioButton_countable.setText(_translate("RefillWindow", "Countable"))
        self.radioButton_countinous.setText(_translate("RefillWindow", "Continous"))
        self.label_7.setText(_translate("RefillWindow", "Ablaufdatum angeben:"))
        self.label_8.setText(_translate("RefillWindow", "Ablaufdatum angeben:"))
        self.label_9.setText(_translate("RefillWindow", "Einkaufsliste"))
        self.pushButton_EinkaufslisteAusgabe.setText(_translate("RefillWindow", "Als .txt ausgeben"))
        self.label_10.setText(_translate("RefillWindow", "Ist/ Soll"))
        self.label_11.setText(_translate("RefillWindow", "Produkt auswählen:"))
        self.label_12.setText(_translate("RefillWindow", "Soll festlegen:"))
        self.pushButton_IstSoll_AufSollSetzen.setText(_translate("RefillWindow", "Ausgewähltes Produkt auf Soll setzen"))
        self.pushButton_IstSoll_AllesAufSoll.setText(_translate("RefillWindow", "Alle Produkte auf Soll setzen"))
