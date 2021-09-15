"""
Name: Celine Imani
lab3.py
"""
import math

def average():
    acc = 0
    number_inputs = eval(input("Enter amount of grades: "))
    for i in range(number_inputs):
        grades = eval(input("Enter your grade for HW " + str(i + 1)))
        acc = acc + grades
    mean = acc / number_inputs
    print("Your average is ", mean)

#average()

def tip_jar():
    acc = 0
    for i in range(5):
        donation = eval(input("How much are you donating? " + str(i + 1)))
        acc = acc + donation
    print("The total amount of donations are: ", acc)
#tip_jar()

def newton():
    x = eval(input("x = ")
    refine = eval(input("refine = "))
    approx = x / 2
    for i in range(refine):
        approx = (approx = ((approx + ( x /approx))))/2
    print(approx)

#newton()

def sequence():


#sequence()

#def pi():
    terms = eval(input("Write the amount of terms: "))
    acc = 1
    for i in range(terms):
        num = 2 + (i // 2 * 2)
        denom = 1 + ((i + 1))(2 * 2))
        acc = acc * fractions
    print(acc * 2)

#pi()

