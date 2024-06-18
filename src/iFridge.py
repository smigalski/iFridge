#iFridge
#API course
#(c) Daniel Smigala, Yasmine Hildebrand, Constantin Denden, Julius Schieck, David Nagel

#This is the main file of the iFridge project.
#Please try to implement as much as possible as modules.
#This file should only contain the superior procedures.


#Modules   -------------------------------------

import Inventory


#Config   -------------------------------------

inventorypath = "Storage/Inventory"
userspath = "Storage/Users"



#Procedures   -------------------------------------

#Load inventory and users:
try:
    Inventory.ImportInventory(inventorypath)
    print("Inventory loaded from >" + inventorypath + "<." )
except:
    print("Error: An Error occoured while loading inventory from >" + inventorypath + "<. Ignore this error if this is the first run on this device or after an reset to factory state.")

#try:
#   Inventory.ImportUsers(userspath)
#   print("Users loaded from >" + userpath + "<.")
#except:
#   print("Error: An Error occoured while loading users from >" + userspath + "<. Ignore this error if this is the first run on this device or after an reset to factory state.")




#show main menu:





#Export inventory and users:
Inventory.ExportInventory(inventorypath)
#Inventory.ExportUsers(userspath)