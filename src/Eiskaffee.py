from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QListView, QPushButton,
    QSizePolicy, QWidget)
#from pyqt5.qtcore import *
#from pyqt5.qtgui import *
#from pyqt5.uic import *
import sys
import Eiskaffee_front_page_2

# Dateipfad zum konvertieren QT zu PY: C:\Users\Yasmine\AppData\Local\Programs\Python\Python311\Scripts\pyuic5 -x *NameDate.ui* - o *NeuerNameDerDatei.py*

class Eiskaffee:
    def __init__(self, milch, kaffee, eiswuerfel):
        self.milch = milch
        self.kaffee = kaffee
        self.eiswuerfel = eiswuerfel
        self.eiskaffee = Eiskaffee(0, 0, 0)

    def __str__(self):
        return f"Eiskaffee: Milch={self.milch}ml, Kaffee={self.kaffee}ml, Eiswürfel={self.eiswuerfel} Stück"

