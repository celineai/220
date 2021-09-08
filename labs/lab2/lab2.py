import math
"""
Name: Celine Imani
lab2.py
"""


def sum_of_three():
    bound = eval(input("Enter the upperbound: "))
    total = 0
    for total in range(0, bound + 1, 3):
        print(total)


#sum_of_three()

def multiplication_table():
    for h in range(1, 11):
        for l in range(1, 11):
            print(h * l, end=" ")
        print()

#multiplication_table()

def triangle_area():

    #input statements
    a = eval(input("Enter a's value: "))
    b = eval(input("Enter b's value: "))
    c = eval(input("Enter c's value: "))

    #finding s
    s = (a + b + c)/2

    #finding A
    A = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("Area =", A)

#triangle_area()

def sumSquares():
    lower = eval(input("Enter your lower number: "))
    upper = eval(input("Enter your higher number: "))
    acc = 0
    for s in range(lower, upper + 1):
        acc = acc + s ** 2
    print(acc)

#sumSquares()

def power():
    base = eval(input("Put your base here: "))
    exponent = eval(input("Put your exponent here: "))
    acc = 1
    for i in range(exponent):
        acc = acc * base
    print(base, "^", exponent,"=", acc)


power()
