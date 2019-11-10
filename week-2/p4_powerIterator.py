def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    t = base
    if exp == 0:
        return 1
    else:
        while exp-1>0:
            t*=base
            exp-=1 
        return t 

