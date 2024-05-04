#iFridge
#API course
#(c) Daniel Smigala, Yasmine Hildebrand, Constantin Denden, Julius Schieck, David Nagel

_inventory = [] #Contains all items which are stored in fridge. Do NOT directly access _inventory!

class Inventory:
    def newItem(self, name, expiry):
        list = [expiry]
        _inventory.append(StackableItem(name,list))

    def addItem(self, type, name, expiry):


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
        for i in range self.quantity:
            if i != index:
                list.append(self.expiries(i))
        self.expiries = list
        self.quantity -= 1


class ContinuousItem:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def getQuantity(self):
        return self.quantity

    def refill(self, addend):
        self.quantity += addend

    def take(self, subtrahend):
        self.quantity -= subtrahend