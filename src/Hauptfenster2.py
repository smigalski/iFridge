from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,)
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QLabel, QMainWindow,
    QSizePolicy, QStatusBar, QWidget)

class Ui_QMainWindow(object):
    def setupUi(self, QMainWindow):
        if not QMainWindow.objectName():
            QMainWindow.setObjectName(u"QMainWindow")
        QMainWindow.resize(800, 800)
        self.centralwidget = QWidget(QMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(0, 0, 801, 801)
        self.label_2.setPixmap(QPixmap(u"../img/Kühlschrank_Bild.jpg"))
        self.commandLinkButton = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(350, 160, 131, 81)
        self.commandLinkButton.setText(u"iFridge")
        icon = QIcon()
        icon.addFile(u"../img/iFridge_klein.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setIconSize(QSize(50, 67))
        self.commandLinkButton.setCheckable(False)
        self.commandLinkButton.setAutoDefault(False)
        QMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(QMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        QMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(QMainWindow)

        QMetaObject.connectSlotsByName(QMainWindow)

    # setupUi

    def retranslateUi(self, QMainWindow):
        QMainWindow.setWindowTitle(QCoreApplication.translate("QMainWindow", u"iFridge", None))
        self.label_2.setText("")
    # retranslateUi

class NutzerFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nutzerfenster")
        self.resize(400, 300)
        self.label = QLabel("Dies ist das Nutzerfenster", self)
        self.label.setGeometry(50, 50, 300, 30)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Lade die Hauptfenster UI
    ui_file_name = "Hauptfenster.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    main_window = loader.load(ui_file)
    ui_file.close()
    if not main_window:
        print(loader.errorString())
        sys.exit(-1)

    # Verbinde den commandLinkButton mit dem Öffnen des Nutzerfensters
    def open_nutzerfenster():
        nutzer_window = NutzerFenster()
        nutzer_window.show()

    button = main_window.findChild(QCommandLinkButton, "commandLinkButton")
    if button:
        button.clicked.connect(open_nutzerfenster)

    main_window.show()
    sys.exit(app.exec())
