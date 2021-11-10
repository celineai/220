"""
Name: Celine Imani
lab11.py
"""
from random import *

def getWords(wordList):

    # Open the input file to be read.
    infile = open("list.txt", "r")

    words = []

    for line in infile:
        # get the words from each line
        words.append(line.strip())

    return words

def pickWord(words):
    # accepting the list
    list = getWords("list.txt")

    #generating a random number from 0 to the size of the list
    rand_Num = randint(0, len(list))

    #returning the the word from the list at the random number position

    return list[rand_Num]

def guessedWord(secret_Word, guessed_Letters, guessed_Word, letter):
    # always starting at false
    check = False

    # getting the length of the word
    for i in range(len(secret_Word)):
        # if getting a character correctly
        if letter == secret_Word[i]:
            guessed_Word[i] = letter
            check = True
        if check == True:
            return True
        # adding a letter to the guessed
        guessed_Letters.append(letter)
        return False

def wordSpelled(guessed_Word, secret_Word):
    if "".join(guessed_Word) == secret_Word:
        return True
    else:
        return False

def guessLetter(guessed_Letters, turn_Count, secret_Word, guessed_Word):
    letter = input("Enter a letter: ")
    # cap sensitive so lower it
    letter = letter.lower()
    check = False
    while check == False:
        check = True
        # avoid multiple letters
        if (len(letter) != 1):
            print("Please only put one letter.")
            letter = input("Guess a letter: ")
            check = False
    if guessed_Word(secret_Word, guessed_Letters, guessed_Word, turn_Count, letter):
        return True
    else:
        return False

# def printBoard(guessed_Word, turn_Count, guessed_Letters):
# design the board
def playGame():
    words = getWords("list.txt")
    secret_Word = pickWord(words)
    guessedWord = ["_"] * len(secret_Word)
    guessed_Letters = []
    turn_Count = 0

def main():

main()
