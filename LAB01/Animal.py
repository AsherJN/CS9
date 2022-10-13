class Animal:

    # Constructor
    def __init__(self, species=None, weight=None, age=None, name=None):
        self.species = species
        self.weight = weight
        self.age = age
        self.name = name

        if self.species != None:
            self.species = str(species.upper())
        if self.weight != None:
            self.weight = float(weight)
        if self.age != None:
            self.age = int(age)
        if self.name != None:
            self.name = str(name.upper())

    # Setter Functions
    def setSpecies(self, species):
        if self.species != None:
            self.species = str(species.upper())
    def setWeight(self, weight):
        if self.weight != None:
            self.weight = float(weight)
    def setAge(self, age):
        if self.age != None:
            self.age = int(age)
    def setName(self, name):
        if self.name != None:
            self.name = str(name.upper())

    # def setSpecies(self, species):
    #     self.species = str(species.upper())
    # def setWeight(self, weight):
    #     self.weight = float(weight)
    # def setAge(self, age):
    #     self.age = int(age)
    # def setName(self, name):
    #     self.name = str(name.upper())

    # Print Attributes function
    def toString(self):
        return f"Species: {self.species}, Name: {self.name}, Age: {self.age}, Weight: {self.weight}"

    # Getter Functions
    def getSpecies(self):
        return self.species
    def getWeight(self):
        return self.weight
    def getAge(self):
        return self.age
    def getName(self):
        return self.name


    # String Method
    def __str__(self):
        return f"Species: {self.species}, Name: {self.name}, Age: {self.age}, Weight: {self.weight}"



# c = Animal('Dog', 12, 4, "Poop")
# #
# print(c)
#
# print(c.getSpecies())
#
# p = Animal('Dog')
#
# print(p)