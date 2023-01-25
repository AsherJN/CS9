#Defines a class that is a collection of pizza objects the customer wants
# to order. The total price for the order can be derived from each individual
# pizza price. This class will also have an expected time of when the customer
# would like their pizzas ready for pickup. More details on this later in the writeup

from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder:
    def __init__(self, time):
        self.pizzas = []
        self.time = int(time)

    #Getter setter methods
    def getTime(self):
        return self.time
    def setTime(self, time):
        self.time = int(time)
    def addPizza(self, pizza):
        self.pizzas.append(pizza)
    def getOrderDescription(self):
        str = '******\n'
        str += f"Order Time: {self.time}\n"
        for item in self.pizzas:
            str += item.getPizzaDetails() + "\n"
            str += "----\n"
        totalCost = 0
        for cost in self.pizzas:
            totalCost += cost.getPrice()
        str += f"TOTAL ORDER PRICE: ${'{0:.2f}'.format(totalCost)}\n******\n"
        return str


# p1 = CustomPizza('M')
# p1.addTopping('Pineapple')
# sp1 = SpecialtyPizza('s', 'Chicago Blues')
#
# po1 = PizzaOrder(230523)
# po1.addPizza(p1)
# po1.addPizza(sp1)
#
# print(po1.getOrderDescription())
# p2 = CustomPizza('S')
# p2.addTopping('apple')
# p2.addTopping('banana')
# p2.addTopping('orange')
# p2.addTopping('peach')
# p2.addTopping('lettuce')
# p2.addTopping('cumcumber')
# p2.addTopping('poop')
#
# po2 = PizzaOrder(800)
# po2.addPizza(p2)
# print(po2.getOrderDescription())







