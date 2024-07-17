
import Inventory



Inventory.newItem("continous","Milch",12345,3,"L",1)
Inventory.newItem("stackable","Kekse",12345,1,1,1)

print(Inventory.ItemInfo(0))
print(Inventory.ItemInfo(1))
print(Inventory.InventoryToString())


