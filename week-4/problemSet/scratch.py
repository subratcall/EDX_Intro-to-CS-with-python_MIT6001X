from ps4a import *
wordlist = loadWords()

def isValidWord(word, hand, wordList):
    hcpy = hand.copy()

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
        for char in word:
            z = hcpy.get(char)
            if z == None:
                print("The letter",char,"does not exist in your hand. You cannot use this word.")
                return False
            elif z >=1:
                hcpy[char] = hcpy.get(char)-1
            else:
                print('not enough letters in your hand for this letter')
                return False
        return True
    else:
        return word+" not in wordlist"
#print(hand)
#print("enter a valid word, composed of the available letters in your hand")
#x = input()

hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
word = "raasdfsd"
#word = "test"
#word = 'z'
y = isValidWord(word, hand, wordlist)
print(y)
