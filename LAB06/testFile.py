from Apartment import Apartment
from lab06 import *
import pytest

def test_Apartment():
    a1 = Apartment(800, 300, "average")
    assert a1.getRent() == 800
    assert a1.getMetersFromUCSB() == 300
    assert a1.getCondition() == 'average'
    assert a1.getApartmentDetails() == 'Rent: $800, Distance From UCSB: 300m, Condition: average'

    a2 = Apartment("2000", "0", "bad")
    assert a2.getRent() == 2000
    assert a2.getMetersFromUCSB() == 0
    assert a2.getCondition() == 'bad'
    assert a2.getApartmentDetails() == 'Rent: $2000, Distance From UCSB: 0m, Condition: bad'

    assert (a1 < a2) == False
    assert (a2 < a1) == True
    assert (a1 > a2) == True
    assert (a2 > a1) == False


    a3 = Apartment(800, 300, "average")
    assert (a1 == a3) == True
    assert (a1 == a2) == False

def test_ensureSortedAscending():
    a1 = Apartment(800, 300, "average")
    a2 = Apartment("2000", "0", "bad")
    a3 = Apartment(800, 300, "excellent")

    apartmentList = [a1,a2,a3]

    assert ensureSortedAscending(apartmentList) == False

    newAptList = [a3, a1, a2]

    assert ensureSortedAscending(newAptList) == True

def test_mergesort():
    a1 = Apartment(800, 300, "average")
    a2 = Apartment("2000", "0", "bad")
    a3 = Apartment(800, 300, "excellent")
    a4 = Apartment(400, 100, "excellent")
    a5 = Apartment(1500, 200, "average")
    a6 = Apartment(1200, 50, "bad")
    a7 = Apartment(1200, 50, "average")
    a8 = Apartment(3000, 150, 'excellent')
    a9 = Apartment(900, 20, 'bad')
    a10 = Apartment('900', 30, 'average')

    apartmentList = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
    assert ensureSortedAscending(apartmentList) == False

    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True

def test_getBestApartment():
    a1 = Apartment(800, 300, "average")
    a2 = Apartment("2000", "0", "bad")
    a3 = Apartment(800, 300, "excellent")
    a4 = Apartment(400, 100, "excellent")
    a5 = Apartment(1500, 200, "average")
    a6 = Apartment(1200, 50, "bad")
    a7 = Apartment(1200, 50, "average")
    a8 = Apartment(3000, 150, 'excellent')
    a9 = Apartment(900, 20, 'bad')
    a10 = Apartment('900', 30, 'average')

    apartmentList = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]

    best_apt = getBestApartment(apartmentList)
    assert best_apt == a4.getApartmentDetails()

def test_getWorstapartment():
    a1 = Apartment(800, 300, "average")
    a2 = Apartment("2000", "0", "bad")
    a3 = Apartment(800, 300, "excellent")
    a4 = Apartment(400, 100, "excellent")
    a5 = Apartment(1500, 200, "average")
    a6 = Apartment(1200, 50, "bad")
    a7 = Apartment(1200, 50, "average")
    a8 = Apartment(3000, 150, 'excellent')
    a9 = Apartment(900, 20, 'bad')
    a10 = Apartment('900', 30, 'average')

    apartmentList = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
    worst_apt = getWorstApartment(apartmentList)
    assert worst_apt == a8.getApartmentDetails()

def test_getAffordableApartments():
    a1 = Apartment(800, 300, "average")
    a2 = Apartment("2000", "0", "bad")
    a3 = Apartment(800, 300, "excellent")
    a4 = Apartment(400, 100, "excellent")
    a5 = Apartment(1500, 200, "average")
    a6 = Apartment(1200, 50, "bad")
    a7 = Apartment(1200, 50, "average")
    a8 = Apartment(3000, 150, 'excellent')
    a9 = Apartment(900, 20, 'bad')
    a10 = Apartment('900', 30, 'average')

    apartmentList = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
    BudgetList = getAffordableApartments(apartmentList, 1200)
    assert BudgetList == 'Rent: $400, Distance From UCSB: 100m, Condition: excellent\nRent: $800, Distance From UCSB: 300m, Condition: excellent\nRent: $800, Distance From UCSB: 300m, Condition: average\nRent: $900, Distance From UCSB: 20m, Condition: bad\nRent: $900, Distance From UCSB: 30m, Condition: average\nRent: $1200, Distance From UCSB: 50m, Condition: average\nRent: $1200, Distance From UCSB: 50m, Condition: bad\n'

    apartmentList = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
    BudgetList = getAffordableApartments(apartmentList, 0)
    assert BudgetList == ''

    apartmentList = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
    BudgetList = getAffordableApartments(apartmentList, 799)
    assert BudgetList == 'Rent: $400, Distance From UCSB: 100m, Condition: excellent\n'