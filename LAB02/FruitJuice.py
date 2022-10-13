from Beverage import Beverage
"""
The FruitJuice.py file will contain the class definition of what a fruit juice beverage will have. 
Since a fruit juice IS-A beverage, we will inherit the values we defined in the Beverage class.
"""

class FruitJuice(Beverage):
    def __init__(self, ounces, price, fruits):
        super().__init__(ounces, price)
        self.fruits = str(fruits)

    def getInfo(self):
        pass

