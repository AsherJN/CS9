"""
This file will contain your pytest functions that tests the overall
correctness of your class definitions.
"""
from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

def test_car():
    c1 = Car("Tesla", "Model Y", 2020, 55000)
    c2 = Car("Toyota", "4Runner", 2010, 15000)
    c3 = Car("Honda", "Civic", 2001, 2000)
    c4 = Car("Cherolet", "Bolt", 2016, 25000)
    c5 = Car("Hyundai", "Ioniq 5", 2022, 45000)
    c6 = Car("Toyota", "4Runner", 2010, 21000)
    c7 = Car("Tesla", "Model Y", 2019, 51000)
    c8 = Car("Honda", "Element", 2012, 12000)
    c9 = Car("chevRolEt", "bolt", 2016, 25000)

    assert (c1 > c2) == False
    assert (c1 < c2) == True
    assert (c3 == c4) == False
    assert (c9 == c4) == False
    assert (c7 < c1) == True
    assert (c6 > c2) == True
    assert (c5 == c8) == False
    assert (c8 < c3) == False

    assert str(c1) == "Make: TESLA, Model: MODEL Y, Year: 2020, Price: $55000"
    assert str(c9) == "Make: CHEVROLET, Model: BOLT, Year: 2016, Price: $25000"

def test_CarInventoryNode():
    c1 = Car("Tesla", "Model Y", 2020, 55000)
    c2 = Car("Toyota", "4Runner", 2010, 15000)
    c3 = Car("Honda", "Civic", 2001, 2000)
    c4 = Car("Cherolet", "Bolt", 2016, 25000)
    c5 = Car("Hyundai", "Ioniq 5", 2022, 45000)
    c6 = Car("Toyota", "4Runner", 2010, 21000)
    c7 = Car("Tesla", "Model Y", 2019, 51000)
    c8 = Car("Honda", "Element", 2012, 12000)
    c9 = Car("chevRolEt", "bolt", 2016, 25000)

    cin1 = CarInventoryNode(c1)
    assert cin1.getMake() == "TESLA"
    assert cin1.getModel() == "MODEL Y"
    assert cin1.getParent() == None
    assert cin1.cars == [c1]

    cin1.cars.append(c7)
    assert cin1.cars == [c1, c7]
    assert str(cin1) == "Make: TESLA, Model: MODEL Y, Year: 2020, Price: $55000\nMake: TESLA, Model: MODEL Y, Year: 2019, Price: $51000\n"

    cin2 = CarInventoryNode(c2)
    cin1.setParent(cin2)
    assert cin1.parent == cin2

    cin3 = CarInventoryNode(c3)
    cin4 = CarInventoryNode(c4)
    cin1.setLeft(cin3)
    cin1.setRight(cin4)
    assert cin1.getLeft() == cin3
    assert cin1.getRight() == cin4

def test_CarInventory():
    c1 = Car("Tesla", "Model Y", 2020, 55000)
    c2 = Car("Toyota", "4Runner", 2010, 15000)
    c3 = Car("Honda", "Civic", 2001, 2000)
    c4 = Car("Cherolet", "Bolt", 2016, 25000)
    c5 = Car("Hyundai", "Ioniq 5", 2022, 45000)
    c6 = Car("Toyota", "4Runner", 2010, 21000)
    c7 = Car("Tesla", "Model Y", 2019, 51000)
    c8 = Car("Honda", "Element", 2012, 12000)
    c9 = Car("chevRolEt", "bolt", 2016, 25000)

    ci = CarInventory()
    assert ci.root == None

    ci.addCar(c1)
    assert ci.inOrder() == "Make: TESLA, Model: MODEL Y, Year: 2020, Price: $55000\n"

    ci.addCar(c7)

    assert ci.inOrder() == "Make: TESLA, Model: MODEL Y, Year: 2020, Price: $55000\nMake: TESLA, Model: MODEL Y, Year: 2019, Price: $51000\n"

    ci.addCar(c2)
    ci.addCar(c3)
    ci.addCar(c4)
    ci.addCar(c5)
    ci.addCar(c6)
    ci.addCar(c8)
    #ci.addCar(c9)
    #print(ci.postOrder())

    print(ci.doesCarExist(c8))

# def test_getTotalAssets():
#     bst = CarInventory()
#     car1 = Car("Nissan", "Leaf", 2018, 18000)
#     car2 = Car("Tesla", "Model3", 2018, 50000)
#     car3 = Car("Mercedes", "Sprinter", 2022, 40000)
#     car4 = Car("Mercedes", "Sprinter", 2014, 25000)
#     car5 = Car("Ford", "Ranger", 2021, 25000)
#     bst.addCar(car1)
#     bst.addCar(car2)
#     bst.addCar(car3)
#     bst.addCar(car4)
#     bst.addCar(car5)
#     assert bst.getTotalInventoryPrice() == 158000




