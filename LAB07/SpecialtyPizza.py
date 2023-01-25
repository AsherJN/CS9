#Defines a child class of Pizza. This class should inherit all fields /
# methods from the Pizza class. Specialty pizzas are defined by a name
# attribute and all have a set price depending on the pizza size
from Pizza import Pizza
from CustomPizza import CustomPizza
class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        super().__init__(size)
        self.name = str(name)
        if self.size == 'S':
            self.price = float(12.00)
        elif self.size == 'M':
            self.price = float(14.00)
        elif self.size == 'L':
            self.price = float(16.00)

    def getPizzaDetails(self):
        """
        this method will construct and return a string containing the details of
        the SpecialtyPizza object including the size and name of the SpecialtyPizza
        """
        # str = \
        # f"SPECIALTY PIZZA\n\
        # Size: {self.size}\n\
        # Name: {self.name}\n\
        # Price: ${'{0:.2f}'.format(self.price)}\n"
        # return str
        return f"SPECIALTY PIZZA\nSize: {self.size}\nName: {self.name}\nPrice: ${'{0:.2f}'.format(self.price)}\n"




# sp1 = SpecialtyPizza('L', 'Chupacabra')
# print(sp1.getSize())
# print(sp1.getPrice())
# print(sp1.getPizzaDetails())