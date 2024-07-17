
#Import Funktionen, Klassen von .py Dateien ----------------------------------------------------------------------------
import Inventory


#Config   --------------------------------------------------------------------------------------------------------------

inventorypath = "Storage/Inventory"
userspath = "Storage/Users"

#Procedures   ----------------------------------------------------------------------------------------------------------

Inventory.newItem("continous","Kekse",12345,1,1,1)

print(Inventory.ItemInfo(0))



