# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'if_Kalender.ui'
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
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

import if_Kalender

class Ui_Form(object):

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(668, 458)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.backButton = QPushButton(Form)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.backButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.comboBoxMonat = QComboBox(Form)
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

        self.spinBoxJahreszahl = QSpinBox(Form)
        self.spinBoxJahreszahl.setObjectName(u"spinBoxJahreszahl")
        self.spinBoxJahreszahl.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spinBoxJahreszahl.setMaximum(9998)
        self.spinBoxJahreszahl.setValue(2024)

        self.horizontalLayout.addWidget(self.spinBoxJahreszahl)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.addTerminButton = QPushButton(Form)
        self.addTerminButton.setObjectName(u"addTerminButton")
        self.addTerminButton.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.addTerminButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.LabelKW = QLabel(Form)
        self.LabelKW.setObjectName(u"LabelKW")
        self.LabelKW.setEnabled(True)
        self.LabelKW.setMinimumSize(QSize(75, 30))
        self.LabelKW.setMaximumSize(QSize(16777215, 30))
        self.LabelKW.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        self.LabelKW.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.LabelKW)

        self.labelMon = QLabel(Form)
        self.labelMon.setObjectName(u"labelMon")
        self.labelMon.setMinimumSize(QSize(75, 30))
        self.labelMon.setMaximumSize(QSize(16777215, 30))
        self.labelMon.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        self.labelMon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelMon)

        self.labelTue = QLabel(Form)
        self.labelTue.setObjectName(u"labelTue")
        self.labelTue.setMinimumSize(QSize(75, 30))
        self.labelTue.setMaximumSize(QSize(16777215, 30))
        self.labelTue.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        self.labelTue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelTue)

        self.labelWed = QLabel(Form)
        self.labelWed.setObjectName(u"labelWed")
        self.labelWed.setMinimumSize(QSize(75, 30))
        self.labelWed.setMaximumSize(QSize(16777215, 30))
        self.labelWed.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        self.labelWed.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelWed)

        self.labelThu = QLabel(Form)
        self.labelThu.setObjectName(u"labelThu")
        self.labelThu.setMinimumSize(QSize(75, 30))
        self.labelThu.setMaximumSize(QSize(16777215, 30))
        self.labelThu.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        self.labelThu.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelThu)

        self.labelFri = QLabel(Form)
        self.labelFri.setObjectName(u"labelFri")
        self.labelFri.setMinimumSize(QSize(75, 30))
        self.labelFri.setMaximumSize(QSize(16777215, 30))
        self.labelFri.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        self.labelFri.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelFri)

        self.labelSat = QLabel(Form)
        self.labelSat.setObjectName(u"labelSat")
        self.labelSat.setMinimumSize(QSize(75, 30))
        self.labelSat.setMaximumSize(QSize(16777215, 30))
        self.labelSat.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        self.labelSat.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelSat)

        self.labelSun = QLabel(Form)
        self.labelSun.setObjectName(u"labelSun")
        self.labelSun.setMinimumSize(QSize(75, 30))
        self.labelSun.setMaximumSize(QSize(16777215, 30))
        self.labelSun.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        self.labelSun.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelSun)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.LabelKW_2 = QLabel(Form)
        self.LabelKW_2.setObjectName(u"LabelKW_2")
        self.LabelKW_2.setMinimumSize(QSize(0, 50))
        self.LabelKW_2.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.LabelKW_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.LabelKW_2)

        self.labelMon_2 = QLabel(Form)
        self.labelMon_2.setObjectName(u"labelMon_2")
        self.labelMon_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelMon_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelMon_2)

        self.labelTue_2 = QLabel(Form)
        self.labelTue_2.setObjectName(u"labelTue_2")
        self.labelTue_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelTue_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelTue_2)

        self.labelWed_2 = QLabel(Form)
        self.labelWed_2.setObjectName(u"labelWed_2")
        self.labelWed_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelWed_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelWed_2)

        self.labelThu_2 = QLabel(Form)
        self.labelThu_2.setObjectName(u"labelThu_2")
        self.labelThu_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelThu_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelThu_2)

        self.labelFri_2 = QLabel(Form)
        self.labelFri_2.setObjectName(u"labelFri_2")
        self.labelFri_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelFri_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelFri_2)

        self.labelSat_2 = QLabel(Form)
        self.labelSat_2.setObjectName(u"labelSat_2")
        self.labelSat_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSat_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelSat_2)

        self.labelSun_2 = QLabel(Form)
        self.labelSun_2.setObjectName(u"labelSun_2")
        self.labelSun_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSun_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelSun_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.LabelKW_3 = QLabel(Form)
        self.LabelKW_3.setObjectName(u"LabelKW_3")
        self.LabelKW_3.setMinimumSize(QSize(0, 50))
        self.LabelKW_3.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.LabelKW_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.LabelKW_3)

        self.labelMon_3 = QLabel(Form)
        self.labelMon_3.setObjectName(u"labelMon_3")
        self.labelMon_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelMon_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelMon_3)

        self.labelTue_3 = QLabel(Form)
        self.labelTue_3.setObjectName(u"labelTue_3")
        self.labelTue_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelTue_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelTue_3)

        self.labelWed_3 = QLabel(Form)
        self.labelWed_3.setObjectName(u"labelWed_3")
        self.labelWed_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelWed_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelWed_3)

        self.labelThu_3 = QLabel(Form)
        self.labelThu_3.setObjectName(u"labelThu_3")
        self.labelThu_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelThu_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelThu_3)

        self.labelFri_3 = QLabel(Form)
        self.labelFri_3.setObjectName(u"labelFri_3")
        self.labelFri_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelFri_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelFri_3)

        self.labelSat_3 = QLabel(Form)
        self.labelSat_3.setObjectName(u"labelSat_3")
        self.labelSat_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSat_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelSat_3)

        self.labelSun_3 = QLabel(Form)
        self.labelSun_3.setObjectName(u"labelSun_3")
        self.labelSun_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSun_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelSun_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.LabelKW_4 = QLabel(Form)
        self.LabelKW_4.setObjectName(u"LabelKW_4")
        self.LabelKW_4.setMinimumSize(QSize(0, 50))
        self.LabelKW_4.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.LabelKW_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.LabelKW_4)

        self.labelMon_4 = QLabel(Form)
        self.labelMon_4.setObjectName(u"labelMon_4")
        self.labelMon_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelMon_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelMon_4)

        self.labelTue_4 = QLabel(Form)
        self.labelTue_4.setObjectName(u"labelTue_4")
        self.labelTue_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelTue_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelTue_4)

        self.labelWed_4 = QLabel(Form)
        self.labelWed_4.setObjectName(u"labelWed_4")
        self.labelWed_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelWed_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelWed_4)

        self.labelThu_4 = QLabel(Form)
        self.labelThu_4.setObjectName(u"labelThu_4")
        self.labelThu_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelThu_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelThu_4)

        self.labelFri_4 = QLabel(Form)
        self.labelFri_4.setObjectName(u"labelFri_4")
        self.labelFri_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelFri_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelFri_4)

        self.labelSat_4 = QLabel(Form)
        self.labelSat_4.setObjectName(u"labelSat_4")
        self.labelSat_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSat_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelSat_4)

        self.labelSun_4 = QLabel(Form)
        self.labelSun_4.setObjectName(u"labelSun_4")
        self.labelSun_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSun_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelSun_4)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.LabelKW_5 = QLabel(Form)
        self.LabelKW_5.setObjectName(u"LabelKW_5")
        self.LabelKW_5.setMinimumSize(QSize(0, 50))
        self.LabelKW_5.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.LabelKW_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.LabelKW_5)

        self.labelMon_5 = QLabel(Form)
        self.labelMon_5.setObjectName(u"labelMon_5")
        self.labelMon_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelMon_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelMon_5)

        self.labelTue_5 = QLabel(Form)
        self.labelTue_5.setObjectName(u"labelTue_5")
        self.labelTue_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelTue_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelTue_5)

        self.labelWed_5 = QLabel(Form)
        self.labelWed_5.setObjectName(u"labelWed_5")
        self.labelWed_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelWed_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelWed_5)

        self.labelThu_5 = QLabel(Form)
        self.labelThu_5.setObjectName(u"labelThu_5")
        self.labelThu_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelThu_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelThu_5)

        self.labelFri_5 = QLabel(Form)
        self.labelFri_5.setObjectName(u"labelFri_5")
        self.labelFri_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelFri_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelFri_5)

        self.labelSat_5 = QLabel(Form)
        self.labelSat_5.setObjectName(u"labelSat_5")
        self.labelSat_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSat_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelSat_5)

        self.labelSun_5 = QLabel(Form)
        self.labelSun_5.setObjectName(u"labelSun_5")
        self.labelSun_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSun_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelSun_5)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.LabelKW_6 = QLabel(Form)
        self.LabelKW_6.setObjectName(u"LabelKW_6")
        self.LabelKW_6.setMinimumSize(QSize(0, 50))
        self.LabelKW_6.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.LabelKW_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.LabelKW_6)

        self.labelMon_6 = QLabel(Form)
        self.labelMon_6.setObjectName(u"labelMon_6")
        self.labelMon_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelMon_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.labelMon_6)

        self.labelTue_6 = QLabel(Form)
        self.labelTue_6.setObjectName(u"labelTue_6")
        self.labelTue_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelTue_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.labelTue_6)

        self.labelWed_6 = QLabel(Form)
        self.labelWed_6.setObjectName(u"labelWed_6")
        self.labelWed_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelWed_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.labelWed_6)

        self.labelThu_6 = QLabel(Form)
        self.labelThu_6.setObjectName(u"labelThu_6")
        self.labelThu_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelThu_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.labelThu_6)

        self.labelFri_6 = QLabel(Form)
        self.labelFri_6.setObjectName(u"labelFri_6")
        self.labelFri_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelFri_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.labelFri_6)

        self.labelSat_6 = QLabel(Form)
        self.labelSat_6.setObjectName(u"labelSat_6")
        self.labelSat_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSat_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.labelSat_6)

        self.labelSun_6 = QLabel(Form)
        self.labelSun_6.setObjectName(u"labelSun_6")
        self.labelSun_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSun_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.labelSun_6)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.LabelKW_7 = QLabel(Form)
        self.LabelKW_7.setObjectName(u"LabelKW_7")
        self.LabelKW_7.setMinimumSize(QSize(0, 50))
        self.LabelKW_7.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.LabelKW_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.LabelKW_7)

        self.labelMon_7 = QLabel(Form)
        self.labelMon_7.setObjectName(u"labelMon_7")
        self.labelMon_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelMon_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.labelMon_7)

        self.labelTue_7 = QLabel(Form)
        self.labelTue_7.setObjectName(u"labelTue_7")
        self.labelTue_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelTue_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.labelTue_7)

        self.labelWed_7 = QLabel(Form)
        self.labelWed_7.setObjectName(u"labelWed_7")
        self.labelWed_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelWed_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.labelWed_7)

        self.labelThu_7 = QLabel(Form)
        self.labelThu_7.setObjectName(u"labelThu_7")
        self.labelThu_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelThu_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.labelThu_7)

        self.labelFri_7 = QLabel(Form)
        self.labelFri_7.setObjectName(u"labelFri_7")
        self.labelFri_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelFri_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.labelFri_7)

        self.labelSat_7 = QLabel(Form)
        self.labelSat_7.setObjectName(u"labelSat_7")
        self.labelSat_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSat_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.labelSat_7)

        self.labelSun_7 = QLabel(Form)
        self.labelSun_7.setObjectName(u"labelSun_7")
        self.labelSun_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelSun_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.labelSun_7)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.backButton.setToolTip(QCoreApplication.translate("Form", u"Vorheriges Fenster anzeigen", None))
        self.backButton.clicked.connect(self.backButtonClicked)
#endif // QT_CONFIG(tooltip)
        self.backButton.setText(QCoreApplication.translate("Form", u"\u2190 Zur\u00fcck", None))
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
        self.comboBoxMonat.currentIndexChanged.connect(self.monatJahrChanged)
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.spinBoxJahreszahl.setToolTip(QCoreApplication.translate("Form", u"Jahreszahl", None))
        self.spinBoxJahreszahl.valueChanged.connect(self.monatJahrChanged)
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.addTerminButton.setToolTip(QCoreApplication.translate("Form", u"Termin Hinzuf\u00fcgen", None))
        self.addTerminButton.clicked.connect(self.addTerminButtonClicked)
#endif // QT_CONFIG(tooltip)

        self.addTerminButton.setText(QCoreApplication.translate("Form", u"+ Termin", None))
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
    def addTerminButtonClicked(self):
        print("Termin Hinzufügen")

    def backButtonClicked(self):
        print("Zurück!")

    def monatJahrChanged(self):
        jahreszahl = 2024
        jahreszahl = self.spinBoxJahreszahl.value()
        monat = 1
        monat = self.comboBoxMonat.currentIndex()
        ausgewJahr = if_Kalender.jahr(jahreszahl)
        ausgewMonat = if_Kalender.getMonat(ausgewJahr, monat)
        self.LabelKW_2.setText(QCoreApplication.translate("Form", str(ausgewMonat[0][7]), None))
        self.LabelKW_3.setText(QCoreApplication.translate("Form", str(ausgewMonat[1][7]), None))
        self.LabelKW_4.setText(QCoreApplication.translate("Form", str(ausgewMonat[2][7]), None))
        self.LabelKW_5.setText(QCoreApplication.translate("Form", str(ausgewMonat[3][7]), None))
        self.LabelKW_6.setText(QCoreApplication.translate("Form", str(ausgewMonat[4][7]), None))
        self.LabelKW_7.setText(QCoreApplication.translate("Form", str(ausgewMonat[5][7]), None))
        self.labelMon_2.setText(QCoreApplication.translate("Form", str(ausgewMonat[0][0].tagNr+1), None))
        self.labelMon_3.setText(QCoreApplication.translate("Form", str(ausgewMonat[1][0].tagNr+1), None))
        self.labelMon_4.setText(QCoreApplication.translate("Form", str(ausgewMonat[2][0].tagNr+1), None))
        self.labelMon_5.setText(QCoreApplication.translate("Form", str(ausgewMonat[3][0].tagNr+1), None))
        self.labelMon_6.setText(QCoreApplication.translate("Form", str(ausgewMonat[4][0].tagNr+1), None))
        self.labelMon_7.setText(QCoreApplication.translate("Form", str(ausgewMonat[5][0].tagNr+1), None))
        self.labelTue_2.setText(QCoreApplication.translate("Form", str(ausgewMonat[0][1].tagNr+1), None))
        self.labelTue_3.setText(QCoreApplication.translate("Form", str(ausgewMonat[1][1].tagNr+1), None))
        self.labelTue_4.setText(QCoreApplication.translate("Form", str(ausgewMonat[2][1].tagNr+1), None))
        self.labelTue_5.setText(QCoreApplication.translate("Form", str(ausgewMonat[3][1].tagNr+1), None))
        self.labelTue_6.setText(QCoreApplication.translate("Form", str(ausgewMonat[4][1].tagNr+1), None))
        self.labelTue_7.setText(QCoreApplication.translate("Form", str(ausgewMonat[5][1].tagNr+1), None))
        self.labelWed_2.setText(QCoreApplication.translate("Form", str(ausgewMonat[0][2].tagNr+1), None))
        self.labelWed_3.setText(QCoreApplication.translate("Form", str(ausgewMonat[1][2].tagNr+1), None))
        self.labelWed_4.setText(QCoreApplication.translate("Form", str(ausgewMonat[2][2].tagNr+1), None))
        self.labelWed_5.setText(QCoreApplication.translate("Form", str(ausgewMonat[3][2].tagNr+1), None))
        self.labelWed_6.setText(QCoreApplication.translate("Form", str(ausgewMonat[4][2].tagNr+1), None))
        self.labelWed_7.setText(QCoreApplication.translate("Form", str(ausgewMonat[5][2].tagNr+1), None))
        self.labelThu_2.setText(QCoreApplication.translate("Form", str(ausgewMonat[0][3].tagNr+1), None))
        self.labelThu_3.setText(QCoreApplication.translate("Form", str(ausgewMonat[1][3].tagNr+1), None))
        self.labelThu_4.setText(QCoreApplication.translate("Form", str(ausgewMonat[2][3].tagNr+1), None))
        self.labelThu_5.setText(QCoreApplication.translate("Form", str(ausgewMonat[3][3].tagNr+1), None))
        self.labelThu_6.setText(QCoreApplication.translate("Form", str(ausgewMonat[4][3].tagNr+1), None))
        self.labelThu_7.setText(QCoreApplication.translate("Form", str(ausgewMonat[5][3].tagNr+1), None))
        self.labelFri_2.setText(QCoreApplication.translate("Form", str(ausgewMonat[0][4].tagNr+1), None))
        self.labelFri_3.setText(QCoreApplication.translate("Form", str(ausgewMonat[1][4].tagNr+1), None))
        self.labelFri_4.setText(QCoreApplication.translate("Form", str(ausgewMonat[2][4].tagNr+1), None))
        self.labelFri_5.setText(QCoreApplication.translate("Form", str(ausgewMonat[3][4].tagNr+1), None))
        self.labelFri_6.setText(QCoreApplication.translate("Form", str(ausgewMonat[4][4].tagNr+1), None))
        self.labelFri_7.setText(QCoreApplication.translate("Form", str(ausgewMonat[5][4].tagNr+1), None))
        self.labelSat_2.setText(QCoreApplication.translate("Form", str(ausgewMonat[0][5].tagNr+1), None))
        self.labelSat_3.setText(QCoreApplication.translate("Form", str(ausgewMonat[1][5].tagNr+1), None))
        self.labelSat_4.setText(QCoreApplication.translate("Form", str(ausgewMonat[2][5].tagNr+1), None))
        self.labelSat_5.setText(QCoreApplication.translate("Form", str(ausgewMonat[3][5].tagNr+1), None))
        self.labelSat_6.setText(QCoreApplication.translate("Form", str(ausgewMonat[4][5].tagNr+1), None))
        self.labelSat_7.setText(QCoreApplication.translate("Form", str(ausgewMonat[5][5].tagNr+1), None))
        self.labelSun_2.setText(QCoreApplication.translate("Form", str(ausgewMonat[0][6].tagNr+1), None))
        self.labelSun_3.setText(QCoreApplication.translate("Form", str(ausgewMonat[1][6].tagNr+1), None))
        self.labelSun_4.setText(QCoreApplication.translate("Form", str(ausgewMonat[2][6].tagNr+1), None))
        self.labelSun_5.setText(QCoreApplication.translate("Form", str(ausgewMonat[3][6].tagNr+1), None))
        self.labelSun_6.setText(QCoreApplication.translate("Form", str(ausgewMonat[4][6].tagNr+1), None))
        self.labelSun_7.setText(QCoreApplication.translate("Form", str(ausgewMonat[5][6].tagNr+1), None))

        #Ausgrauen und ent-Ausgrauen der Labels, je nachdem, ob der jeweilige Tag im Monat drin ist oder nicht
        #Ausgrauen für vorhergehende Tage:
        
        if ausgewMonat[0][0].imMonat != monat:
            self.labelMon_2.setStyleSheet("background-color : grey; color : grey;")
        else:
            self.labelMon_2.setStyleSheet("background-color : white; color : black")
        if ausgewMonat[0][1].imMonat != monat:
            self.labelTue_2.setStyleSheet("background-color : grey; color : grey;")
        else:
            self.labelTue_2.setStyleSheet("background-color : white; color : black")
        if ausgewMonat[0][2].imMonat != monat:
            self.labelWed_2.setStyleSheet("background-color: grey; color : grey;")
        else:
            self.labelWed_2.setStyleSheet("background-color: white; color : black")
        if ausgewMonat[0][3].imMonat != monat:
            self.labelThu_2.setStyleSheet("background-color: grey; color : grey;")
        else:
            self.labelThu_2.setStyleSheet("background-color: white; color : black")
        if ausgewMonat[0][4].imMonat != monat:
            self.labelFri_2.setStyleSheet("background-color: grey; color : grey;")
        else:
            self.labelFri_2.setStyleSheet("background-color: white; color : black")
        if ausgewMonat[0][5].imMonat != monat:
            self.labelSat_2.setStyleSheet("background-color: grey; color : grey;")
        else:
            self.labelSat_2.setStyleSheet("background-color: white; color : black")
        if ausgewMonat[0][6].imMonat != monat:
            self.labelSun_2.setStyleSheet("background-color: grey; color : grey;")
        else:
            self.labelSun_2.setStyleSheet("background-color: white; color : black")
        


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

