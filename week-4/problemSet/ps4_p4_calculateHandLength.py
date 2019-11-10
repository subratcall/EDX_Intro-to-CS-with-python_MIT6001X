def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    count = 0
    for eachKey in hand.keys():
        count +=hand[eachKey]
    return count

hand = {'r': 2, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
handCount = calculateHandlen(hand)
print(handCount)
