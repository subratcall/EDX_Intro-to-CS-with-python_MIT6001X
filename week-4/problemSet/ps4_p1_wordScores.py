VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 5

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def getWordScore(word, n):
    # find each letter in a word within SCRABBLE_LETTER_VALUES and sum values
    score = 0
    for char in word:
        score+=SCRABBLE_LETTER_VALUES.get(char)

    # add up the values and multiply by the letter size
    score*=len(word)

    # If the word size if the same as HAND_SIZE, add an additional 50 points
    if n == len(word):
        score+=50

    # return the score
    return score

'''
h: 4
e: 1
l: 1
l: 1
o: 1
'''
x = getWordScore('hello', HAND_SIZE)
print(x)
