#iFridge
#API course
#(c) Daniel Smigala, Yasmine Hildebrand, Constantin Denden, Julius Schieck, David Nagel

_inventory = [] #Contains all items which are stored in fridge. Do NOT directly access _inventory!

def getInventory():
    return _inventory

def newItem(type, name, expiry, quantity, unit): #type can be "stackable" or "continous". unit can be "[]" or nothing if item is stackable. quantity must be 1 for stackable items.
    if getItemIndex(name) == -1
        if type == "stackable" or type == "continous":
            if type == "stackable":
                if quantity == 1 or quantity == "":
                    list = [expiry]
                    _inventory.append(StackableItem(name, list))
                else:
                    print("Error: You can ony add one stackable item at one time! quantity must be 1.")
            if type == "continous":
                _inventory.append(ContinuousItem(name, expiry, quantity, unit))
        else:
            print("Error: type {type} is unknown.")
    else:
        print("Error: There is already an item with the name {name} existing. Choose an other name or add quantity to the existing item with addItem(type, name, expiry, addend)")

def addItem(type, name, expiry, addend): #Increases quantity and adds properties to an existing type of item. addend is the added quantity for continous items or must be 1 for countable items. expiry can be nothing for continous items.
    index = getItemIndex(name)
    if index == -1:
        print("Error: Es konnte kein Produkt mit dem Namen {name} gefunden werden.")
    if type == "stackable" or type == "continous":
        if type == "stackable":
            if addend == 1 or addend == "":
                _inventory[index].add(expiry)
            else:
                print("Error: You can ony add one stackable item at one time! addend must be 1.")
        if type == "continous":
            _inventory[index].refill(addend, expiry)
    else:
        print("Error: type {type} is unknown.")

def getItemIndex(name):
    index = -1
    for i in range(len(_inventory) - 1):
        if name == _inventory[i].name:
            index = i
    return index

#classes for items
#There will be 2 Types of items contained in inventory: StackableItem(s) and CountinousItem(s)

class StackableItem:
    def __init__(self, name, expiries):
        self.name = name
        self.expiries = expiries #List of expiry dates of stacked item
        self.quantity = 0 #Quantity of stacked items of same type

    def getQuantity(self):
        return self.quantity


    def add(self, expiry):
        self.quantity += 1
        self.expiries.append(expiry)

    def remove(self, index):
        list = []
        for i in range (self.quantity - 1):
            if i != index:
                list.append(self.expiries(i))
        self.expiries = list
        self.quantity -= 1


class ContinuousItem:
    def __init__(self, name, expiry, quantity, unit):
        self.name = name
        self.expiry = expiry
        self.quantity = quantity
        self.unit = unit

    def getQuantity(self):
        return self.quantity

    def refill(self, addend, expiry):
        if self.quantity == 0:
            self.expiry = expiry
        self.quantity += addend

    def take(self, subtrahend):
        self.quantity -= subtrahend