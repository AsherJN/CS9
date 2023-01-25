# Defines a Pizza class representing commonality for all Pizzas
class Pizza:
    def __init__(self, size=None):
        self.price = 0
        self.size = str(size.upper())

    #getter setter methods
    def getPrice(self):
        return self.price
    def getSize(self):
        return self.size

    def setPrice(self, price):
        self.price = float(price)
    def setSize(self, size):
        self.size = str(size)

# p1 = Pizza(25.99, 'M')
# assert p1.getPrice() == 25.99
# assert p1.getSize() == 'M'
# p1.setPrice(5.50)
# assert p1.getPrice() == 5.50
# p1.setSize('L')
# assert p1.getSize() == 'L'