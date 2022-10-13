
"""
The Beverage.py file will contain the class definition of what a general beverage is.

We will define this class’ attributes as follows:

ounces - positive int that represents the number of ounces of the beverage.
price - positive float that represents the price of the beverage.
"""

class Beverage:
    def __init__(self, ounces, price):
        self.ounces = int(ounces)
        self.price = float(price)

    #Setter getter methods
    def updateOunces(self, newOunces):
        """
        updates the ounces of the beverage
        """
        self.ounces = int(newOunces)

    def updatePrice(self, newPrice):
        """
        updates the price of the beverage
        """
        self.price = float(newPrice)

    def getOunces(self):
        """
        returns the ounces of the beverage
        """
        return self.ounces

    def getPrice(self):
        """
        returns the price of the beverage
        """
        return self.price

    def getInfo(self):
        pass