# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UsermanagementTrwVQt.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl,QStringListModel, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QLinearGradient, QPainter,
<<<<<<< HEAD
<<<<<<< HEAD
    QPalette, QPixmap, QRadialGradient, QTransform, QStandardItemModel, QStandardItem)
=======
    QPalette, QPixmap, QRadialGradient, QTransform, QStandardItemModel, QStandardItem)   #QSequence
>>>>>>> main
=======
    QPalette, QPixmap, QRadialGradient, QTransform, QStandardItemModel, QStandardItem)   #QSequence
>>>>>>> main
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QListView, QPushButton, QDoubleSpinBox,
    QSizePolicy, QWidget)


class Ui_Usermanagement(object):  #GUI als Dialog mit QtDesigner hinzugefügt
    def setupUi(self, Usermanagement):
        if not Usermanagement.objectName():
            Usermanagement.setObjectName(u"Usermanagement")
        Usermanagement.resize(573, 476)
        Usermanagement.setWindowTitle(u"Nutzerverwaltung")
        self.listView = QListView(Usermanagement)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(20, 50, 191, 391))
        self.listView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.listView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.label = QLabel(Usermanagement)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 10, 171, 31))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label_Nutzeranzahl = QLabel(Usermanagement)
        self.label_Nutzeranzahl.setObjectName(u"label_Nutzeranzahl")
        self.label_Nutzeranzahl.setGeometry(QRect(20, 450, 161, 16))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_Nutzeranzahl.setFont(font1)
        self.pushButton_AddUser = QPushButton(Usermanagement)
        self.pushButton_AddUser.setObjectName(u"pushButton_AddUser")
        self.pushButton_AddUser.setGeometry(QRect(480, 60, 81, 21))
        self.pushButton_RemoveUser = QPushButton(Usermanagement)
        self.pushButton_RemoveUser.setObjectName(u"pushButton_RemoveUser")
        self.pushButton_RemoveUser.setGeometry(QRect(450, 440, 121, 31))
        font2 = QFont()
        font2.setBold(True)
        self.pushButton_RemoveUser.setFont(font2)
        self.line = QFrame(Usermanagement)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(205, 10, 31, 451))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.lineEdit = QLineEdit(Usermanagement)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(300, 60, 151, 20))
        self.label_3 = QLabel(Usermanagement)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 60, 81, 16))
        self.label_3.setFont(font1)
        self.comboBox = QComboBox(Usermanagement)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(300, 150, 191, 22))
        self.comboBox.setEditable(False)
        self.line_2 = QFrame(Usermanagement)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(220, 110, 91, 16))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.pushButton_deposit = QPushButton(Usermanagement)
        self.pushButton_deposit.setObjectName(u"pushButton_deposit")
        self.pushButton_deposit.setGeometry(QRect(430, 230, 141, 31))
        self.label_2 = QLabel(Usermanagement)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 100, 171, 31))
        self.label_2.setFont(font1)
        self.label_4 = QLabel(Usermanagement)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(340, 190, 201, 31))
        self.label_4.setFont(font1)
        self.line_3 = QFrame(Usermanagement)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(220, 200, 111, 16))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_4 = QFrame(Usermanagement)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(410, 200, 161, 16))
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.pushButton_newBalance = QPushButton(Usermanagement)
        self.pushButton_newBalance.setObjectName(u"pushButton_newBalance")
        self.pushButton_newBalance.setGeometry(QRect(430, 280, 141, 31))
        self.line_5 = QFrame(Usermanagement)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(460, 110, 111, 20))
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_5 = QLabel(Usermanagement)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 20, 201, 16))
        self.label_5.setFont(font1)
        self.line_6 = QFrame(Usermanagement)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(220, 20, 91, 16))
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_7 = QFrame(Usermanagement)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(460, 20, 111, 20))
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_6 = QLabel(Usermanagement)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(230, 150, 81, 16))
        self.label_6.setFont(font1)
        self.doubleSpinBox_amount = QDoubleSpinBox(Usermanagement)
        self.doubleSpinBox_amount.setObjectName(u"doubleSpinBox_amount")
        self.doubleSpinBox_amount.setGeometry(QRect(300, 250, 81, 31))
        self.doubleSpinBox_amount.setMinimum(0.010000000000000)
        self.doubleSpinBox_amount.setValue(5.000000000000000)
        self.label_7 = QLabel(Usermanagement)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(230, 250, 61, 31))
        self.label_7.setFont(font1)
        self.label_8 = QLabel(Usermanagement)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(480, 260, 51, 20))

        self.retranslateUi(Usermanagement)

        QMetaObject.connectSlotsByName(Usermanagement)
    # setupUi

        # Buttons mit den entsprechenden Methoden verbinden
        self.pushButton_AddUser.clicked.connect(lambda: UserManagementInstanz.add_user(self.lineEdit.text(),0,True))
        self.pushButton_RemoveUser.clicked.connect(lambda: UserManagementInstanz.remove_user(self.comboBox.currentText(),True))
        self.pushButton_deposit.clicked.connect(lambda: UserManagementInstanz.deposit(self.comboBox.currentText(),self.doubleSpinBox_amount.value(),True))
        self.pushButton_newBalance.clicked.connect(lambda: UserManagementInstanz.change_balance(self.comboBox.currentText(),self.doubleSpinBox_amount.value(),True))

    def retranslateUi(self, Usermanagement):
        self.label.setText(QCoreApplication.translate("Usermanagement", u"Nutzerliste", None))
        self.label_Nutzeranzahl.setText(QCoreApplication.translate("Usermanagement", u"0 registrierte Nutzer", None))
        self.pushButton_AddUser.setText(QCoreApplication.translate("Usermanagement", u"Hinzuf\u00fcgen", None))
        self.pushButton_RemoveUser.setText(QCoreApplication.translate("Usermanagement", u"Nutzer entfernen", None))
        self.label_3.setText(QCoreApplication.translate("Usermanagement", u"Name:", None))
        self.pushButton_deposit.setText(QCoreApplication.translate("Usermanagement", u"Einzahlen", None))
        self.label_2.setText(QCoreApplication.translate("Usermanagement", u"Nutzer ausw\u00e4hlen", None))
        self.label_4.setText(QCoreApplication.translate("Usermanagement", u"Aktionen", None))
        self.pushButton_newBalance.setText(QCoreApplication.translate("Usermanagement", u"Als Kontostand setzen", None))
        self.label_5.setText(QCoreApplication.translate("Usermanagement", u"Nutzer hinzuf\u00fcgen", None))
        self.label_6.setText(QCoreApplication.translate("Usermanagement", u"Name:", None))
        self.doubleSpinBox_amount.setSuffix(QCoreApplication.translate("Usermanagement", u" \u20ac", None))
        self.label_7.setText(QCoreApplication.translate("Usermanagement", u"Betrag:", None))
        self.label_8.setText(QCoreApplication.translate("Usermanagement", u"- oder -", None))
        pass
    # retranslateUi

    def LineEditClear(self):      #Methode zum Leeren der TextBox und der ComboBox, die in der Klasser Usermanagement aufgerufen werden kann
        self.lineEdit.clear()
        self.comboBox.clear()
    def update_ui(self):
        # Holen der Benutzerdaten aus der Usermanagement Instanz
        users = UserManagementInstanz.get_all_users()

        # ListView aktualisieren, damit die Namen neben den Kontoständen dort angezeigt werden
        model = QStandardItemModel()                                     #Auswahl der Art des Inhalts beim Listview
        for user, Kontostand in users.items():                           #das Dictionary users wird durchgegangen
            item = QStandardItem(f"{user}: {Kontostand['balance']}")     #das Item wird aus Namen und Kontostand zusammengesetzt. Dafür wird der Kontostand aus dem Dictionary aufgerufen
            model.appendRow(item)                                        #und danach an die Liste angehängt
        self.listView.setModel(model)

        # ComboBox aktualisieren
        self.comboBox.clear() #damit die UI schöner aussieht, wird die ComboBox geleert
        self.comboBox.addItems(users.keys()) #die User werden in der ComboBox aufgeführt, damit man diese dort auswählen und löschen kann

        #Label mit der Anzahl der Nutzer aktualisieren
        self.label_Nutzeranzahl.setText("Anzahl der Nutzer: " + str(len(UserManagementInstanz.get_all_users())))

class UserManagement:                   #Klasse Usermanagemengt hinzugefügt
    def __init__(self):
        self.users = {}  # Ein leeres Dictionary zur Speicherung von Benutzern

    def add_user(self, username, initial_balance=0, clicked=False):        #Methode zum Hinzufügen von Usern. Der Startwert des Kontostands ist 0
        if username not in self.users:
            self.users[username] = {"name": username, "balance": initial_balance}
            print(f"Benutzer '{username}' wurde hinzugefügt.")
            if clicked == True:
                ui.LineEditClear()
                ui.update_ui()
        else:
            print(f"Benutzer '{username}' existiert bereits.")

    def remove_user(self, username,clicked=False):                        #Methode zum Entfernen von Usern. Es fehlt noch das Melden des Auszahlbetrags
        if username in self.users:
            del self.users[username]
            if clicked == True:
                ui.update_ui()
        else:
            print("Der angegebene Nutzer existiert nicht")

    def deposit(self, username, amount,clicked=False):
        if username in self.users:
            self.users[username]['balance'] += amount
            if clicked == True:
                ui.update_ui()
        else:
            print("Der angegebene Nutzer existiert nicht")

    def change_balance(self, username, new_balance, clicked=False):
        if username in self.users:
            self.users[username]['balance'] = new_balance
            if clicked == True:
                ui.update_ui()
        else:
            print(f"Der angegebene Nutzer existiert nicht")

    def withdraw(self, username, amount, clicked=False):
        if username in self.users:
            self.users[username]['balance'] -= amount
            if clicked == True:
                ui.update_ui()
        else:
            print("Der angegebene Nutzer existiert nicht")


    def get_all_users(self):                                #Methode, die die Nutzernamen und Kontostände zurückgibt
        return self.users

UserManagementInstanz = UserManagement()            #Zur besseren Übersichtlichkeit wird die Instanz der Klasse hier explizit erzeugt




if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    dialog = QDialog()
    ui = Ui_Usermanagement()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec())

