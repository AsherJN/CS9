from Beverage import Beverage
"""
The Coffee.py file will contain the class definition of what a coffee beverage will have. 
Since a coffee IS-A beverage, we will inherit the values we defined in the Beverage class.
"""

class Coffee(Beverage):
    def __init__(self, ounces, price, style):
        super().__init__(ounces, price)
        self.style = str(style)

    def getInfo(self):
        pass


