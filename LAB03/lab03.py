#lab03.py

"""
You will write five recursive functions for this lab.
"""

def multiply(x, y):
    """
    The parameters x and y are positive integers (including 0).
    This function recursively returns the product of x and y without
    explicitly multiplying the two numbers together.
    """
    #base case
    if y == 0:
        return 0
    return x + multiply(x, y-1)

def collectMultiples(intList, n):
    """
    The parameter intList contains a list of positive integers >= 1,
    and n is a positive integer >= 1. This function recursively returns a
    list containing elements in intList that are multiples of n in the
    order that they appear in intList. If there are no multiples of n in
    intList, then this function should return an empty list.
    """
    #base case
    if intList == []:
        return intList
    elif intList[0] % n == 0:

        return [intList[0]] + collectMultiples(intList[1:], n)
    else:
        return collectMultiples(intList[1:], n)



def countVowels(s):
    """
    This function will take a string value (s) and recursively return
    the number of vowels (‘A’,’E’,’I’,’O’,’U’,’a’,’e’,’i’,’o’,’u’) that
    exists in someString.
    """
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    #base case
    if s == '':
        return 0
    elif s[0] in vowels:
        return 1 + countVowels(s[1:])
    else:
        return countVowels(s[1:])

def reverseVowels(s):
    """
    This function will take a string value (s) and recursively return a
    string containing only the vowels (‘A’,’E’,’I’,’O’,’U’,’a’,’e’,’i’,’o’,’u’)
    in s in reverse order.
    """
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    #base case
    if s == '':
        return s
    elif s[-1] in vowels:
        return s[-1] + reverseVowels(s[:-1])
    else:
        return reverseVowels(s[:-1])

def removeSubString(s, sub):
    """
    The parameters s and sub are strings that contain at least one character.
    This function will recursively return a string where all occurrences of
    sub are removed in the order it appears in the string s (see example test
    below for an interesting case)
    """
    #base case
    if sub not in s:
        return s
    elif s[0:len(sub)] == sub:
        return removeSubString(s[len(sub):], sub)
    else:
        return s[0] + removeSubString(s[1:], sub)

