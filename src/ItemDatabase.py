#iFridge
#API course
#(c) Daniel Smigala, Yasmine Hildebrand, Constantin Denden, Julius Schieck, David Nagel

inventory = [] #contains all items which are stored in fridge

class StackableItem(self, name, expirys):
    def __init__(self, name, expiries):
        self.name = name
        self.expiries = expiries #List of expiry dates of stacked item
        self.quantity = None #Quantity of stacked items of same type

    def count(self):
        self.quantity = len(self.expiry)
        return self.quantity

    def Add(self, expiry):
        self.expiries.append(expiry)
