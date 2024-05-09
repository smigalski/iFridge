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
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QStandardItemModel, QStandardItem)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QListView, QPushButton,
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
        self.listView.setSelectionMode(QListView.NoSelection)
        self.label = QLabel(Usermanagement)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 171, 31))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label_2 = QLabel(Usermanagement)                   #Label2 ist das Label für die Anzahl der aktiven Nutzer
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 450, 161, 16))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.pushButton = QPushButton(Usermanagement)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(470, 50, 75, 23))
        self.pushButton_2 = QPushButton(Usermanagement)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(470, 90, 75, 23))
        self.line = QFrame(Usermanagement)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(205, 10, 31, 451))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lineEdit = QLineEdit(Usermanagement)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(300, 50, 151, 20))
        self.label_3 = QLabel(Usermanagement)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 50, 81, 16))
        font2 = QFont()
        font2.setPointSize(14)
        self.label_3.setFont(font2)
        self.comboBox = QComboBox(Usermanagement)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(300, 90, 151, 22))

        self.retranslateUi(Usermanagement)

        QMetaObject.connectSlotsByName(Usermanagement)
    # setupUi

        # Buttons mit den entsprechenden Methoden verbinden
        self.pushButton.clicked.connect(lambda: UserManagementInstanz.add_user(self.lineEdit.text()))
        self.pushButton_2.clicked.connect(lambda: UserManagementInstanz.remove_user(self.comboBox.currentText()))

    def retranslateUi(self, Usermanagement):
        self.label.setText(QCoreApplication.translate("Usermanagement", u"Kontostände", None))
        self.label_2.setText(QCoreApplication.translate("Usermanagement", u"Anzahl der Nutzer: 0", None))
        self.pushButton.setText(QCoreApplication.translate("Usermanagement", u"Add User", None))
        self.pushButton_2.setText(QCoreApplication.translate("Usermanagement", u"Remove User", None))
        self.label_3.setText(QCoreApplication.translate("Usermanagement", u"Name:", None))
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
        self.label_2.setText("Anzahl der Nutzer: " + str(len(UserManagementInstanz.get_all_users())))

class UserManagement:                   #Klasse Usermanagemengt hinzugefügt
    def __init__(self):
        self.users = {}  # Ein leeres Dictionary zur Speicherung von Benutzern

    def add_user(self, username, initial_balance=0):        #Methode zum Hinzufügen von Usern. Der Startwert des Kontostands ist 0
        if username not in self.users:
            self.users[username] = {"name": username, "balance": initial_balance}
            print(f"Benutzer '{username}' wurde hinzugefügt.")
            ui.LineEditClear()
            ui.update_ui()
        else:
            print(f"Benutzer '{username}' existiert bereits.")

    def remove_user(self, username):                        #Methode zum Entfernen von Usern. Es fehlt noch das Melden des Auszahlbetrags
        if username in self.users:
            del self.users[username]
            print(f"Benutzer '{username}' wurde entfernt.")
            ui.update_ui()
        else:
            print(f"Benutzer '{username}' existiert nicht.")


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

