"""
Defines a BST Node class containing all fields for a BST Node and
a Python List collection of Car objects.
"""
class CarInventoryNode:
    def __init__(self, car):
        self.cars = []
        self.cars.append(car)
        self.make = str(car.make.upper())
        self.model = str(car.model.upper())
        self.parent = None
        self.right = None
        self.left = None

    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getParent(self):
        if self.parent:
            return self.parent
        return None
    def setParent(self, parent):
        self.parent = parent
    def getLeft(self):
        if self.left:
            return self.left
        return None
    def setLeft(self, left):
        self.left = left
    def getRight(self):
        if self.right:
            return self.right
        return None
    def setRight(self, right):
        self.right = right
    def __str__(self):
        str = ''
        for node in self.cars:
            str += node.__str__() + '\n'
        return str

    # def __eq__(self, rhs):
    #     if self.make == rhs.make:
    #         if self.model == rhs.model:
    #             return True
    #     else:
    #         return False

####################################################################
####################################################################

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def replaceNodeData(self,cars,left,right):
        self.cars = cars
        self.left = left
        self.right = right
        if self.hasLeftChild():
            self.left.parent = self
        if self.hasRightChild():
            self.right.parent = self

    def getSuccessor(self, make, model):
        succ = None
        # Check if node has a right subtree...
        if self.hasRightChild():
            # traverse through left children (min)
            succ = self.right.findMin()
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.left
        return current

    def spliceOut(self):
        # Case 1:
        # If node to be removed is a leaf, set parent's left or right
        # child references to None
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None

        # Case 2:
        # Not a leaf node. Should only have a right child for BST
        # removal
        elif self.hasAnyChildren():
            if self.hasRightChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.right
                else:
                    self.parent.rightChild = self.right
                self.right.parent = self.parent
