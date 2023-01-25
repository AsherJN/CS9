#BookCollectionNode.py
#from Book import *
class BookCollectionNode():
    """
    Similar to the Linked List Node implementation done in lecture
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    #getter methods
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    #setter methods
    def setData(self, newData):
        self.data = newData
    def setNext(self, newNext):
        self.next = newNext
