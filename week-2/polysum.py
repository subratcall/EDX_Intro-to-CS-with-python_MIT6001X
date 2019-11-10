"""
polysum inputs:
    n: polygon number of sides
    s: length of each side
    
    plysum finds the sum of the area and square of the perimeter of a polygon and returns it
"""
import math

def polysum(n,s):
    
    area = (.25*n*(s*s))
    area = area/math.tan(math.pi/n)
    
    per = n*s
    
    ans = area+(per*per)
    return round(ans,4)
#print(polysum(4,1))