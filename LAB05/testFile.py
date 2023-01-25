#testFile.py
from Book import Book
from BookCollectionNode import BookCollectionNode
from BookCollection import BookCollection

def test_Book():
    b1 = Book("Green Eggs and Ham", "Dr. Suess", 1960)
    assert b1.getTitle() == "Green Eggs and Ham"
    assert b1.getAuthor() == "Dr. Suess"
    assert b1.getYear() == 1960
    assert b1.getBookDetails() == "Title: Green Eggs and Ham, Author: Dr. Suess, Year: 1960"

    b2 = Book(1984, "Orwell, George", "1948")
    assert b2.getTitle() == "1984"
    assert b2.getAuthor() == "Orwell, George"
    assert b2.getYear() == 1948
    assert b2.getBookDetails() == "Title: 1984, Author: Orwell, George, Year: 1948"

    assert (b1 > b2) == False

test_Book()

def test_BookCollectionNode():
    b1 = Book("Green Eggs and Ham", "Dr. Suess", 1960)
    n1 = BookCollectionNode(b1)
    assert n1.getData() == b1
    assert n1.getNext() == None

    b2 = Book(1984, "Orwell, George", "1948")
    n1.setData(b2)
    assert n1.getData() == b2
    b3 = Book("CS9 Textbook", "Wang, Richert", 2022)
    n2 = BookCollectionNode(b3)
    n1.setNext(n2)
    assert n1.getNext() == n2


def test_BookCollection():
    b1 = Book("Green Eggs and Ham", "Dr. Suess", 1960)
    b2 = Book(1984, "Orwell, George", "1948")
    b3 = Book("CS9 Textbook", "Wang, Richert", 2022)
    b4 = Book("A Fake Book", "Orwell, George", 2001)
    b5 = Book("An Even Faker Book", "Orwell, George", 1948)
    #creates book collection
    c1 = BookCollection()
    #tests if collection is empty
    assert c1.isEmpty() == True
    #inserts another book
    c1.insertBook(b1)
    #tests if collectionis empty
    assert c1.isEmpty() == False
    #tests how many books in collection
    assert c1.getNumberOfBooks() == 1
    #inserts 4 more books
    c1.insertBook(b2)
    c1.insertBook(b3)
    c1.insertBook(b4)
    c1.insertBook(b5)
    #tests if colelction is empty
    assert c1.isEmpty() == False

    #tests how many books in collection
    assert c1.getNumberOfBooks() == 5

    #tests if it can return books by author as string
    assert c1.getBooksByAuthor("Orwell, George") =="Title: 1984, Author: Orwell, George, Year: 1948\nTitle: An Even Faker Book, Author: Orwell, George, Year: 1948\nTitle: A Fake Book, Author: Orwell, George, Year: 2001\n"

    #tests if it can return all books from collection as a string
    assert c1.getAllBooksInCollection() == 'Title: Green Eggs and Ham, Author: Dr. Suess, Year: 1960\nTitle: 1984, Author: Orwell, George, Year: 1948\nTitle: An Even Faker Book, Author: Orwell, George, Year: 1948\nTitle: A Fake Book, Author: Orwell, George, Year: 2001\nTitle: CS9 Textbook, Author: Wang, Richert, Year: 2022\n'

    #Tests recursive title search method
    assert c1.recursiveSearchTitle('CS9 Textbook', c1.head) == True
    assert c1.recursiveSearchTitle('1984', c1.head) == True
    assert c1.recursiveSearchTitle('None', c1.head) == False

    #tests whether an author can be removed
    c1.removeAuthor('Orwell, George')
    assert c1.getAllBooksInCollection() == "Title: Green Eggs and Ham, Author: Dr. Suess, Year: 1960\nTitle: CS9 Textbook, Author: Wang, Richert, Year: 2022\n"

    #Tests recursive title search method
    assert c1.recursiveSearchTitle('1984', c1.head) == False
    assert c1.recursiveSearchTitle('A Fake Book', c1.head) == False
    assert c1.recursiveSearchTitle('CS9 Textbook', c1.head) == True

def test_BookEQ():
    b1 = Book("The Philosopher's Stone", "Rowling, J.K.", 1997)
    b2 = Book("The Deathly Hallows", "Rowling, J.K.", 2007)

    assert b2 > b1

def test_removeAuthor():
    b1 = Book("Green Eggs and Ham", "Dr. Suess", 1960)
    b2 = Book(1984, "Orwell, George", "1948")
    b3 = Book("CS9 Textbook", "Wang, Richert", 2022)
    b4 = Book("A Fake Book", "Orwell, George", 2001)
    b5 = Book("An Even Faker Book", "Orwell, George", 1948)
    b6 = Book("The Philosopher's Stone", "Rowling, J.K.", 1997)
    b7 = Book("The Deathly Hallows", "Rowling, J.K.", 2007)

    c1 = BookCollection()
    c1.insertBook(b1)
    c1.insertBook(b2)
    c1.insertBook(b3)
    c1.insertBook(b4)
    c1.insertBook(b5)
    c1.insertBook(b6)
    c1.insertBook(b7)

    c1.removeAuthor('Rowling, J.K.')
    #print(c1.getAllBooksInCollection())
    assert c1.getAllBooksInCollection() == "Title: Green Eggs and Ham, Author: Dr. Suess, Year: 1960\nTitle: 1984, Author: Orwell, George, Year: 1948\nTitle: An Even Faker Book, Author: Orwell, George, Year: 1948\nTitle: A Fake Book, Author: Orwell, George, Year: 2001\nTitle: CS9 Textbook, Author: Wang, Richert, Year: 2022\n"
    #print(c1.getAllBooksInCollection())
    c1.removeAuthor('Orwell, George')
    assert c1.getAllBooksInCollection() == "Title: Green Eggs and Ham, Author: Dr. Suess, Year: 1960\nTitle: CS9 Textbook, Author: Wang, Richert, Year: 2022\n"
    c1.removeAuthor("Dr.Suess")
    assert c1.getAllBooksInCollection() == "Title: CS9 Textbook, Author: Wang, Richert, Year: 2022\n"

def test_index():
    b1 = Book("Green Eggs and Ham", "Dr. Suess", 1960)
    b2 = Book(1984, "Orwell, George", "1948")
    b3 = Book("CS9 Textbook", "Wang, Richert", 2022)
    b4 = Book("A Fake Book", "Orwell, George", 2001)
    b5 = Book("An Even Faker Book", "Orwell, George", 1948)
    b6 = Book("The Philosopher's Stone", "Rowling, J.K.", 1997)
    b7 = Book("The Deathly Hallows", "Rowling, J.K.", 2007)

    c1 = BookCollection()
    c1.insertBook(b1)
    c1.insertBook(b2)
    c1.insertBook(b3)
    c1.insertBook(b4)
    c1.insertBook(b5)
    c1.insertBook(b6)
    c1.insertBook(b7)

    assert c1.index(b3) == 6



