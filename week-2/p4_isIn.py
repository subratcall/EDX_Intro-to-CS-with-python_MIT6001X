"""
bisection search for a character within a string

inputs: 
 char = a single character
 aStr = a string in alphabetical order

outputs:
    True -> character was found in the string
    False-> desired character was not found in the string
"""

def isIn(char,aStr):
    l = len(aStr)
    if l <=1:
        return False
    else:
        m = int(len(aStr)/2)
        if char == aStr[m]:
            return True
        if char < aStr[m]:
            return isIn(char, aStr[:m])
        elif char > aStr[m]:
            return isIn(char, aStr[m:])
        else:
            return False
    #print(x)
    #print(m)
    #print(aStr[m])
print(isIn('c','abdqrsyz'))
print(int(1/2))