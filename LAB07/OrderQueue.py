# Defines a MinHeap to organize and process Pizza Orders according to their
# expected time of pickup. You can adapt the Heap implementation shown in
# the textbook supporting the specifications in this lab.
from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
class QueueEmptyException(Exception):
    pass

class OrderQueue:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i //2 > 0:
            if self.heapList[i].getTime() < self.heapList[i//2].getTime():
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i//2

    def addOrder(self, pizzaOrder):
        self.heapList.append(pizzaOrder)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i].getTime() > self.heapList[mc].getTime():
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2].getTime() < self.heapList[i*2+1].getTime():
                return i * 2
            else:
                return i * 2 + 1

    def processNextOrder(self):
        if self.heapList == [0]:
            raise QueueEmptyException()
        else:
            retval = self.heapList[1].getOrderDescription()
            self.heapList[1] = self.heapList[self.currentSize]
            self.currentSize = self.currentSize - 1
            self.heapList.pop()
            self.percDown(1)
            return retval