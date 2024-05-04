#iFridge
#API course
#(c) Daniel Smigala, Yasmine Hildebrand, Constantin Denden, Julius Schieck, David Nagel

_inventory = [] #Contains all items which are stored in fridge. Do NOT directly access _inventory!

class Inventory:
    def getInventory(self):
        return _inventory

    def newItem(self, type, name, expiry, quantity, unit): #type can be "stackable" or "continous". unit can be "[]" or nothing if item is stackable. quantity must be 1 for stackable items.
        if type == "stackable" or type == "continous":
            if type == "stackable":
                list = [expiry]
                _inventory.append(StackableItem(name, list))
            if type == "continous":
                list = [expiry]
                _inventory.append(ContinuousItem(name, expiry, quantity, unit))
        else:
            print("Error: type {type} is unknown.")

    def addItem(self, type, name, expiry, addend): #Increases quantity and adds properties to an existing type of item. addend is the added quantity for continous items or must be 1 for countable items. expiry can be nothing for continous items.
        for i in range (len(_inventory) - 1):
            if name == _inventory[i].name:
                if type == "stackable" or type == "continous":
                    if type == "stackable":
                        if addend == 1 or addend == "":
                            _inventory[i].add(expiry)
                        else:
                            print("Error: You can ony add one stackable item at one time! addend must be 1.")
                    if type == "continous":
                        _inventory[i].refill(addend)
                else:
                    print("Error: type {type} is unknown.")


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

    def refill(self, addend):
        self.quantity += addend

    def take(self, subtrahend):
        self.quantity -= subtrahend