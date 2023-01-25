#BookCollection.py
from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection():
    """
    The BookCollection will manage an Ordered Linked List containing
    BookCollectionNodes.The BookCollection class will be responsible
    for maintaining the overall structure of the Ordered Linked List.
    """
    #initializer
    def __init__(self):
        self.head = None

    #linked list methods
    def isEmpty(self):
        return self.head == None

    def getNumberOfBooks(self):
        temp = self.head
        count = 0
        while temp != None:
            count = count + 1
            temp = temp.getNext()
        return count

    def insertBook(self, book):
        #Basically add functionality in lecture
        current = self.head
        previous = None
        stop = False
        #Find the correct place in the list to add
        while current != None and not stop:
            #import pdb
            #pdb.set_trace()
            #Are authors equal?
            if current.getData() > book:
                stop = True
            #try next node
            else:
                previous = current
                current = current.getNext()

        #creates node
        temp = BookCollectionNode(book)
        #Case 1: insert at front of list
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        #Case 2: insert not at front of list
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def getBooksByAuthor(self, author):
        temp = self.head
        str = ''
        while temp != None:
            if temp.getData().getAuthor().upper() == author.upper():
                str += temp.getData().getBookDetails() + '\n'
                temp = temp.getNext()
            else:
                temp = temp.getNext()
        return str
    def getAllBooksInCollection(self):
        temp = self.head
        str = ''
        while temp != None:
            str += temp.getData().getBookDetails() + '\n'
            temp = temp.getNext()
        return str
    def removeAuthor(self, author):
        current = self.head

        #checks if empty list
        if current == None:
            return
        previous = None
        #goes through collection
        while current != None:
            if current.getData().getAuthor().upper() == author.upper():
                if previous == None:
                    self.head = current.getNext()
                    current = self.head
                if previous != None:
                    previous.setNext(current.getNext())
                    current = self.head
            #I guess there is a problem with these two line sof codes?
            #I dont really know, the TA isnt very helpful

            previous = current
            current = current.getNext()

    def index(self, item):
        current = self.head
        stop = False
        count = 0

        while current != None and not stop:
            if current.getData() == item:
                break
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
            count += 1
        return count



        ''' Stop Gap Solution in which will run method twice to get correct result'''
        '''
        current = self.head
        previous = None

        #checks if empty list
        if current == None:
            return None
        #goes through collection
        while current != None:
            if current.getData().getAuthor().upper() == author.upper():
                if previous == None:
                    self.head = current.getNext()
                if previous != None:
                    previous.setNext(current.getNext())
            #I guess there is a problem with these two line sof codes?
            #I dont really know, the TA isnt very helpful

            previous = current
            current = current.getNext()
    '''
    def recursiveSearchTitle(self, title, bookNode):
        "Searches Collection for book recursively (duh)"
        #base case
        if bookNode == None:
            return False
        elif bookNode.getData().getTitle().upper() == title.upper():
            return True
        else:
            return self.recursiveSearchTitle(title, bookNode.getNext())





# b0 = Book("Cujo", "King, Stephen", 1981)
# b1 = Book("The Shining", "King, Stephen", 1977)
# b2 = Book("Ready Player One", "Cline, Ernest", 2011)
# b3 = Book("Rage", "King, Stephen", 1977)

# b1 = Book("Green Eggs and Ham", "Dr. Suess", 1960)
# b2 = Book(1984, "Orwell, George", "1948")
# b3 = Book("CS9 Textbook", "Wang, Richert", 2022)
# b4 = Book("A Fake Book", "Orwell, George", 2001)
# b5 = Book("An Even Faker Book", "Orwell, George", 1948)
#
# bc = BookCollection()
#
# bc.insertBook(b1)
# bc.insertBook(b2)
# bc.insertBook(b3)
# bc.insertBook(b4)
# bc.insertBook(b5)
# #
# #print(bc.getAllBooksInCollection())
# #
# #print(bc.getBooksByAuthor('Orwell, George'))
#
# print(bc.recursiveSearchTitle('CS9 Textboo', bc.head))

# b1 = Book("Green Eggs and Ham", "Dr. Suess", 1960)
# b2 = Book(1984, "Orwell, George", "1948")
# b3 = Book("CS9 Textbook", "Wang, Richert", 2022)
# b4 = Book("A Fake Book", "Orwell, George", 2001)
# b5 = Book("An Even Faker Book", "Orwell, George", 1948)
# # creates book collection
# c1 = BookCollection()
# # tests if collection is empty
# assert c1.isEmpty() == True
# # inserts another book
# c1.insertBook(b1)
# # tests if collectionis empty
# assert c1.isEmpty() == False
# # tests how many books in collection
# assert c1.getNumberofBooks() == 1
# # inserts 4 more books
# c1.insertBook(b2)
# c1.insertBook(b3)
# c1.insertBook(b4)
# c1.insertBook(b5)
# # tests if colelction is empty
# assert c1.isEmpty() == False
#
# # tests how many books in collection
# assert c1.getNumberofBooks() == 5
#
# # tests if it can return books by author as string
# assert c1.getBooksByAuthor("Orwell, George") == "Title: A Fake Book, Author: Orwell, George, Year: 2001\nTitle: 1984, Author: Orwell, George, Year: 1948\nTitle: An Even Faker Book, Author: Orwell, George, Year: 1948\n"
#
# # tests if it can return all books from collection as a string
# assert c1.getAllBooksInCollection() == "Title: Green Eggs and Ham, Author: Dr. Suess, Year: 1960\nTitle: A Fake Book, Author: Orwell, George, Year: 2001\nTitle: 1984, Author: Orwell, George, Year: 1948\nTitle: An Even Faker Book, Author: Orwell, George, Year: 1948\nTitle: CS9 Textbook, Author: Wang, Richert, Year: 2022\n"
# print(c1.getAllBooksInCollection())
# # Tests recursive title search method
# assert c1.recursiveSearchTitle('CS9 Textbook', c1.head) == True
# assert c1.recursiveSearchTitle('1984', c1.head) == True
# assert c1.recursiveSearchTitle('None', c1.head) == False
#
# # tests whether an author can be removed
# c1.removeAuthor('Orwell, George')
#
# #print(c1.getAllBooksInCollection())
#
# assert c1.getAllBooksInCollection() == "Title: Green Eggs and Ham, Author: Dr. Suess, Year: 1960\nTitle: CS9 Textbook, Author: Wang, Richert, Year: 2022\n"
#
# # Tests recursive title search method
# assert c1.recursiveSearchTitle('1984', c1.head) == False
# assert c1.recursiveSearchTitle('A FAKE Book', c1.head) == False
# assert c1.recursiveSearchTitle('CS9 Textbook', c1.head) == True
