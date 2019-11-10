def build_shift_dict(shift):
    '''
    shift (integer): the amount by which to shift every letter of the
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to
             another letter (string).
    '''
    import string
    lc_str = string.ascii_lowercase
    #print(lc)
    uc_str = string.ascii_uppercase
    #print(uc)

    '''
    -Create empty dictionaries for uppercase and lowercase values
    -insert original alphabet values as keys and the index+2 value as the key
    -if index + character shift is greater than 25, mod the number to begin at the beginning of the string once again
    '''
    lc_dict = {}
    uc_dict = {}

    for c1 in lc_str:
        c2 = c1.upper()
        if lc_str.index(c1)+shift>25:
            lc_dict[c1] = lc_str[(lc_str.index(c1)+shift)%len(lc_str)]
            uc_dict[c2] = uc_str[(uc_str.index(c2)+shift)%len(uc_str)]
        else:
            lc_dict[c1] = lc_str[(lc_str.index(c1)+shift)]
            uc_dict[c2] = uc_str[(uc_str.index(c2)+shift)]

    return {**lc_dict,**uc_dict}
#cipher_dict = build_shift_dict(1)


x = 'hello'
shift = 0
cipher_dict = build_shift_dict(shift)
new_str = ''
for char in x:
    if char not in cipher_dict.keys():
        new_str+=char
    else:
        new_str+=(cipher_dict[char])

print(new_str)
