"""
Defines a CarInventory (BST) class that is an ordered collection of a
Dealership’s Cars. You can adapt the BST implementation shown in the
textbook supporting the specifications in this lab.
"""

from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:
    def __init__(self):
        self.root = None

    def addCar(self, car):
        if self.root:
            self._add(car, self.root)
        else:
            self.root = CarInventoryNode(car)

    def _add(self, car, currentNode):
        if currentNode:
            if car.make < currentNode.make:
                if currentNode.getLeft():
                    self._add(car, currentNode.left)
                else:
                    currentNode.left = CarInventoryNode(car)


            elif car.make == currentNode.make:
                if car.model < currentNode.model:
                    if currentNode.getLeft():
                        self._add(car, currentNode.left)
                    else:
                        currentNode.left = CarInventoryNode(car)


                elif car.model == currentNode.model:
                    currentNode.cars.append(car)
                elif car.model > currentNode.model:
                    if currentNode.getRight():
                        self._add(car, currentNode.left)
                    else:
                        currentNode.right = CarInventoryNode(car)


            elif car.make > currentNode.make:
                if currentNode.getRight():
                    self._add(car, currentNode.left)
                else:
                    currentNode.right = CarInventoryNode(car)

    def doesCarExist(self, car):
        if self._doesCarExist(car, self.root):
            return True
        else:
            return False

    def _doesCarExist(self, car, currentNode):

        if not currentNode:
            return None
        for item in currentNode.cars:
            if item.make == car.make:
                if item.model == car.model:
                    return currentNode
                elif car.model < item.model:
                    return self._doesCarExist(car, currentNode.left)
                else:
                    return self._doesCarExist(car, currentNode.right)
            elif car.make < item.make:
                return self._doesCarExist(car, currentNode.left)
            else:
                return self._doesCarExist(car, currentNode.right)





    def inOrder(self):
        return self._inOrder(self.root)
    def _inOrder(self, tree):
        ret = ""
        if tree:
            ret += str(self._inOrder(tree.getLeft()))
            ret += str(tree)
            ret += str(self._inOrder(tree.getRight()))
        else:
            return ''
        return ret
    def preOrder(self):
        return self._preOrder(self.root)
    def _preOrder(self, tree):
        ret = ""
        if tree:
            ret += str(tree)
            ret += str(self._preOrder(tree.getLeft()))
            ret += str(self._preOrder(tree.getRight()))
        else:
            return ''
        return ret

    def postOrder(self):
        return self._postOrder(self.root)
    def _postOrder(self, tree):
        ret = ""
        if tree:
            ret += str(self._postOrder(tree.getLeft()))
            ret += str(self._postOrder(tree.getRight()))
            ret += str(tree)
        else:
            return ''
        return ret
    def getBestCar(self, make, model):
        pass
    def getWorstCar(self, make, model):
        pass
    def getTotalInventoryPrice(self):
        return self._getTotalInventoryPrice(self.root)
    def _getTotalInventoryPrice(self, currentNode):
        total = 0
        for i in currentNode.cars:
            total += i.price
        for i in currentNode.left.cars:
            total += i.price
        for i in currentNode.right.cars:
            total += i.price
#################################################################
#################################################################




    # def getSuccessor(self, make, model):
    #     succ = None
    #     # Check if node has a right subtree...
    #     if self.getRight():
    #         # traverse through left children (min)
    #         succ = self.right.findMin()
    #     return succ
    #
    # def findMin(self):
    #     current = self
    #     while current.getLeft():
    #         current = current.left
    #     return current
    def get(self, car):
        if self.root:
            res = self._get(car, self.root)
            if res:
                return res.cars
            else:
                return None
        else:
            return None

    def _get(self, make, model, year, price, currentNode):
        if not currentNode:
            return None
        for item in currentNode.cars:
            if item.make == make:
                if item.model == model:
                    if item.year == year:
                        if item.price == price:
                            return currentNode
                else:
                    if model < item.model:
                        return self._get(make, model, year, price, currentNode.left)
                    else:
                        return self._get(make, model, year, price, currentNode.right)

        if make < item.make:
            return self._get(make, model, year, price, currentNode.left)
        else:
            return self._get(make, model, year, price, currentNode.right)


    def removeCar(self, make, model, year, price):
        if self.root:
            nodeToRemove = self._get(make, model, year, price, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)  # remove modifies the tree
            else:
                raise KeyError('Error, key not in tree')
        elif self.root.make == make:
            if self.root.model == model:
                self.root = None
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, currentNode):
        # Case 1: Node to remove is leaf
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.left:
                currentNode.parent.left = None
            else:
                currentNode.parent.right = None

        # Case 3: Node to remove has both children
        elif currentNode.hasBothChildren():
            # Need to find the successor, remove successor, and replace
            # currentNode with successor's data / payload
            succ = currentNode.getSuccessor()
            succ.spliceOut()
            currentNode.cars = succ.cars
            currentNode.cars = succ.cars

        # Case 2: Node to remove has one child
        else:
            # Node has leftChild
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.left = currentNode.left
                elif currentNode.isRightChild():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.right = currentNode.left
                else:  # currentNode is the Root
                    currentNode.replaceNodeData(currentNode.left.cars,
                                                currentNode.left.left,
                                                currentNode.left.right)

            # Node has rightChild
            else:
                if currentNode.isLeftChild():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.left = currentNode.right
                elif currentNode.isRightChild():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.right = currentNode.right
                else:
                    currentNode.replaceNodeData(currentNode.right.cars,
                                                currentNode.right.left,
                                                currentNode.right.right)
