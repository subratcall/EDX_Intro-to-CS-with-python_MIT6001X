def gcdIter(a, b):
    #gcd = 0
    if a>b:
        small = b
        large = a
    else:
        small = a
        large = b
    
    if large%small == 0:
        gcd = small
    else:    
        for i in range(1,round(small/2)):
            if small%i == 0 and large%i ==0:
                gcd = i
    return gcd
print(gcdIter(49,7))
#print(round(1/2))