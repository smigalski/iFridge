# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KalenderUITest.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(668, 643)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(29, 50, 611, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.comboBoxMonat = QComboBox(self.horizontalLayoutWidget)
        self.comboBoxMonat.addItem("")
        self.comboBoxMonat.addItem("")
        self.comboBoxMonat.addItem("")
        self.comboBoxMonat.addItem("")
        self.comboBoxMonat.addItem("")
        self.comboBoxMonat.addItem("")
        self.comboBoxMonat.addItem("")
        self.comboBoxMonat.addItem("")
        self.comboBoxMonat.addItem("")
        self.comboBoxMonat.addItem("")
        self.comboBoxMonat.addItem("")
        self.comboBoxMonat.addItem("")
        self.comboBoxMonat.setObjectName(u"comboBoxMonat")
        self.comboBoxMonat.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout.addWidget(self.comboBoxMonat)

        self.spinBoxJahreszahl = QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxJahreszahl.setObjectName(u"spinBoxJahreszahl")
        self.spinBoxJahreszahl.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spinBoxJahreszahl.setMaximum(9998)
        self.spinBoxJahreszahl.setValue(2024)

        self.horizontalLayout.addWidget(self.spinBoxJahreszahl)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(29, 89, 611, 521))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.LabelKW = QLabel(self.verticalLayoutWidget)
        self.LabelKW.setObjectName(u"LabelKW")
        self.LabelKW.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        self.LabelKW.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.LabelKW)

        self.labelMon = QLabel(self.verticalLayoutWidget)
        self.labelMon.setObjectName(u"labelMon")
        self.labelMon.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        self.labelMon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelMon)

        self.labelTue = QLabel(self.verticalLayoutWidget)
        self.labelTue.setObjectName(u"labelTue")
        self.labelTue.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        self.labelTue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelTue)

        self.labelWed = QLabel(self.verticalLayoutWidget)
        self.labelWed.setObjectName(u"labelWed")
        self.labelWed.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        self.labelWed.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelWed)

        self.labelThu = QLabel(self.verticalLayoutWidget)
        self.labelThu.setObjectName(u"labelThu")
        self.labelThu.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        self.labelThu.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelThu)

        self.labelFri = QLabel(self.verticalLayoutWidget)
        self.labelFri.setObjectName(u"labelFri")
        self.labelFri.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        self.labelFri.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelFri)

        self.labelSat = QLabel(self.verticalLayoutWidget)
        self.labelSat.setObjectName(u"labelSat")
        self.labelSat.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        self.labelSat.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelSat)

        self.labelSun = QLabel(self.verticalLayoutWidget)
        self.labelSun.setObjectName(u"labelSun")
        self.labelSun.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        self.labelSun.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelSun)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.LabelKW_2 = QLabel(self.verticalLayoutWidget)
        self.LabelKW_2.setObjectName(u"LabelKW_2")
        self.LabelKW_2.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.LabelKW_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.LabelKW_2)

        self.labelMon_2 = QLabel(self.verticalLayoutWidget)
        self.labelMon_2.setObjectName(u"labelMon_2")
        self.labelMon_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelMon_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelMon_2)

        self.labelTue_2 = QLabel(self.verticalLayoutWidget)
        self.labelTue_2.setObjectName(u"labelTue_2")
        self.labelTue_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelTue_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelTue_2)

        self.labelWed_2 = QLabel(self.verticalLayoutWidget)
        self.labelWed_2.setObjectName(u"labelWed_2")
        self.labelWed_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelWed_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelWed_2)

        self.labelThu_2 = QLabel(self.verticalLayoutWidget)
        self.labelThu_2.setObjectName(u"labelThu_2")
        self.labelThu_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelThu_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelThu_2)

        self.labelFri_2 = QLabel(self.verticalLayoutWidget)
        self.labelFri_2.setObjectName(u"labelFri_2")
        self.labelFri_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelFri_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelFri_2)

        self.labelSat_2 = QLabel(self.verticalLayoutWidget)
        self.labelSat_2.setObjectName(u"labelSat_2")
        self.labelSat_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSat_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelSat_2)

        self.labelSun_2 = QLabel(self.verticalLayoutWidget)
        self.labelSun_2.setObjectName(u"labelSun_2")
        self.labelSun_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSun_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelSun_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.LabelKW_3 = QLabel(self.verticalLayoutWidget)
        self.LabelKW_3.setObjectName(u"LabelKW_3")
        self.LabelKW_3.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.LabelKW_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.LabelKW_3)

        self.labelMon_3 = QLabel(self.verticalLayoutWidget)
        self.labelMon_3.setObjectName(u"labelMon_3")
        self.labelMon_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelMon_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelMon_3)

        self.labelTue_3 = QLabel(self.verticalLayoutWidget)
        self.labelTue_3.setObjectName(u"labelTue_3")
        self.labelTue_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelTue_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelTue_3)

        self.labelWed_3 = QLabel(self.verticalLayoutWidget)
        self.labelWed_3.setObjectName(u"labelWed_3")
        self.labelWed_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelWed_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelWed_3)

        self.labelThu_3 = QLabel(self.verticalLayoutWidget)
        self.labelThu_3.setObjectName(u"labelThu_3")
        self.labelThu_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelThu_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelThu_3)

        self.labelFri_3 = QLabel(self.verticalLayoutWidget)
        self.labelFri_3.setObjectName(u"labelFri_3")
        self.labelFri_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelFri_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelFri_3)

        self.labelSat_3 = QLabel(self.verticalLayoutWidget)
        self.labelSat_3.setObjectName(u"labelSat_3")
        self.labelSat_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSat_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelSat_3)

        self.labelSun_3 = QLabel(self.verticalLayoutWidget)
        self.labelSun_3.setObjectName(u"labelSun_3")
        self.labelSun_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSun_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelSun_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.LabelKW_4 = QLabel(self.verticalLayoutWidget)
        self.LabelKW_4.setObjectName(u"LabelKW_4")
        self.LabelKW_4.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.LabelKW_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.LabelKW_4)

        self.labelMon_4 = QLabel(self.verticalLayoutWidget)
        self.labelMon_4.setObjectName(u"labelMon_4")
        self.labelMon_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelMon_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelMon_4)

        self.labelTue_4 = QLabel(self.verticalLayoutWidget)
        self.labelTue_4.setObjectName(u"labelTue_4")
        self.labelTue_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelTue_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelTue_4)

        self.labelWed_4 = QLabel(self.verticalLayoutWidget)
        self.labelWed_4.setObjectName(u"labelWed_4")
        self.labelWed_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelWed_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelWed_4)

        self.labelThu_4 = QLabel(self.verticalLayoutWidget)
        self.labelThu_4.setObjectName(u"labelThu_4")
        self.labelThu_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelThu_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelThu_4)

        self.labelFri_4 = QLabel(self.verticalLayoutWidget)
        self.labelFri_4.setObjectName(u"labelFri_4")
        self.labelFri_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelFri_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelFri_4)

        self.labelSat_4 = QLabel(self.verticalLayoutWidget)
        self.labelSat_4.setObjectName(u"labelSat_4")
        self.labelSat_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSat_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelSat_4)

        self.labelSun_4 = QLabel(self.verticalLayoutWidget)
        self.labelSun_4.setObjectName(u"labelSun_4")
        self.labelSun_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSun_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelSun_4)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.LabelKW_5 = QLabel(self.verticalLayoutWidget)
        self.LabelKW_5.setObjectName(u"LabelKW_5")
        self.LabelKW_5.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.LabelKW_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.LabelKW_5)

        self.labelMon_5 = QLabel(self.verticalLayoutWidget)
        self.labelMon_5.setObjectName(u"labelMon_5")
        self.labelMon_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelMon_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelMon_5)

        self.labelTue_5 = QLabel(self.verticalLayoutWidget)
        self.labelTue_5.setObjectName(u"labelTue_5")
        self.labelTue_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelTue_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelTue_5)

        self.labelWed_5 = QLabel(self.verticalLayoutWidget)
        self.labelWed_5.setObjectName(u"labelWed_5")
        self.labelWed_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelWed_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelWed_5)

        self.labelThu_5 = QLabel(self.verticalLayoutWidget)
        self.labelThu_5.setObjectName(u"labelThu_5")
        self.labelThu_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelThu_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelThu_5)

        self.labelFri_5 = QLabel(self.verticalLayoutWidget)
        self.labelFri_5.setObjectName(u"labelFri_5")
        self.labelFri_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelFri_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelFri_5)

        self.labelSat_5 = QLabel(self.verticalLayoutWidget)
        self.labelSat_5.setObjectName(u"labelSat_5")
        self.labelSat_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSat_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelSat_5)

        self.labelSun_5 = QLabel(self.verticalLayoutWidget)
        self.labelSun_5.setObjectName(u"labelSun_5")
        self.labelSun_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSun_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelSun_5)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.LabelKW_6 = QLabel(self.verticalLayoutWidget)
        self.LabelKW_6.setObjectName(u"LabelKW_6")
        self.LabelKW_6.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.LabelKW_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.LabelKW_6)

        self.labelMon_6 = QLabel(self.verticalLayoutWidget)
        self.labelMon_6.setObjectName(u"labelMon_6")
        self.labelMon_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelMon_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.labelMon_6)

        self.labelTue_6 = QLabel(self.verticalLayoutWidget)
        self.labelTue_6.setObjectName(u"labelTue_6")
        self.labelTue_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelTue_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.labelTue_6)

        self.labelWed_6 = QLabel(self.verticalLayoutWidget)
        self.labelWed_6.setObjectName(u"labelWed_6")
        self.labelWed_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelWed_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.labelWed_6)

        self.labelThu_6 = QLabel(self.verticalLayoutWidget)
        self.labelThu_6.setObjectName(u"labelThu_6")
        self.labelThu_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelThu_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.labelThu_6)

        self.labelFri_6 = QLabel(self.verticalLayoutWidget)
        self.labelFri_6.setObjectName(u"labelFri_6")
        self.labelFri_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelFri_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.labelFri_6)

        self.labelSat_6 = QLabel(self.verticalLayoutWidget)
        self.labelSat_6.setObjectName(u"labelSat_6")
        self.labelSat_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSat_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.labelSat_6)

        self.labelSun_6 = QLabel(self.verticalLayoutWidget)
        self.labelSun_6.setObjectName(u"labelSun_6")
        self.labelSun_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSun_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.labelSun_6)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.LabelKW_7 = QLabel(self.verticalLayoutWidget)
        self.LabelKW_7.setObjectName(u"LabelKW_7")
        self.LabelKW_7.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.LabelKW_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.LabelKW_7)

        self.labelMon_7 = QLabel(self.verticalLayoutWidget)
        self.labelMon_7.setObjectName(u"labelMon_7")
        self.labelMon_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelMon_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.labelMon_7)

        self.labelTue_7 = QLabel(self.verticalLayoutWidget)
        self.labelTue_7.setObjectName(u"labelTue_7")
        self.labelTue_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelTue_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.labelTue_7)

        self.labelWed_7 = QLabel(self.verticalLayoutWidget)
        self.labelWed_7.setObjectName(u"labelWed_7")
        self.labelWed_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelWed_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.labelWed_7)

        self.labelThu_7 = QLabel(self.verticalLayoutWidget)
        self.labelThu_7.setObjectName(u"labelThu_7")
        self.labelThu_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelThu_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.labelThu_7)

        self.labelFri_7 = QLabel(self.verticalLayoutWidget)
        self.labelFri_7.setObjectName(u"labelFri_7")
        self.labelFri_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelFri_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.labelFri_7)

        self.labelSat_7 = QLabel(self.verticalLayoutWidget)
        self.labelSat_7.setObjectName(u"labelSat_7")
        self.labelSat_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSat_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.labelSat_7)

        self.labelSun_7 = QLabel(self.verticalLayoutWidget)
        self.labelSun_7.setObjectName(u"labelSun_7")
        self.labelSun_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSun_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.labelSun_7)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.comboBoxMonat.setItemText(0, QCoreApplication.translate("Form", u"Januar", None))
        self.comboBoxMonat.setItemText(1, QCoreApplication.translate("Form", u"Februar", None))
        self.comboBoxMonat.setItemText(2, QCoreApplication.translate("Form", u"M\u00e4rz", None))
        self.comboBoxMonat.setItemText(3, QCoreApplication.translate("Form", u"April", None))
        self.comboBoxMonat.setItemText(4, QCoreApplication.translate("Form", u"Mai", None))
        self.comboBoxMonat.setItemText(5, QCoreApplication.translate("Form", u"Juni", None))
        self.comboBoxMonat.setItemText(6, QCoreApplication.translate("Form", u"Juli", None))
        self.comboBoxMonat.setItemText(7, QCoreApplication.translate("Form", u"August", None))
        self.comboBoxMonat.setItemText(8, QCoreApplication.translate("Form", u"September", None))
        self.comboBoxMonat.setItemText(9, QCoreApplication.translate("Form", u"Oktober", None))
        self.comboBoxMonat.setItemText(10, QCoreApplication.translate("Form", u"November", None))
        self.comboBoxMonat.setItemText(11, QCoreApplication.translate("Form", u"Dezember", None))

#if QT_CONFIG(tooltip)
        self.comboBoxMonat.setToolTip(QCoreApplication.translate("Form", u"Monat", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.spinBoxJahreszahl.setToolTip(QCoreApplication.translate("Form", u"Jahreszahl", None))
#endif // QT_CONFIG(tooltip)
        self.LabelKW.setText(QCoreApplication.translate("Form", u"KW", None))
        self.labelMon.setText(QCoreApplication.translate("Form", u"Montag", None))
        self.labelTue.setText(QCoreApplication.translate("Form", u"Dienstag", None))
        self.labelWed.setText(QCoreApplication.translate("Form", u"Mittwoch", None))
        self.labelThu.setText(QCoreApplication.translate("Form", u"Donnerstag", None))
        self.labelFri.setText(QCoreApplication.translate("Form", u"Freitag", None))
        self.labelSat.setText(QCoreApplication.translate("Form", u"Samstag", None))
        self.labelSun.setText(QCoreApplication.translate("Form", u"Sonntag", None))
        self.LabelKW_2.setText(QCoreApplication.translate("Form", u"01", None))
        self.labelMon_2.setText(QCoreApplication.translate("Form", u"11", None))
        self.labelTue_2.setText(QCoreApplication.translate("Form", u"22", None))
        self.labelWed_2.setText(QCoreApplication.translate("Form", u"33", None))
        self.labelThu_2.setText(QCoreApplication.translate("Form", u"44", None))
        self.labelFri_2.setText(QCoreApplication.translate("Form", u"55", None))
        self.labelSat_2.setText(QCoreApplication.translate("Form", u"66", None))
        self.labelSun_2.setText(QCoreApplication.translate("Form", u"77", None))
        self.LabelKW_3.setText(QCoreApplication.translate("Form", u"02", None))
        self.labelMon_3.setText(QCoreApplication.translate("Form", u"11", None))
        self.labelTue_3.setText(QCoreApplication.translate("Form", u"22", None))
        self.labelWed_3.setText(QCoreApplication.translate("Form", u"33", None))
        self.labelThu_3.setText(QCoreApplication.translate("Form", u"44", None))
        self.labelFri_3.setText(QCoreApplication.translate("Form", u"55", None))
        self.labelSat_3.setText(QCoreApplication.translate("Form", u"66", None))
        self.labelSun_3.setText(QCoreApplication.translate("Form", u"77", None))
        self.LabelKW_4.setText(QCoreApplication.translate("Form", u"03", None))
        self.labelMon_4.setText(QCoreApplication.translate("Form", u"11", None))
        self.labelTue_4.setText(QCoreApplication.translate("Form", u"22", None))
        self.labelWed_4.setText(QCoreApplication.translate("Form", u"33", None))
        self.labelThu_4.setText(QCoreApplication.translate("Form", u"44", None))
        self.labelFri_4.setText(QCoreApplication.translate("Form", u"55", None))
        self.labelSat_4.setText(QCoreApplication.translate("Form", u"66", None))
        self.labelSun_4.setText(QCoreApplication.translate("Form", u"77", None))
        self.LabelKW_5.setText(QCoreApplication.translate("Form", u"04", None))
        self.labelMon_5.setText(QCoreApplication.translate("Form", u"11", None))
        self.labelTue_5.setText(QCoreApplication.translate("Form", u"22", None))
        self.labelWed_5.setText(QCoreApplication.translate("Form", u"33", None))
        self.labelThu_5.setText(QCoreApplication.translate("Form", u"44", None))
        self.labelFri_5.setText(QCoreApplication.translate("Form", u"55", None))
        self.labelSat_5.setText(QCoreApplication.translate("Form", u"66", None))
        self.labelSun_5.setText(QCoreApplication.translate("Form", u"77", None))
        self.LabelKW_6.setText(QCoreApplication.translate("Form", u"05", None))
        self.labelMon_6.setText(QCoreApplication.translate("Form", u"11", None))
        self.labelTue_6.setText(QCoreApplication.translate("Form", u"22", None))
        self.labelWed_6.setText(QCoreApplication.translate("Form", u"33", None))
        self.labelThu_6.setText(QCoreApplication.translate("Form", u"44", None))
        self.labelFri_6.setText(QCoreApplication.translate("Form", u"55", None))
        self.labelSat_6.setText(QCoreApplication.translate("Form", u"66", None))
        self.labelSun_6.setText(QCoreApplication.translate("Form", u"77", None))
        self.LabelKW_7.setText(QCoreApplication.translate("Form", u"06", None))
        self.labelMon_7.setText(QCoreApplication.translate("Form", u"11", None))
        self.labelTue_7.setText(QCoreApplication.translate("Form", u"22", None))
        self.labelWed_7.setText(QCoreApplication.translate("Form", u"33", None))
        self.labelThu_7.setText(QCoreApplication.translate("Form", u"44", None))
        self.labelFri_7.setText(QCoreApplication.translate("Form", u"55", None))
        self.labelSat_7.setText(QCoreApplication.translate("Form", u"66", None))
        self.labelSun_7.setText(QCoreApplication.translate("Form", u"77", None))
    # retranslateUi

class UI(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication()
    win = UI()
    win.show()
    app.exec()
