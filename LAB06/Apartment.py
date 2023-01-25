class Apartment():
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = int(rent)
        self.metersFromUCSB = int(metersFromUCSB)
        self.condition = str(condition)

    #getter methods
    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return f"Rent: ${self.rent}, Distance From UCSB: {self.metersFromUCSB}m, Condition: {self.condition}"

    #overloaded methods
    '''
    You have decided to sort Apartments as follows. First, you will organize 
    the Apartment by increasing rent. In the event of a tie (several Apartments 
    have the same rent), the meters from UCSB will be used to determine the 
    Apartment’s place in the list. The closer the apartment is to campus, 
    the better. If the rent and the meters from campus are the same, then 
    the Apartment’s condition will be used to determine the Apartment’s 
    place in the list. An apartment can have either a "bad", "average", 
    or "excellent" condition - the better the condition is, the better the 
    apartment. You may assume that apartment objects will have either "bad", 
    "average", or "excellent" as their condition when comparing / sorting 
    apartments.
    '''
    def __lt__(self, rhs):

        if self.getRent() != rhs.getRent():
            return self.getRent() < rhs.getRent()
        elif self.getMetersFromUCSB() != rhs.getMetersFromUCSB():
            return self.getMetersFromUCSB() < rhs.getMetersFromUCSB()
        elif self.getCondition() != rhs.getCondition():
            conditionList = ['bad', 'average', 'excellent']

            index = 0
            selfTemp = 0
            for rating in conditionList:
                if self.getCondition() == rating:
                    selfTemp = index
                else:
                    index += 1

            index = 0
            rhsTemp = 0
            for secondRating in conditionList:
                if rhs.getCondition() == secondRating:
                    rhsTemp = index
                else:
                    index += 1
            return selfTemp > rhsTemp
        return False

    def __gt__(self, rhs):
        if self.getRent() != rhs.getRent():
            return self.getRent() > rhs.getRent()
        elif self.getMetersFromUCSB() != rhs.getMetersFromUCSB():
            return self.getMetersFromUCSB() > rhs.getMetersFromUCSB()
        elif self.getCondition() != rhs.getCondition():
            conditionList = ['bad', 'average', 'excellent']

            index = 0
            selfTemp = 0
            for rating in conditionList:
                if self.getCondition() == rating:
                    selfTemp = index
                    break
                else:
                    index += 1

            index = 0
            rhsTemp = 0
            for secondRating in conditionList:
                if rhs.getCondition() == secondRating:
                    rhsTemp = index
                    break
                else:
                    index += 1

            return selfTemp < rhsTemp
        return False

    def __eq__(self, rhs):
        if self.getRent() == rhs.getRent():
            if self.getMetersFromUCSB() == rhs.getMetersFromUCSB():
                return self.getCondition() == rhs.getCondition()
        return False


# a1 = Apartment(800, 300, "average")
# a2 = Apartment("2000", "0", "bad")
# a3 = Apartment("2000", "0", "excellent")
#
# print(a1 < a2)
# print(a2 < a3)