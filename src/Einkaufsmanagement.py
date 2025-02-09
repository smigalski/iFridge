# Import der benötigten Bibliotheken

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import time

# Import des Inventory.py Moduls
import Inventory



# Der gesamte Code wurde in die durch PyQt erstellte Klasse integriert (beim nächsten Mal würde ich getrennte Klassen erstellen)
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
        self.radioButton_Stackable = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_Stackable.setGeometry(QtCore.QRect(10, 280, 95, 20))
        self.radioButton_Stackable.setChecked(True)
        self.radioButton_Stackable.setObjectName("radioButton_countable")
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
        self.line_10.setGeometry(QtCore.QRect(370, 150, 290, 21))
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
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(160, 230, 55, 16))
        self.label_13.setObjectName("label_13")
        self.doubleSpinBox_HinzuAnzahl = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_HinzuAnzahl.setGeometry(QtCore.QRect(160, 250, 62, 22))
        self.doubleSpinBox_HinzuAnzahl.setObjectName("doubleSpinBox_HinzuAnzahl")
        RefillWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RefillWindow)
        self.statusbar.setObjectName("statusbar")
        RefillWindow.setStatusBar(self.statusbar)

        #Button Update nach Kauf hinzufügen
        self.pushButton_UpdateNachKauf = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_UpdateNachKauf.setGeometry(QtCore.QRect(380, 220, 316, 41))  # Rechts vom "Anlegen" Button
        self.pushButton_UpdateNachKauf.setObjectName("pushButton_UpdateNachKauf")



        # Festlegen einiger Standardwerte
        self.doubleSpinBox_HinzuAnzahl.setValue(1)
        self.doubleSpinBox_AufAnzahl.setValue(1)
        self.doubleSpinBox_HinzuAnzahl.setDisabled(True)
        self.retranslateUi(RefillWindow)
        QtCore.QMetaObject.connectSlotsByName(RefillWindow)

        # Buttons und Elemente mit den entsprechenden Funktionen verbinden (quasi wie Slots)
        self.pushButton_HinzuAnlegen.clicked.connect(self.add_product_to_inventory)
        self.pushButton_AufHinzu.clicked.connect(self.refill_product_to_inventory)
        self.radioButton_Stackable.toggled.connect(self.on_radio_button_toggled)
        self.radioButton_countinous.toggled.connect(self.on_radio_button_toggled)
        self.comboBox_AufAuswahl.currentTextChanged.connect(self.on_comboBox_changed)
        self.pushButton_EinkaufslisteAusgabe.clicked.connect(self.export_inventory)
        self.lineEdit_HinzuProduktname.returnPressed.connect(self.add_product_to_inventory)
        self.pushButton_UpdateNachKauf.clicked.connect(self.load_inventory)

    # Diese Methode sorgt dafür, dass bei Verwendung des Typs Stackable die Spinbox deaktiviert ist, da die hinzugefügte Menge immer 1 sein muss (siehe Dokumentation)
    def on_radio_button_toggled(self):
        if self.radioButton_Stackable.isChecked():
            self.doubleSpinBox_HinzuAnzahl.setValue(1)
            self.doubleSpinBox_HinzuAnzahl.setDisabled(True)
        else:
            self.doubleSpinBox_HinzuAnzahl.setDisabled(False)
            self.doubleSpinBox_HinzuAnzahl.setValue(1)  # Wert wird wieder standardmäßig auf 1 gesetzt

    # diese Methode sorgt dafür, dass die Spinbox den Wert 1 hat und nicht vom Benutzer verändert werden kann, wenn der Produkttyp stackable ist, da der Wert dafür 1 sein muss
    def on_comboBox_changed(self):
        print("Aufruf on_comboBox_changed")
        AuswahlCB = self.comboBox_AufAuswahl.currentText()
        PIndex = Inventory.getItemIndex(AuswahlCB)
        product_info = Inventory.ItemInfo(PIndex)

        print(product_info)

        if product_info[1] == "StackableItem":
            self.doubleSpinBox_AufAnzahl.setValue(1)
            self.doubleSpinBox_AufAnzahl.setEnabled(False)
        else:
            self.doubleSpinBox_AufAnzahl.setEnabled(True)

    # durch PyQt5 erstellt
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
        self.radioButton_Stackable.setText(_translate("RefillWindow", "stackable"))
        self.radioButton_countinous.setText(_translate("RefillWindow", "continous"))
        self.label_7.setText(_translate("RefillWindow", "Ablaufdatum angeben:"))
        self.label_8.setText(_translate("RefillWindow", "Ablaufdatum angeben:"))
        self.label_9.setText(_translate("RefillWindow", "Inventarliste"))
        self.pushButton_EinkaufslisteAusgabe.setText(_translate("RefillWindow", "Als .txt ausgeben"))
        self.label_13.setText(_translate("RefillWindow", "Anzahl:"))
        self.pushButton_UpdateNachKauf.setText(_translate("RefillWindow", "Update nach Kauf"))


    # diese Methode ermöglicht das Hinzufügen von Produkten zum Inventar (über das Inventory.py Modul)
    def add_product_to_inventory(self):  # Methode zum Hinzufügen von Produkten
        # Bestimme den Produkttyp basierend auf dem ausgewählten Radio-Button
        if self.radioButton_countinous.isChecked():
            product_type = "continous"
        else:
            product_type = "stackable"

        # Erhalte den Produktnamen aus der LineEdit
        product_name = self.lineEdit_HinzuProduktname.text()

        # Prüfe, ob der Produktname leer ist
        if not product_name:
            QMessageBox.warning(self, "Warnung", "Bitte geben Sie einen Produktnamen ein.")
            return

        # Erhalte die Menge aus der DoubleSpinBox
        quantity = self.doubleSpinBox_HinzuAnzahl.value()

        # Erhalte das Ablaufdatum aus der DateEdit und konvertiere es in einen Unix-Zeitstempel
        expiry_date = self.dateEdit_HinzuAblaufdatum.date().toPyDate()
        expiry_date_timestamp = int(QDateTime(expiry_date).toSecsSinceEpoch())

        # Einheit (entsprechende LineEdit fehlt aktuell noch, daher erstmal auf KG)
        if product_type == "continous":
            unit = "KG/LITER"
        else:
            unit = ""

        # Füge das neue Produkt dem Inventar hinzu
        Inventory.newItem(product_type, product_name, expiry_date_timestamp, quantity, unit, 1)

        # Leeren der LineEdit für eine bessere Übersichtlichkeit
        self.lineEdit_HinzuProduktname.clear()

        # Lade das Inventar neu
        self.load_inventory()

    # diese Methode lädt die angelegten Produkte (aus der Inventory.py Instanz in die Listview und Combobox oben)
    def load_inventory(self):
        print("Methode load_inventory wird aufgerufen")

        loadedinventory = []  # Liste erstellen
        model = QStandardItemModel() # Model für ListView festlegen

        NumberOfItems = Inventory.getNumberOfItems()

        print(NumberOfItems)
        # print(Inventory.ItemInfo(0))

        # Produkte in die loadedinventory Liste laden
        for Item in range(0, NumberOfItems):
            loadedinventory.append(Inventory.ItemInfo(Item))

        # für die ListView wird eine Formatierung benötigt. Die Produktnamen und Mengen sollen ansprechend dargestellt werden
        for item_info in loadedinventory:
            print("Schleife")
            if item_info[1] == "StackableItem":
                item_text = f"Name:  {item_info[2]} - Menge:  {item_info[3]} Stk"
                print("stackable erfogreich")
            else:
                item_text = f"Name:  {item_info[2]} - Menge:  {item_info[3]} {item_info[4]}"

            # ComboBox leeren, bevor Produkte hinzugefügt werden
            self.comboBox_AufAuswahl.clear()

            # Vorbereitung zur Darstellung im ListView
            item = QStandardItem(item_text)
            model.appendRow(item)
            for item in range(0, (NumberOfItems)):
                self.comboBox_AufAuswahl.addItem(loadedinventory[item][2])

        self.listView_Inventaranzeige.setModel(model)  # Darstellung im ListView

        # Inventar in Textdatei für Produktauswahlfenster exportieren
        self.export_inventory_forProduktauswahl()

        # Export mit der Inventory.export Funktion
        Inventory.ExportInventory()

    # diese Methode ermöglicht das Auffüllen von Produkten (d.h. Mengenänderung bestehender Produkte)
    def refill_product_to_inventory(self):
        product_name = self.comboBox_AufAuswahl.currentText()
        amount = self.doubleSpinBox_AufAnzahl.value()

        # Erhalte das Ablaufdatum aus der DateEdit und konvertiere es in einen Unix-Zeitstempel
        expiry_date = self.dateEdit_HinzuAblaufdatum.date().toPyDate()
        expiry_date_timestamp = int(QDateTime(expiry_date).toSecsSinceEpoch())

        # Ermitteln, von welchem Typ das hinzugefügte Produkt ist
        EIndex = Inventory.getItemIndex(product_name)
        EInfo = Inventory.ItemInfo(EIndex)
        ETyp = EInfo[1]
        # Umbenennen, damit die Methode die richtigen Attribute erhält
        print(f"Produkttyp: {ETyp}")
        if ETyp == "StackableItem":
            ETyp = "stackable"
        else:
            ETyp = "continous"

        print(f"ETyp umbenannt {ETyp}")
        Inventory.addItem(ETyp, product_name, expiry_date_timestamp, amount)

        self.load_inventory()

    # über diese Methode wird die Inventarliste erstellt
    def export_inventory(self):
        # Dialogfenster, damit Nutzer den Speicherort und Dateinamen auszuwählen kann
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Inventar als Textdatei speichern", "",
                                                            "Textdateien (*.txt);;Alle Dateien (*)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                # Header erzeugen
                file.write("Inventarliste\n")
                file.write(f"Erstellt am: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")  # Zeitstempel drucken

                # Inventardaten aus der Inventory.py erhalten
                NumberOfItems = Inventory.getNumberOfItems()
                inventory_dict = {}

                for Item in range(NumberOfItems):
                    item_info = Inventory.ItemInfo(Item)
                    item_type = item_info[1]  # Stackable oder Continuous
                    name = item_info[2]
                    quantity = item_info[3]
                    unit = item_info[4]

                    if item_type == "StackableItem":
                        # Menge für StackableItem über die Anzahl der Ablaufdaten
                        num_items = len(item_info[5])  # Anzahl der Ablaufdaten
                        if name in inventory_dict:
                            inventory_dict[name] += num_items
                        else:
                            inventory_dict[name] = num_items
                    elif item_type == "ContinuousItem":
                        # Menge hinzufügen
                        if name in inventory_dict:
                            inventory_dict[name] += quantity
                        else:
                            inventory_dict[name] = quantity

                # Inventar in die .TXT Datei schreiben und vorher noch die passenden Einheiten ermitteln
                for name, total_quantity in inventory_dict.items():
                    if isinstance(total_quantity, (float,)):
                        unit = "KG/Liter"  # hatte einige Probleme durch die Inventory.py und daher hier ein kleiner, schneller Work-around
                    else:
                        unit = "Stk"
                    file.write(f"{name} - Menge: {total_quantity} {unit}\n")

    # Modifizierte Exportfunktion. Es wird der Produkttyp (stackable/..), der Produktname und die Quantity für die Verwendung in der Produktauswahl exportiert
    def export_inventory_forProduktauswahl(self):
        # Kein Dialogfenster hier, sondern nur ein fester Dateiname
        fileName = "InventarFürProduktauswahl.txt"

        with open(fileName, 'w') as file:
            # Inventardaten aus der Inventory.py erhalten
            NumberOfItems = Inventory.getNumberOfItems()

            for Item in range(NumberOfItems):
                item_info = Inventory.ItemInfo(Item)
                item_type = item_info[1]  # Stackable oder Continuous
                name = item_info[2]
                quantity = item_info[3]

                # Bestimme den Produkttyp als string
                if item_type == "StackableItem":
                    product_type = "stackable"
                else:
                    product_type = "continous"

                # Schreibe die Daten im gewünschten Format in die Datei
                file.write(f"{product_type};{name};{quantity}\n")

# von PyQt5 erstellt
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    RefillWindow = QtWidgets.QMainWindow()
    ui = Ui_RefillWindow()
    ui.setupUi(RefillWindow)
    RefillWindow.show()
    sys.exit(app.exec_())