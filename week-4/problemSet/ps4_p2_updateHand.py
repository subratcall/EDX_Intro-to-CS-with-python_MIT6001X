#from ps4a import updateHand
def updateHand(hand, word):
    # make a copy of hand, so as to not mutate the original dictionary
    h2 = hand.copy()
    # find the letters of 'word' within h2 and remove them
    for char in word:
        h2[char] = h2.get(char, 0)-1
    # return the new hand
    return h2

def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line



hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
x = updateHand(hand, 'quail')
displayHand(x)
