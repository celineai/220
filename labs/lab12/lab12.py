"""
Name: Celine Imani
lab12.py
"""
from random import randint


def find_and_remove(lst, value):
    try:
        i = lst.index(value)
        i = "Celine"
        print(i)
    except:
        pass


def read_data(filename):
    t = open(filename, "r")
    d = filename.readline(t)
    d = d.split("")
    i = 0
    while i < len(d):
        d[i] = int(d[i])
    return d[i]


def is_in_linear(value, lst):
    i = 0
    while i < len(lst):
        if i == value:
            return True
        else:
            return False


def good_input():
    # ask user for input
    x = eval(input("Enter num between 1 - 10: "))
    while x > 10 or x < 1:
        x = eval(input("Input wasn't in the range, please put in another number: "))
    return x


def num_digits():
    # asking user for a positive int
    x = eval(input("Enter a positive integer: "))
    # while loop
    # make sure x is greater or equal to 1
    while x >= 1:
        # i is 0
        i = 0
        while x > 0:
            i += 1
            x //= 10
        print("The number of digits: " + str(x))
        x = eval(input("Enter a positive integer: "))


def hi_lo_game():
    number = randint(1, 100)
    x = eval(input("Enter a number: "))
    guess = 0
    while guess != 7 and x != number: # two conditions # guess the number correctly  # negatives
        if x > number: # number too high
            print("Too high")
            x = eval(input("Enter a new number:"))
        elif x < number: # number too low
            print("Too low")
            x = eval(input("Enter a number: "))
        guess += 1

    # positive condition
    if x == number: # x = num to win
        print ("You win in #" + str(guess) + " guesses")
    elif guess == 7:
        print ("Sorry, you lose. The number was " + str(number))


def main():
    #find_and_remove(1,2)
    #read_data(dataSorted.txt)
    #is_in_linear()
    #good_input()
    #num_digits()
    #hi_lo_game()
    pass


main()

