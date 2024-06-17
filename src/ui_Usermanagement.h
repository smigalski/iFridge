/********************************************************************************
** Form generated from reading UI file 'UsermanagementvvITNo.ui'
**
** Created by: Qt User Interface Compiler version 5.11.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef USERMANAGEMENTVVITNO_H
#define USERMANAGEMENTVVITNO_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListView>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_Usermanagement
{
public:
    QListView *listView;
    QLabel *label;
    QLabel *label_Nutzeranzahl;
    QPushButton *pushButton_AddUser;
    QPushButton *pushButton_RemoveUser;
    QFrame *line;
    QLineEdit *lineEdit;
    QLabel *label_3;
    QComboBox *comboBox;
    QFrame *line_2;
    QPushButton *pushButton_deposit;
    QLabel *label_2;
    QLabel *label_4;
    QFrame *line_3;
    QFrame *line_4;
    QPushButton *pushButton_newBalance;
    QFrame *line_5;
    QLabel *label_5;
    QFrame *line_6;
    QFrame *line_7;
    QLabel *label_6;
    QDoubleSpinBox *doubleSpinBox_amount;
    QLabel *label_7;
    QLabel *label_8;

    void setupUi(QDialog *Usermanagement)
    {
        if (Usermanagement->objectName().isEmpty())
            Usermanagement->setObjectName(QStringLiteral("Usermanagement"));
        Usermanagement->resize(573, 476);
        Usermanagement->setWindowTitle(QStringLiteral("Nutzerverwaltung"));
        listView = new QListView(Usermanagement);
        listView->setObjectName(QStringLiteral("listView"));
        listView->setGeometry(QRect(20, 50, 191, 391));
        listView->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOn);
        listView->setHorizontalScrollBarPolicy(Qt::ScrollBarAsNeeded);
        label = new QLabel(Usermanagement);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(60, 10, 171, 31));
        QFont font;
        font.setPointSize(14);
        label->setFont(font);
        label_Nutzeranzahl = new QLabel(Usermanagement);
        label_Nutzeranzahl->setObjectName(QStringLiteral("label_Nutzeranzahl"));
        label_Nutzeranzahl->setGeometry(QRect(20, 450, 161, 16));
        QFont font1;
        font1.setPointSize(10);
        label_Nutzeranzahl->setFont(font1);
        pushButton_AddUser = new QPushButton(Usermanagement);
        pushButton_AddUser->setObjectName(QStringLiteral("pushButton_AddUser"));
        pushButton_AddUser->setGeometry(QRect(480, 60, 81, 21));
        pushButton_RemoveUser = new QPushButton(Usermanagement);
        pushButton_RemoveUser->setObjectName(QStringLiteral("pushButton_RemoveUser"));
        pushButton_RemoveUser->setGeometry(QRect(450, 440, 121, 31));
        QFont font2;
        font2.setBold(true);
        font2.setWeight(75);
        pushButton_RemoveUser->setFont(font2);
        line = new QFrame(Usermanagement);
        line->setObjectName(QStringLiteral("line"));
        line->setGeometry(QRect(205, 10, 31, 451));
        line->setFrameShape(QFrame::VLine);
        line->setFrameShadow(QFrame::Sunken);
        lineEdit = new QLineEdit(Usermanagement);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));
        lineEdit->setGeometry(QRect(300, 60, 151, 20));
        label_3 = new QLabel(Usermanagement);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(230, 60, 81, 16));
        label_3->setFont(font1);
        comboBox = new QComboBox(Usermanagement);
        comboBox->setObjectName(QStringLiteral("comboBox"));
        comboBox->setGeometry(QRect(300, 150, 191, 22));
        comboBox->setEditable(false);
        line_2 = new QFrame(Usermanagement);
        line_2->setObjectName(QStringLiteral("line_2"));
        line_2->setGeometry(QRect(220, 110, 91, 16));
        line_2->setFrameShape(QFrame::HLine);
        line_2->setFrameShadow(QFrame::Sunken);
        pushButton_deposit = new QPushButton(Usermanagement);
        pushButton_deposit->setObjectName(QStringLiteral("pushButton_deposit"));
        pushButton_deposit->setGeometry(QRect(430, 230, 141, 31));
        label_2 = new QLabel(Usermanagement);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(320, 100, 171, 31));
        label_2->setFont(font1);
        label_4 = new QLabel(Usermanagement);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(340, 190, 201, 31));
        label_4->setFont(font1);
        line_3 = new QFrame(Usermanagement);
        line_3->setObjectName(QStringLiteral("line_3"));
        line_3->setGeometry(QRect(220, 200, 111, 16));
        line_3->setFrameShape(QFrame::HLine);
        line_3->setFrameShadow(QFrame::Sunken);
        line_4 = new QFrame(Usermanagement);
        line_4->setObjectName(QStringLiteral("line_4"));
        line_4->setGeometry(QRect(410, 200, 161, 16));
        line_4->setFrameShape(QFrame::HLine);
        line_4->setFrameShadow(QFrame::Sunken);
        pushButton_newBalance = new QPushButton(Usermanagement);
        pushButton_newBalance->setObjectName(QStringLiteral("pushButton_newBalance"));
        pushButton_newBalance->setGeometry(QRect(430, 280, 141, 31));
        line_5 = new QFrame(Usermanagement);
        line_5->setObjectName(QStringLiteral("line_5"));
        line_5->setGeometry(QRect(460, 110, 111, 20));
        line_5->setFrameShape(QFrame::HLine);
        line_5->setFrameShadow(QFrame::Sunken);
        label_5 = new QLabel(Usermanagement);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setGeometry(QRect(320, 20, 201, 16));
        label_5->setFont(font1);
        line_6 = new QFrame(Usermanagement);
        line_6->setObjectName(QStringLiteral("line_6"));
        line_6->setGeometry(QRect(220, 20, 91, 16));
        line_6->setFrameShape(QFrame::HLine);
        line_6->setFrameShadow(QFrame::Sunken);
        line_7 = new QFrame(Usermanagement);
        line_7->setObjectName(QStringLiteral("line_7"));
        line_7->setGeometry(QRect(460, 20, 111, 20));
        line_7->setFrameShape(QFrame::HLine);
        line_7->setFrameShadow(QFrame::Sunken);
        label_6 = new QLabel(Usermanagement);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setGeometry(QRect(230, 150, 81, 16));
        label_6->setFont(font1);
        doubleSpinBox_amount = new QDoubleSpinBox(Usermanagement);
        doubleSpinBox_amount->setObjectName(QStringLiteral("doubleSpinBox_amount"));
        doubleSpinBox_amount->setGeometry(QRect(300, 250, 81, 31));
        doubleSpinBox_amount->setMinimum(0.01);
        doubleSpinBox_amount->setValue(5);
        label_7 = new QLabel(Usermanagement);
        label_7->setObjectName(QStringLiteral("label_7"));
        label_7->setGeometry(QRect(230, 250, 61, 31));
        label_7->setFont(font1);
        label_8 = new QLabel(Usermanagement);
        label_8->setObjectName(QStringLiteral("label_8"));
        label_8->setGeometry(QRect(480, 260, 51, 20));

        retranslateUi(Usermanagement);

        QMetaObject::connectSlotsByName(Usermanagement);
    } // setupUi

    void retranslateUi(QDialog *Usermanagement)
    {
        label->setText(QApplication::translate("Usermanagement", "Nutzerliste", nullptr));
        label_Nutzeranzahl->setText(QApplication::translate("Usermanagement", "XX registrierte Nutzer", nullptr));
        pushButton_AddUser->setText(QApplication::translate("Usermanagement", "Hinzuf\303\274gen", nullptr));
        pushButton_RemoveUser->setText(QApplication::translate("Usermanagement", "Nutzer entfernen", nullptr));
        label_3->setText(QApplication::translate("Usermanagement", "Name:", nullptr));
        pushButton_deposit->setText(QApplication::translate("Usermanagement", "Einzahlen", nullptr));
        label_2->setText(QApplication::translate("Usermanagement", "Nutzer ausw\303\244hlen", nullptr));
        label_4->setText(QApplication::translate("Usermanagement", "Aktionen", nullptr));
        pushButton_newBalance->setText(QApplication::translate("Usermanagement", "Als Kontostand setzen", nullptr));
        label_5->setText(QApplication::translate("Usermanagement", "Nutzer hinzuf\303\274gen", nullptr));
        label_6->setText(QApplication::translate("Usermanagement", "Name:", nullptr));
        doubleSpinBox_amount->setSuffix(QApplication::translate("Usermanagement", " \342\202\254", nullptr));
        label_7->setText(QApplication::translate("Usermanagement", "Betrag:", nullptr));
        label_8->setText(QApplication::translate("Usermanagement", "- oder -", nullptr));
        Q_UNUSED(Usermanagement);
    } // retranslateUi

};

namespace Ui {
    class Usermanagement: public Ui_Usermanagement {};
} // namespace Ui

QT_END_NAMESPACE

#endif // USERMANAGEMENTVVITNO_H
