from Apartment import Apartment

def mergesort(apartmentList):
    """
    Performs a mergesort on the apartmentList passed as input.
    Sorts the Apartment objects based on the specifications in
    the Introduction section of this lab. Gradescope will test
    to ensure that your mergesort implementation’s Big-O is O(NlogN).
    """
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
        left_half = apartmentList[:mid]
        right_half = apartmentList[mid:]

        mergesort(left_half)
        mergesort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if (left_half[i] < right_half[j]) or (left_half[i] == right_half[i]):
                apartmentList[k] = left_half[i]
                i += 1
            else:
                apartmentList[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            apartmentList[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            apartmentList[k] = right_half[j]
            j += 1
            k += 1





def ensureSortedAscending(apartmentList):
    """
    Method that returns a boolean value. True if the apartmentList is
    sorted correctly in asending order. False otherwise.
    """
    for apartment in range(len(apartmentList)):
        try:
            if apartmentList[apartment] > apartmentList[apartment + 1]:
                return False
        except Exception:
            break
    return True

def getBestApartment(apartmentList):
    """
    Method that returns a string detailing the best Apartment’s rent,
    meters from UCSB, and condition. Make use of getApartmentDetails(self)
    and mergesort(apartmentList). You can assume that apartmentList has at
    least one apartment.
    """
    mergesort(apartmentList)
    return '(Apartment) ' + apartmentList[0].getApartmentDetails()


def getWorstApartment(apartmentList):
    """
    Method that returns a string detailing the worst Apartment’s rent,
    meters from UCSB, and condition. Make use of getApartmentDetails(self)
    and mergesort(apartmentList). You can assume that apartmentList has at
    least one apartment.
    """
    mergesort(apartmentList)
    return '(Apartment) ' + apartmentList[-1].getApartmentDetails()

def getAffordableApartments(apartmentList, budget):
    """
    Method that returns a labeled, newline separated string detailing the rent,
    meters from UCSB, and condition of all the apartments whose rent is less
    than or equal to budget from the apartmentList in sorted order. Make use
    of getApartmentDetails(self) and mergesort(apartmentList). You can assume
    that apartmentList has at least one apartment and that there is no newline
    at the end of the string returned by this method. If there are no apartments
    that are affordable in the apartmentList, this method returns an empty string.
    """
    mergesort(apartmentList)
    temp = ''
    tempAptList = apartmentList
    for apartment in tempAptList:
        if apartment.getRent() > budget:
            break
        elif apartment == tempAptList[0]:
            temp += '(Apartment) ' + apartment.getApartmentDetails()
        else:
            temp += '\n' + '(Apartment) ' + apartment.getApartmentDetails()

    return temp

# a1 = Apartment(800, 300, "average")
# a2 = Apartment("2000", "0", "bad")
# a3 = Apartment(800, 300, "excellent")
# apartmentList = [a1, a2, a3]
# temp = ''
#
# for apartment in apartmentList:
#     temp += apartment.getApartmentDetails() + '\n'
# print(temp)
#
# temp = ''
# mergesort(apartmentList)
#
# for apartment in apartmentList:
#     temp += apartment.getApartmentDetails() + '\n'
# print(temp)

# a1 = Apartment(800, 300, "average")
# a2 = Apartment("2000", "0", "bad")
# a3 = Apartment(800, 300, "excellent")
# a4 = Apartment(400, 100, "excellent")
# a5 = Apartment(1500, 200, "average")
# a6 = Apartment(1200, 50, "bad")
# a7 = Apartment(1200, 50, "average")
# a8 = Apartment(3000, 150, 'excellent')
# a9 = Apartment(900, 20, 'bad')
# a10 = Apartment('900', 30, 'average')
#
# apartmentList = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
#
# BudgetList = getAffordableApartments(apartmentList, 1200)
#
# print(BudgetList)