"""
Name: Celine Imani
lab7.py
"""
import math

def cash_conversion():
    # first we have to ask the user the interger
    x = eval(input('Please insert an integer:  '))
    # then we convert it
    print('$' + '{:.2f}'.format(x))

def encode():
    # ask the user for the message being coded
    message = input('Please insert a message to be encoded: ')
    # asking for the numerical value
    key = eval(input('Please insert a key: '))
    # the accumulation
    acc = ""
    for c in message:
        x = ord(c)
        #shift x by the key
        ch = (x + key)
        ac = chr(ch)
        #add the new character to your acc
        acc = acc + ac
    print(acc)

def sphere_area(radius):
     a = 4 * (3.14) * (radius ** 2)
     return a

def sphere_volume(radius):
    v = ( 4 / 3) * 3.14 * (radius ** 3)
    return v

def sum_n(n):
    acc = 0
    for i in range(n):
        #add i to n
        sum = i + n
        # add the sum to the accumulator
        acc = acc + sum
        #we return the statement
        return acc

def sum_n_cubes(n):
    #instead of adding i to accumulator it'll be i * 3
    acc = 0
    for i in range(n):
        sum = i * 3
        acc = acc + sum
        return acc

def encode_better():
    # ask the user for the message being coded
    message = input('Please insert a message to be encoded: ')
    # asking for the numerical value
    k = input('Please insert a key: ')
    # the accumulation
    acc = ""
    for i in range(len(message)):
        c = message[i]
        key = k[i % len(k)]

        key = (ord(key) - 97)

        # shift c by the key
        ch = (ord(c) + key)

        # convert c back to a chr
        c = chr(ch)

        # add c to the acc
        acc = acc + c
    print(acc)

def main():
    #cash_conversion()
    #encode()
    #print(sphere_area())
    #print(sphere_volume())
    #print(sum_n())
    #print(sum_n_cubes())
    #encode_better()
    pass


main()
