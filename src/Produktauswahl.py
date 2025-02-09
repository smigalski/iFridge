# Importieren der PyQt5 Bibliotheken
from PyQt5 import QtCore, QtGui, QtWidgets

import os
import Inventory

# Initialiseren des Dictionaries für die Nutzer
users = {}

# Von PyQt5 erstellte Klasse. Wurde um ein paar Methoden ergänzt
class Ui_Produktauswahl(object):

    # durch Qt5 erstellt
    def setupUi(self, Produktauswahl):
        Produktauswahl.setObjectName("Produktauswahl")
        Produktauswahl.resize(811, 515)
        Produktauswahl.setWindowTitle("Produktauswahl")
        self.centralwidget = QtWidgets.QWidget(Produktauswahl)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(20, 50, 371, 391))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 460, 381, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(410, 10, 20, 521))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(600, 170, 181, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 170, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 250, 361, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(QtGui.QFont.Weight.Normal)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(600, 220, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        Produktauswahl.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Produktauswahl)
        self.statusbar.setObjectName("statusbar")
        Produktauswahl.setStatusBar(self.statusbar)

        # Neuer Button "Update Userinformationen"
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_update.setGeometry(QtCore.QRect(600, 130, 181, 31))
        self.pushButton_update.setObjectName("pushButton_update")

        # update Button verbinden mit der Combobox Update Methode
        self.pushButton_update.clicked.connect(self.update_comboBox)

        # Wenn etwas anderes in der Combobox ausgewählt wird, wird der jeweilige Kontostand angezeigt
        self.comboBox.currentIndexChanged.connect(self.update_balance)

        # Neuer Button "Inventar laden"
        self.pushButton_updateInventory = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_updateInventory.setGeometry(QtCore.QRect(600, 85, 181, 31))
        self.pushButton_updateInventory.setObjectName("pushButton_updateInventory")
        self.pushButton_updateInventory.setText("Update Inventar")

        # Button mit der Methode zum Laden des Inventars verbinden
        self.pushButton_updateInventory.clicked.connect(self.load_inventory_into_listview)

        # Button zum Kaufen verbinden
        self.pushButton.clicked.connect(self.buy_product)


        self.retranslateUi(Produktauswahl)
        QtCore.QMetaObject.connectSlotsByName(Produktauswahl)

    # Methode zum Updaten der ComboBox mit den Userinformationen aus dem User Dictionary
    def update_comboBox(self):
        self.comboBox.clear()  # Erst die Combobox leeren, sonst doppelte Einträge
        self.comboBox.addItems(users.keys())  # Hinzufügen aller Usernamen
        self.update_balance()


    # Methode zum Laden des Guthabens des ausgewählten Nutzers in das Label Guthaben
    def update_balance(self):
        if self.comboBox.currentText() != "":
            self.label_4.setText(f"Guthaben: {users[self.comboBox.currentText()]} €")

    def retranslateUi(self, Produktauswahl):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Produktauswahl", "Verfügbare Produkte:"))
        self.label_2.setText(_translate("Produktauswahl", "Aktion: Jedes Produkt kostet aktuell 2,50€!"))
        self.label_3.setText(_translate("Produktauswahl", "Mitarbeiter:"))
        self.pushButton.setText(_translate("Produktauswahl", "Eine Einheit des ausgewählten Produktes kaufen!"))
        self.label_4.setText(_translate("Produktauswahl", "Guthaben:"))
        self.pushButton_update.setText(_translate("Produktauswahl", "Update Userinfos"))

    #Methode zum UI Aktualisieren
    def update_ui(self):
        self.comboBox.addItems(users.keys())  # die User werden in der ComboBox aufgeführt, damit man diese dort auswählen

    # Methode zur Darstellung des Inventars in der ListView mit Name und Menge
    def load_inventory_into_listview(self):
        # StandardItemModel festlegen
        model = QtGui.QStandardItemModel()

        # Dateiname festlegen
        file_path = "Inventory.txt"
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    line_data = line.strip().split(';')
                    if len(line_data) >= 3:  # Überprüfen, ob mindestens 3 Einträge vorhanden sind
                        product_type, product_name, quantity = line_data[:3]  # Die ersten drei Einträge extrahieren
                        # Formatieren des Textes für die ListView
                        item_text = f"Name: {product_name} - Menge: {quantity}"
                        item = QtGui.QStandardItem(item_text)
                        model.appendRow(item)

            # Listviewmodel festlegen
            self.listView.setModel(model)

        except FileNotFoundError:
            print(f"Datei wurde noch nicht erstellt. Einkaufsmanagement öffnen.")
        except Exception as e:
            print(f"Fehler beim Laden der Datei: {e}")

    # Funktion zum Kauf von einem Produkt
    def buy_product(self):



        #debug
        print("Userdict vor Kauf: ", users)

        # Aktuellen Usernamen aus ComboBox holen
        selected_user = self.comboBox.currentText()

        # Prüfen, ob überhaupt einer ausgewählt wurde
        if selected_user == "":
            print("Kein Benutzer ausgewählt.")
            return

        # Der User muss mindestens 2,50 auf seinem Konto haben, um etwas zu kaufen
        current_balance = users.get(selected_user, 0)
        if current_balance < 2.50:
            print("Geld einzahlen! Der Kontostand reicht nicht aus!")
            return

        # Prüfen, welches Produkt in der ListView ausgewählt wurde
        selected_indexes = self.listView.selectedIndexes()

        # Prüfen, ob überhaupt ein Produkt ausgewählt wurde
        if not selected_indexes:
            print("Zum Kaufen muss ein Produkt ausgewählt werden!")
            return

        # Name und Menge des Produktes erhalten
        selected_item = selected_indexes[0]
        product_data = selected_item.data()
        product_name = product_data.split(" - ")[0].replace("Name: ", "")
        quantity = int(product_data.split(" - ")[1].replace("Menge: ", ""))

        # Wenn die Menge des Produkts kleiner als 1 ist, abbrechen
        if quantity < 1:
            print("Produktmenge reicht nicht aus!")
            return

        # jetzt 2,50€ vom Kontostand abziehen
        users[selected_user] -= 2.50
        print("Userinformationen nach Abzug der 2,50", users)

        # Aktualisiere den Kontostand in der UI und speichere die Änderungen in der Datei
        self.update_balance()
        print("Userinformationen nach update_balance ", users)
        save_users_to_file()
        print("Userinformationen nach save_users_to_file ", users)

        # Reduziere die Menge des Produkts um 1 und aktualisiere die Inventardatei
        new_quantity = quantity - 1
        self.update_inventory_file(product_name, new_quantity)

        # Lade das Inventar neu, um die aktualisierten Daten anzuzeigen
        self.load_inventory_into_listview()

    # Methode zum Aktualisieren des Inventars in der Textdatei
    def update_inventory_file(self, product_name, new_quantity):
        file_path = "Inventory.txt"
        inventory_lines = []

        # Lese die Inventardatei Zeile für Zeile und aktualisiere die Menge des ausgewählten Produkts
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    # Splitte die Zeile in ihre Bestandteile
                    line_data = line.strip().split(';')
                    if len(line_data) >= 3:  # Sicherstellen, dass die Zeile mindestens 3 Einträge hat
                        product_type, name, quantity = line_data[:3]  # Extrahiere die ersten drei Einträge

                        # Wenn das Produkt gefunden wurde, aktualisiere die Menge
                        if name == product_name:
                            line_data[2] = str(new_quantity)  # Setze die neue Menge

                        # Füge die Zeile (mit den unveränderten restlichen Einträgen) zur Liste hinzu
                        inventory_lines.append(';'.join(line_data))

            # Schreibe die aktualisierten Daten zurück in die Datei
            with open(file_path, 'w') as file:
                for line in inventory_lines:
                    file.write(line + "\n")

        # Wenn die Datei nicht gefunden wurde, gebe eine Fehlermeldung aus
        except FileNotFoundError:
            print(f"Datei {file_path} nicht gefunden.")

        # Fange andere Fehler ab und gebe eine Fehlermeldung aus
        except Exception as e:
            print(f"Fehler beim Aktualisieren der Datei: {e}")




# noch ein paar benötigte Funktionen außerhalb der Klasse



# Reuse der Save und Load Funktionen aus der ui_Usermanagement.py
def save_users_to_file():
    print("Methode save_users_to_file aufgerufen")  # Debug
    file_path = "Userinformationen.txt"  # Kann bei Bedarf angepasst werden
    try:
        with open(file_path, 'w') as file:  # Aufruf im Write-Modus, damit die Datei jedes Mal überschrieben wird
            for username, balance in users.items():  # Verwende 'balance' direkt, da 'data' der float-Wert ist
                file.write(f"{username};{balance}\n")
        print(f"Benutzerinformationen erfolgreich in {file_path} gespeichert.")
    except Exception as e:  # just in Case
        print(f"Fehler beim Speichern der Benutzerinformationen: {e}")


# Diese Methode ruft die Userinformation aus der mit save_users_to_file angelegten txt ab
def load_users_from_file():
    file_path = "Userinformationen.txt"  # kann bei Bedarf verändert werden
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Jede Zeile in der txt sollte so aussehen Username;Kontostand"
                user_data = line.strip().split(';')
                if len(user_data) == 2:  # Es soll nur Name und Kontostand abgelegt sein, also 2 Einträge
                    username = user_data[0]
                    try:
                        balance = float(user_data[1])  # Kontostand von String in Float
                        users[username] = balance  # Statt add_user werden jetzt die Infos einfach in das users-Dictionary geschrieben
                    except ValueError:
                        print(f"Ungültiger Kontostand für Benutzer: {username}")
                else:
                    print(f"Dateiaufbau prüfen. Fehler in Zeile: {line}")
        print("Userinformationen erfolgreich aus der Datei geladen.")
    except FileNotFoundError:
        print(f"Datei nicht gefunden")
    except Exception as e:
        print(f"sonstiger Fehler")

# Abrufen der Userdaten aus der Textdatei
load_users_from_file()
print(users)





# von Qt5 erstellt
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Produktauswahl = QtWidgets.QMainWindow()
    ui = Ui_Produktauswahl()
    ui.setupUi(Produktauswahl)
    Produktauswahl.show()
    sys.exit(app.exec_())
