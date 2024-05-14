# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Usermanagement.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QListView, QPushButton,
    QSizePolicy, QWidget, QFileDialog)

class Ui_Usermanagement(object):
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
        self.label.setGeometry(QRect(20, 10, 171, 31))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label_Nutzeranzahl = QLabel(Usermanagement)
        self.label_Nutzeranzahl.setObjectName(u"label_Nutzeranzahl")
        self.label_Nutzeranzahl.setGeometry(QRect(20, 450, 161, 16))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_Nutzeranzahl.setFont(font1)
        self.pushButton_AddUser = QPushButton(Usermanagement)
        self.pushButton_AddUser.setObjectName(u"pushButton_AddUser")
        self.pushButton_AddUser.setGeometry(QRect(470, 50, 75, 23))
        self.pushButton_RemoveUser = QPushButton(Usermanagement)
        self.pushButton_RemoveUser.setObjectName(u"pushButton_RemoveUser")
        self.pushButton_RemoveUser.setGeometry(QRect(470, 90, 75, 23))
        self.line = QFrame(Usermanagement)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(205, 10, 31, 451))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
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
        self.comboBox.setEditable(False)

        self.retranslateUi(Usermanagement)

        QMetaObject.connectSlotsByName(Usermanagement)
    # setupUi

    def retranslateUi(self, Usermanagement):
        self.label.setText(QCoreApplication.translate("Usermanagement", u"Aktive User", None))
        self.label_Nutzeranzahl.setText(QCoreApplication.translate("Usermanagement", u"XX registrierte Nutzer", None))
        self.pushButton_AddUser.setText(QCoreApplication.translate("Usermanagement", u"Add User", None))
        self.pushButton_RemoveUser.setText(QCoreApplication.translate("Usermanagement", u"Remove User", None))
        self.label_3.setText(QCoreApplication.translate("Usermanagement", u"Name:", None))
        pass
    # retranslateUi
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "Usermanagement.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    sys.exit(app.exec())
