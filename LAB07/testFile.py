# This file will contain your pytest functions that tests the overall
# correctness of your class definitions
from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue
def test_pizza():
    p1 = Pizza('M')
    assert p1.getSize() == 'M'
    p1.setPrice(5.50)
    assert p1.getPrice() == 5.50
    p1.setSize('L')
    assert p1.getSize() == 'L'

def test_customPizza():
    p1 = CustomPizza('L')
    assert p1.getPrice() == 12
    p1.addTopping('Spinach')
    p1.addTopping('Mushroom')
    p1.addTopping('Olive')
    assert p1.getPrice() == 15
    assert p1.getPizzaDetails() == "CUSTOM PIZZA\nSize: L\nToppings:\n\t+ Spinach\n\t+ Mushroom\n\t+ Olive\nPrice: $15.00\n"

def test_specialtyPizza():
    sp1 = SpecialtyPizza('L', 'Chupacabra')
    assert sp1.getPrice() == 16
    assert sp1.getSize() == 'L'
    assert sp1.getPizzaDetails() == "SPECIALTY PIZZA\nSize: L\nName: Chupacabra\nPrice: $16.00\n"

def test_pizzaOrder():
    p1 = CustomPizza('M')
    p1.addTopping('Pineapple')
    sp1 = SpecialtyPizza('s', 'Chicago Blues')

    po1 = PizzaOrder(230523)
    po1.addPizza(p1)
    po1.addPizza(sp1)
    assert po1.getOrderDescription() == \
"******\n\
Order Time: 230523\n\
CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
\t+ Pineapple\n\
Price: $10.75\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Chicago Blues\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $22.75\n\
******\n"

    p2 = CustomPizza('S')
    p2.addTopping('apple')
    p2.addTopping('banana')
    p2.addTopping('orange')
    p2.addTopping('peach')
    p2.addTopping('lettuce')
    p2.addTopping('cumcumber')
    p2.addTopping('poop')

    po2 = PizzaOrder(800)
    po2.addPizza(p2)
    assert po2.getOrderDescription() == \
"******\n\
Order Time: 800\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ apple\n\
\t+ banana\n\
\t+ orange\n\
\t+ peach\n\
\t+ lettuce\n\
\t+ cumcumber\n\
\t+ poop\n\
Price: $11.50\n\
\n\
----\n\
TOTAL ORDER PRICE: $11.50\n\
******\n"

def test_OrderQueue():
    p1 = CustomPizza('M')
    p1.addTopping('Pineapple')
    sp1 = SpecialtyPizza('s', 'Chicago Blues')

    po1 = PizzaOrder(230523)
    po1.addPizza(p1)
    po1.addPizza(sp1)

    p2 = CustomPizza('S')
    p2.addTopping('apple')
    p2.addTopping('banana')
    p2.addTopping('orange')
    p2.addTopping('peach')
    p2.addTopping('lettuce')
    p2.addTopping('cumcumber')
    p2.addTopping('poop')

    po2 = PizzaOrder(800)
    po2.addPizza(p2)

    oq1 = OrderQueue()

    oq1.addOrder(po1)
    oq1.addOrder(po2)

    assert oq1.processNextOrder() == \
"******\n\
Order Time: 800\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ apple\n\
\t+ banana\n\
\t+ orange\n\
\t+ peach\n\
\t+ lettuce\n\
\t+ cumcumber\n\
\t+ poop\n\
Price: $11.50\n\
\n\
----\n\
TOTAL ORDER PRICE: $11.50\n\
******\n"
    assert oq1.processNextOrder() == \
"******\n\
Order Time: 230523\n\
CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
\t+ Pineapple\n\
Price: $10.75\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Chicago Blues\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $22.75\n\
******\n"



