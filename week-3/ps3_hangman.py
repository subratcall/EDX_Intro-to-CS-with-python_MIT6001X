# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "C:/Users/gamad/Dropbox/school/Code/Python/EDX/wEEK 3/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    #word = 'test'
    #a = ['t', 'e', 'x', 's']
    #b = ['n', 'o']
    counter = 0
    for i in secretWord:
        if i in lettersGuessed:
            counter+=1
    if counter == len(secretWord):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    #word = 'testies'
    #l = ['e', 's', 't']
    for i in secretWord:
        if i not in lettersGuessed:
            secretWord = secretWord.replace(i,'_')
    #print(word
    return secretWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in lettersGuessed:
        if char in alphabet:
            alphabet = alphabet.replace(char, '')
    #print(alphabet)
    return alphabet

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    X At the start of the game, let the user know how many
      letters the secretWord contains.

    X Ask the user to supply one guess (i.e. letter) per round.

    X The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    X After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
            - getAvailableLetters
            -

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",len(secretWord),"letters long")
    print("-----------")
    lg = []
    guesses = 8
    while True:
        if isWordGuessed(secretWord,lg):
            print("Congratulations, you won!")
            break
        print("You have",guesses,"guesses left")
        print("Available Letters:",getAvailableLetters(lg))
        letter = input('Please guess a letter: ').lower()
        if len(letter)>1:
            print("Please only enter 1 letter.")
        elif letter in lg:
            print("Oops! You've already guessed that letter:",remaining_word)
        else:
            lg.append(letter)
            remaining_word = getGuessedWord(secretWord, lg)
            if letter in secretWord:
                print("Good guess:",remaining_word)
                #guesses-=1
            else:
                print("Oops! That letter is not in my word:",remaining_word)
                guesses-=1
        print("-----------")
        if guesses == 0:
            print("Sorry, you ran out of guesses. The word was ",secretWord+'.')
            break


#secretWord = chooseWord(wordlist)
secretWord = 'test'
hangman(secretWord)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
