# Defines a child class of Pizza. This class should inherit all fields / methods
# from the Pizza class, but also introduces the concepts of toppings a customer
# can order (represented as a list of strings)
from Pizza import Pizza

class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.topping = []
        if self.size == 'S':
            self.price = float(8.00) #+ (len(topping) * .5))
        elif self.size == 'M':
            self.price = float(10.00) #+ (len(topping) * .75))
        elif self.size == 'L':
            self.price = float(12.00) #+ (len(topping) * 1.00))

    #other methods
    def addTopping(self, topping):
        """
        this method will add to the toppings list and update its
        price appropriately. The topping parameter is represented
        as a str type
        """
        self.topping.append(topping)
        if self.size == 'S':
            self.price = float(8.00 + (len(self.topping) * .5))
        elif self.size == 'M':
            self.price = float(10.00 + (len(self.topping) * .75))
        elif self.size == 'L':
            self.price = float(12.00 + (len(self.topping) * 1.00))

    def getPizzaDetails(self):
        """
        this method will construct and return a string containing the details of
        the CustomPizza object including the size, toppings, and price of the
        CustomPizza.
        """
        str = f"CUSTOM PIZZA\nSize: {self.size}\nToppings:\n"
        tempstr = ''
        for item in self.topping:
            tempstr += f"\t+ {item}\n"
        str += tempstr
        return str + f"Price: ${'{0:.2f}'.format(self.price)}\n"

        #return f"CUSTOM PIZZA\nSize: {self.size}\nToppings: {self.topping}\nPrice: ${self.price}\n"

# p1 = CustomPizza('L')
#
# p1.addTopping('dog shit')
#
# # print(p1.getPrice())
#
# print(p1.getPizzaDetails())

# p1 = CustomPizza('L')
# assert p1.getPrice() == 12
# p1.addTopping('Spinach')
# p1.addTopping('Mushroom')
# p1.addTopping('Olive')
# assert p1.getPrice() == 15
# print(p1.getPizzaDetails())