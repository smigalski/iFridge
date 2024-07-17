#iFridge
#API course
#(c) Daniel Smigala, Yasmine Hildebrand, Constantin Denden, Julius Schieck, David Nagel

_inventory = [] #Contains all items which are stored in fridge. Do NOT directly access _inventory!


def getInventory():
    return _inventory


def newItem(type, name, expiry, quantity, unit, targetquantity = 0): #type can be "stackable" or "continous". unit can be "1" or "" if item is stackable. quantity must be 1 for stackable items.
    if getItemIndex(name) == -1:
        if type == "stackable" or type == "continous":
            if type == "stackable":
                if quantity == 1 or quantity == "":
                    list = [int(expiry)]
                    _inventory.append(StackableItem(name, list, targetquantity))
                else:
                    print("Error: You can ony add one stackable item at one time! quantity must be 1.")
            if type == "continous":
                _inventory.append(ContinuousItem(name, int(expiry), quantity, unit, targetquantity))
        else:
            print(f"Error: type {type} is unknown.")
    else:
        print(f"Error: There is already an item with the name {name} existing. Choose an other name or add quantity to the existing item with addItem(type, name, expiry, addend)")


def addItem(type, name, expiry, addend): #Increases quantity and adds properties to an existing type of item. addend is the added quantity for continous items or must be 1 for countable items. expiry can be nothing for continous items.
    index = getItemIndex(name)
    if index == -1:
        print(f"Error: There is no item named {name} found. You may made an typo or need to add a new item.")
    if type == "stackable" or type == "continous":
        if type == "stackable":
            if addend == 1 or addend == "":
                _inventory[index].add(int(expiry))
            else:
                print("Error: You can ony add one stackable item at one time! addend must be 1.")
        if type == "continous":
            _inventory[index].refill(addend, int(expiry))
    else:
        print("Error: type {type} is unknown.")


def ItemInfo(index):
    information = "Error"
    if _inventory[index].type == "StackableItem":
        information = [index,_inventory[index].type,_inventory[index].name,_inventory[index].getQuantity(),_inventory[index].unit,_inventory[index].expiries,_inventory[index].targetquantity]
    if _inventory[index].type == "ContinuousItem":
        information = [index, _inventory[index].type, _inventory[index].name, _inventory[index].quantity, _inventory[index].unit, _inventory[index].expiry, _inventory[index].targetquantity]
    return information


def getNumberOfItems():
    return len(_inventory)


def takeItem(index, subtrahend):    #quantity must be 1 or "" for StackableItem(s)
    information = ItemInfo(index)
    if (information[1] == "StackableItem"):
        if (subtrahend == 1) or (subtrahend == ""):
            _inventory.remove(index)
            information[3] = information[3][len(information[3]) - 1]
            information.append(1)
        else:
            print("Error: You can only take on StackableItem at a time. Subtrahend must be 1 for StackableItem(s).")
            information = "Error"
    if (information[1] == "ContinuousItem"):
        information.append(_inventory.take(subtrahend))
    if (information[6] == "Error"):
        information = "Error"
    return information


def getItemIndex(name):
    index = -1
    for i in range (len(_inventory)):
        if name == _inventory[i].name:
            index = i
    return index


def setTargetquantity(index, targetquantity):
    _inventory[index].setTargetquantity(targetquantity)




#classes for items
#There will be 2 Types of items contained in inventory: StackableItem(s) and CountinousItem(s)


class StackableItem:
    def __init__(self, name, expiries, targetquantity = 0):
        self.type = "StackableItem"
        self.name = name
        self.expiries = expiries #List of expiry dates of stacked item
        self.unit = ""
        self.targetquantity = targetquantity

    def getQuantity(self):
        return len(self.expiries)

    def add(self, expiry):
        self.expiries.append(expiry)

    def remove(self, index):
        answer = 1
        if self.quantity > 0:
            list = []
            for i in range (self.quantity):
                if i != index:
                    list.append(self.expiries(i))
            self.expiries = list
            self.quantity -= 1
        else:
            print("Error: You try to remove an Item from a quantity of zero.")
            answer = "Error"
        return answer

    def setTargetquantity(self, tgtqty):
        self.targetquantity = tgtqty


class ContinuousItem:
    def __init__(self, name, expiry, quantity, unit, targetquantity = 0):
        self.type = "ContinuousItem"
        self.name = name
        self.expiry = expiry
        self.quantity = quantity
        self.unit = unit
        self.targetquantity = targetquantity

    def getQuantity(self):
        return self.quantity

    def refill(self, addend, expiry):
        if self.quantity == 0:
            self.expiry = expiry
        self.quantity += addend

    def take(self, subtrahend):
        answer = subtrahend
        self.quantity -= subtrahend
        if (self.quantity < 0):
            answer = subtrahend + self.quantity
            print("Error: You try to take more quantity of an Item than its actual existing quantity.")
            self.quantity = 0
        return answer

    def setTargetquantity(self, tgtqty):
        self.targetquantity = tgtqty


def InventoryToString():
    InventoryString = ""
    index = 0
    while (index < getNumberOfItems()):
        if (index > 0):
            InventoryString += "\n"
        InventoryString += str(ItemInfo(index)[1]) + ";" + str(ItemInfo(index)[2]) + ";" + str(ItemInfo(index)[3])  + ";" + str(ItemInfo(index)[6]) + ";" + str(ItemInfo(index)[4])
        if ItemInfo(index)[1] == "StackableItem":
            i = 0
            while (i < len(ItemInfo(index)[5])):
                InventoryString += str(ItemInfo(index)[5][i]) + ";"
                i += 1
        else:
            InventoryString += str(ItemInfo(index)[5]) + ";"
        index += 1
    return InventoryString
    #File format: [type];[name];[quantity];[targetquantity];[unit];[expiry1];[expiry2];...


def ExportInventory(filename = "Inventory.txt"):
    file = open(filename, "w")
    file.write(InventoryToString())
    file.close()


def ImportInventory(filename = "Inventory.txt"):
    InventoryToString = []
    file = open(filename, "r")
    index = 0
    for line in file:
        InventoryToString.append(file.readline())
        char = 0
        field = 0
        Iteminfo = []
        Text = ""
        while (char < len(InventoryToString)):
            if (InventoryToString[index][char] != ";"):
                if (InventoryToString[index][char] != " "):
                    Text += str(InventoryToString[index][char])
            else:
                Iteminfo.append(Text)
                field += 1
                Text = ""
            char += 1
        count = 1
        while(count + 4 < len(ItemInfo([index]))):
            if (getItemIndex(InventoryToString[index][1]) == -1):
                if (Iteminfo[index][0] == "stackable"):
                    newItem(InventoryToString[index][0], InventoryToString[index][1], InventoryToString[index][4], 1,
                            InventoryToString[index][4], int(InventoryToString[index][2]))
                    count += 1
                else:
                    if (Iteminfo[index][0] == "stackable"):
                        newItem(InventoryToString[index][0], InventoryToString[index][1], InventoryToString[index][4],
                                InventoryToString[index][3],
                                InventoryToString[index][4], int(InventoryToString[index][2]))
                        count += 1
                    else:
                        print(f"Error in line {index}. Unknown type.")
            else:
                addItem(InventoryToString[index][0],InventoryToString[index][1],InventoryToString[index][count+4],1)
                count += 1
        index += 1



