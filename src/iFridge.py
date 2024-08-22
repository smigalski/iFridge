#iFridge
#API course
#(c) Daniel Smigala, Yasmine Hildebrand, Constantin Denden, Julius Schieck, David Nagel
#This is the main file of the iFridge project.
#This file should only contain the superior procedures.


#Modules   -------------------------------------------------------------------------------------------------------------
import sys
from PyQt5 import QtWidgets


#Import Funktionen, Klassen von .py Dateien ----------------------------------------------------------------------------
import Inventory
import UserImportExport
from Hauptfenster import Ui_QMainWindow



#Config   --------------------------------------------------------------------------------------------------------------

inventorypath = "Storage/Inventory"
userspath = "Storage/Users"

#Procedures   ----------------------------------------------------------------------------------------------------------


#Import des Inventory:
try:
    Inventory.ImportInventory(inventorypath)
    print("Inventory loaded from >" + inventorypath + "<." )
except:
    print("Error: An Error occoured while loading inventory from >" + inventorypath + "<. Ignore this error if this is the first run on this device or after an reset to factory state.")

try:
    UserImportExport.ImportUsers(userspath)
    print("Users loaded from >" + userspath + "<.")
except:
    print("Error: An Error occoured while loading users from >" + userspath + "<. Ignore this error if this is the first run on this device or after an reset to factory state.")


# Start des Hauptfenster.py
app = QtWidgets.QApplication(sys.argv)

Hauptfenster = Ui_QMainWindow()
Hauptfenster.show()
Hauptfenster.openMainWindow()



#Export inventory and users:
Inventory.ExportInventory(inventorypath)
print("Inventory successfully exported to >" + inventorypath + "<.")
#UserImportExport.ExportUsers(userspath)
print("Users successfully exported to >" + userspath + "<.")


#Die Ui schließen
sys.exit(app.exec_())

