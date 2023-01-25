#Book.py
#from BookCollectionNode import *
class Book():
    """
    Definition of a Book
    title - str that represents the title of the Book
    author - str that represents the author of the Book. This will be in a LastName,
             FirstName format. You may assume this will always be the case
    year - int that represents the year the Book was published
    """
    def __init__(self, title='', author='', year=None):
        #add conditions
        self.title = str(title)
        self.author = str(author)
        if year == None:
            self.year = None
        else:
            self.year = int(year)

    #getter methods
    def getTitle(self):
        return self.title
    def getAuthor(self):
        return self.author
    def getYear(self):
        return self.year
    #str method
    def getBookDetails(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

    #greater than equality operator
    def __gt__(self, rh):
        #are authors the same?
        if self.author.upper() == rh.author.upper():
            #are the years the same?
            if self.year == rh.year:
                for char in range(len(self.title)):
                    #if the letters are NOT equal...
                    if self.title[char].upper() != rh.title[char].upper():
                        #return boolean expression
                        ''''''
                        return self.title[char].upper() > rh.title[char].upper()
                    else:
                        continue
                return False
            else:
                #return boolean expression
                return self.year > rh.year
        else:
            for char in range(len(self.author)):
                # if the letters are NOT equal...
                if self.author[char].upper() != rh.author[char].upper():
                    # return boolean expression
                    ''''''
                    return self.author[char].upper() > rh.author[char].upper()
                else:
                    continue
            return False
#
#
#
#
#
#
# # b1 = Book("Green Eggs and Ham", "Dr. Suess", 1960)
# # print(b1.getTitle())

# Test Failed: "Title: The Deathly Hallows, Author: Rowling, J.K., Y[602 chars]54\n" != "Title: The Philosopher's Stone, Author: Rowling, J.K[602 chars]55\n"
# Diff is 1139 characters long. Set self.maxDiff to None to see it.