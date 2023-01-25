#testFile.py
from lab03 import *


def test_multiply():
    assert multiply(10, 10) == 100
    assert multiply(5, 11) == 55
    assert multiply(11, 5) == 55
    assert multiply(3168, 8) == 25344
    assert multiply(5, 2) == 10

def test_CollectMultiples():
    assert collectMultiples([2,6,3,8,9,3,46], 2) == [2, 6, 8, 46]
    assert collectMultiples([365, 76578, 1436, 8768, 342, 7668], 15) == []
    assert collectMultiples([1, 2, 4, 6, 8, 10], 12) == []
    assert collectMultiples([5, 5, 5, 5, 5], 5) == [5, 5, 5, 5, 5]
    assert collectMultiples([1], 5) == []

def test_CountVowels():
    assert countVowels("I love CS9 so much, its unbelievable!") == 12
    assert countVowels("WhAt ShOuLd I tAlK aBoUt?") == 8
    assert countVowels("...") == 0
    assert countVowels("") == 0
    assert countVowels("I'm not really sure lol") == 7

def test_reverseVowels():
    assert reverseVowels('poop') == 'oo'
    assert reverseVowels('Aaaaaaaaaa') == 'aaaaaaaaaA'
    assert reverseVowels(' W ') == ''
    assert reverseVowels('What do I even talk about?') == 'uoaaeeIoa'
    assert reverseVowels('Racecar racecaR') == 'aeaaea'

def test_removeSubString():
    assert removeSubString('CS9', 'CS9') == ''
    assert removeSubString('Isla Vista', 'is') == 'Isla Vta'
    assert removeSubString('Isla Vista', 'Is') == 'la Vista'
    assert removeSubString('Nothing should happen', ' ') == 'Nothingshouldhappen'
    assert removeSubString(' ', ' ') == ''
