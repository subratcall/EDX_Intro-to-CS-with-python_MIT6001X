# finding the greatest common denominator with Recursion
def gcdRecur(a, b):
    #gcd = 0
    if a>b:
        small = b
        large = a
    else:
        small = a
        large = b
    m = large%small
    if m == 0:
        return small
    else:
        return gcdRecur(small,m)
print(gcdRecur(1071,462))
#print(round(1/2))




