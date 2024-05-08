# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Hauptfenster.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_QMainWindow(object):
    def setupUi(self, QMainWindow):
        if not QMainWindow.objectName():
            QMainWindow.setObjectName(u"QMainWindow")
        QMainWindow.resize(800, 800)
        self.centralwidget = QWidget(QMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 680, 121, 51))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(160, 680, 121, 51))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(590, 670, 161, 51))
        QMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(QMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuHauptfenster = QMenu(self.menubar)
        self.menuHauptfenster.setObjectName(u"menuHauptfenster")
        QMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(QMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        QMainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHauptfenster.menuAction())

        self.retranslateUi(QMainWindow)

        QMetaObject.connectSlotsByName(QMainWindow)
    # setupUi

    def retranslateUi(self, QMainWindow):
        QMainWindow.setWindowTitle(QCoreApplication.translate("QMainWindow", u"iFridge", None))
        self.pushButton.setText(QCoreApplication.translate("QMainWindow", u"Einstellungen", None))
        self.pushButton_2.setText(QCoreApplication.translate("QMainWindow", u"Nutzer", None))
        self.pushButton_3.setText(QCoreApplication.translate("QMainWindow", u"Einkaufliste", None))
        self.menuHauptfenster.setTitle(QCoreApplication.translate("QMainWindow", u"Hauptfenster", None))
    # retranslateUi

class UI(QMainWindow):
        def __init__(self):
            super().__init__()
            self.ui = Ui_QMainWindow()
            self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication()
    win = UI()
    win.show()
    app.exec()