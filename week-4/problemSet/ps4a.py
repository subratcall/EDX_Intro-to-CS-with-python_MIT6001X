# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

#WORDLIST_FILENAME = "C:/Users/djgama/Dropbox/Online_courses/Edx-intro_to_cs_w_python_MIT6001x/week-4/problemSet/words.txt"
WORDLIST_FILENAME = "C:/Users/gamad/Dropbox/Online_courses/Edx-intro_to_cs_w_python_MIT6001x/week-4/problemSet/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

# (end of helper code)
# -----------------------------------
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
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

def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3

    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # make a copy of hand, so as to not mutate the original dictionary
    h2 = hand.copy()
    # find the letters of 'word' within h2 and remove them
    for char in word:
        h2[char] = h2.get(char, 0)-1
    # return the new hand
    return h2

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """

    """
    Make sure the word provided is in the wordList.
    """
    if word in wordList:
        """
        Run through each letter in 'word'.

        If the letter does not exist, hcpy.get(char) returns a 'None' value, wherein we print to the user
        --> that the word is not playable because you don't have the correct letters in your hand.

        If we do not have enough letters in our hand to qualify the word, we print to the user that this word
        --> is not usable because they ran out of letters in their hand to use the word.
        """
        hcpy = hand.copy()
        for char in word:
            z = hcpy.get(char)
            if z == None:
                #print("The letter",char,"does not exist in your hand. You cannot use this word.")
                return False
            elif z >=1:
                hcpy[char] = hcpy.get(char)-1
            else:
                #print('not enough letters in your hand for this letter')
                return False
        return True
    else:
        #return word+" not in wordlist"
        return False

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

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    # Keep track of the total score
    hz = n
    tScore = 0
    # As long as there are still letters left in the hand:
    while n !=0:
        # Display the hand
        displayHand(hand)
        # Ask user for input
        word = input('Enter word, or a "." to indicate that you are finished: ')
        # If the input is a single period:
        if word == '.':
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(word, hand, wordList):
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again.")
                print("")
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score = getWordScore(word,hz)
                tScore +=score
                print(word,"earned",score,"points. Total:",tScore)
                print(" ")
                # Update the hand
                hand = updateHand(hand,word)
                n = calculateHandlen(hand)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print("Total score:",tScore,"points.")

#
# Problem #5: Playing a game
#

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1
    """
    while True:
        pIn = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if pIn == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand,wordList,HAND_SIZE)
        elif pIn == 'r':
            try:
                playHand(hand,wordList,HAND_SIZE)
            except:
                print("You have not played a hand yet. Please play a new hand first!")
        elif pIn =='e':
            break
        else:
            print("Invalid command.")
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
