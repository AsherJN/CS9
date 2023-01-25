"""
Defines a Car class. This class will assume all Cars have a make(str),
model(str), year(int), and a price(int)
"""
class Car:
    def __init__(self, make, model, year, price):
        self.make = str(make.upper())
        self.model = str(model.upper())
        self.year = int(year)
        self.price = int(price)

    def __gt__(self, rhs):
        """
        comparator operator that allows us to check if a Car
        object is greater than another Car object. Car objects
        are first organized by the lexicographical/alphabetical
        order of their make attribute. If the make attribute is
        the same, then they’ll be determined by the lexicographical/alphabetical
        order of their model attribute. If the model attribute is the same,
        then they are organized by the year (from least-to-greatest). If the
        year is the same, then the they are organized by their price (from
        least-to-greatest)
        """
        if self.make > rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model > rhs.model:
                return True
            elif self.model == rhs.model:
                if self.year > rhs.year:
                    return True
                elif self.year == rhs.year:
                    if self.price > rhs.price:
                        return True
        return False

    def __lt__(self, rhs):
        """
        comparator operator that allows us to check that a Car object is
        less than another Car object via the operation Car1 < Car2 according
        to the specifications above.
        """
        if self.make < rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model < rhs.model:
                return True
            elif self.model == rhs.model:
                if self.year < rhs.year:
                    return True
                elif self.year == rhs.year:
                    if self.price < rhs.price:
                        return True
        return False

    def __eq__(self, rhs):
        """
        comparator operator that allows us to check that a Car object is
        equivalent to another Car (both cars have the same make, model,
        year, and price) via the operation Car1 == Car2
        """
        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    if self.price == rhs.price:
                        return True
        else:
            return False

    def __str__(self):
        """
        overload method that returns the details of a car via the operation
        str(Car1). The string representation should fit the format:
        "Make: [make], Model: [model], Year: [year], Price: $[price]"
        """
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: ${self.price}"

# c1 = Car(Tesla, Model3, 2016, 45000)
