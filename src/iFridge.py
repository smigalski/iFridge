#iFridge
#API course
#(c) Daniel Smigala, Yasmine Hildebrand, Constantin Denden, Julius Schieck, David Nagel

#This is the main file of the iFridge project.
#Please try to implement as much as possible as modules.
#This file should only contain the superior procedures.


#Modules:

import Inventory


#Config:

inventorypath = "Inventory"
userspath = "Users"



#Procedures:

try:
    Inventory.ImportInventory(inventorypath)
    print("Inventory loaded from " + inventorypath + " ." )
except:
    print("Error: An Error occoured while loading inventory from " + inventorypath + " .")




#Hauptmenü öffnen




#Inventory.ExportInventory(inventorypath)










