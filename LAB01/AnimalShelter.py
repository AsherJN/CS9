from Animal import Animal

class AnimalShelter:
    """
    Object will contain a dictionary structure where the keys of the dictionary
    will be a str type representing an Animal’s species (all upper-case characters)
    """

    def __init__(self):
        self.AnimalShelter = {}

    def addAnimal(self, animal):
        """
        Adds an Animal object (animal) to the AnimalShelter
        """
        try:
            if self.AnimalShelter.get(animal.getSpecies()) == None:
                self.AnimalShelter[animal.getSpecies()] = [animal]
            elif animal not in self.AnimalShelter.get(animal.getSpecies()):
                self.AnimalShelter[animal.getSpecies()].append(animal)
        except Exception:
            return None
        # if animal.getSpecies not in self.AnimalShelter:
        #     self.AnimalShelter[animal.getSpecies] = []
        #     self.AnimalShelter[animal.getSpecies] += [animal]
        #     #self.AnimalShelter[animal.getSpecies] = animal
        # else:
        #     #print("bye")
        #     self.AnimalShelter[animal.getSpecies] += [animal]

    def removeAnimal(self, animal):
        """
        Removes an Animal object (animal) from the AnimalShelter if it exists
        """
        if animal in self.AnimalShelter.get(animal.getSpecies()):
            self.AnimalShelter[animal.getSpecies()].remove(animal)
        # for value in self.AnimalShelter.values():
        #     if value == animal:
        #         del value
        #     else:
        #         continue

    def removeSpecies(self, species):
        """
        Removes all animals of a certain species from the AnimalShelter if it exists.
        """
        # if species == None:
        #     return None
        #if species.upper() in self.AnimalShelter:
        try:
            del self.AnimalShelter[species.upper()]
        except Exception:
            try:
                del self.AnimalShelter[species]
            except Exception:
                return None
        # for key in self.AnimalShelter.keys():
        #     if key == species:
        #         del key
        #     else:
        #         continue

    def getAnimalsBySpecies(self, species):
        """
        Returns a string of all animals of a certain species.
        """
        string = []
        #count = len(self.AnimalShelter.get(species.upper()))
        #if species in self.AnimalShelter:
        try:
            for value in self.AnimalShelter.get(species.upper()):
                    string.append(value.toString())
                    #string += '\n'
                    #count -= 1
                #print('True')
        except Exception:
            return ''
        # else:
        #     print("False")
        return '\n'.join(string)
        #return string

    def doesAnimalExist(self, animal):

        """
        Returns True if the parameter animal (with matching species, name, age, and weight)
        exists in the AnimalShelter. Returns False otherwise.
        """
        try:
            if animal in self.AnimalShelter.get(animal.getSpecies()):
                return True
            else:
                return False
        except Exception:
            return False
        # for value in self.AnimalShelter.values():
        #     if value == animal:
        #         return True
        #     else:
        #         continue
        # return False

# c = Animal('Dog', 12, 4, "Poop")
# a = Animal("Dog", 14, 5, "Rodney")
# b = Animal("Cat", 20, 20, "Cunt")
# print(c.toString())
#
# print()
#
# dict = AnimalShelter()
#
# dict.addAnimal(c)



# dict.getAnimalsBySpecies('Dog')
'''
'''
# c = Animal('Dog', 12, 4, "Poop")
# a = Animal("Dog", 14, 5, "Rodney")
# b = Animal("Cat", 20, 20, "Cunt")
# d = Animal('Dog', 13, 4, "Poop")
# n = Animal()
# dict = AnimalShelter()
# dict.addAnimal(c)
# dict.addAnimal(a)
# dict.addAnimal(b)
# dict.addAnimal(n)
# print(dict.getAnimalsBySpecies('dog'))
#
# print(dict.doesAnimalExist(c))
#
# #dict.removeAnimal(b)
#
# dict.removeSpecies(None)
#
# print(dict.getAnimalsBySpecies('CAT'))

# assert dict.doesAnimalExist('Poop') == True
# assert dict.doesAnimalExist('Roop') == False

