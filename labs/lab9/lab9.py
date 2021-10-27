"""
Name: Celine Imani
lab9.py
"""
import math

from graphics import *

def addTen(nums):
    # modify the object in a function without returning the object
    # accepts the parameter of a list of numbers
    # modify list by adding ten to it
    for i in range(len(nums)):
        nums[i] = nums[i] + 10

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] **2

def sumList(nums):
    # returns the sum of numbers in the list
    acc = 0
    for i in range(len(nums)):
        nums[i] = nums[i]
        acc = acc + nums[i]
    print(acc)

def toNumbers(nums):
    #convert strings to a number/int
    for i in range(len(nums)):
        nums[i] = nums[i]

def writeSumofSquares():
    #creating the input text
    ipn = input("inputSums.txt")
    infile = open(ipn, "r")

    # creating the output text
    opn = output("output.txt")
    outfile = open(opn, "w")

    # now the loop
    for line in infile:
        #call your 3 functions
        toNumbers(nums)
        squareEach(nums)
        sumList(nums)
        outfile.write("sum = " + str(line) + "\n")
        pass

def starter():
        weight = eval(input("Enter the wrestler's weight: "))
        wins = eval(input("Enter the amount of wrestler's wins: "))

        # situation a
        # 160  weight >= 150
        # wins >= 5
        if 160 >= weight:
            if weight >= 150:
                if wins >= 5:
                    print("The wrestler earned a starting position.")
                else:
                    print("The wrestler did not earn a starting position.")

        # situation b
        # weight > 199
        if weight > 199 or wins > 20:
            print("The wrestler earned a start position.")
        # if they don't meet any requirement
        else:
            print("The wrestler did not earn a starting position.")


def leapYear(year):

    if year % 4 == 0 and (year % 100 !=0 or year % 400 == 0):
        print(str(year) + " is a leap year")
    else:
        print(str(year) + " is not a leap year")

    # <var> is a leap year
    # <var> is not a leap year


def circleOverlap():
    win = GraphWin("Circle Overlap", 400, 400)
    # circle 1
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius1 = math.sqrt( (p1.getX() - p2.getX()) **2 + (p1.getY() - p2.getY()) **2)
    circle = Circle(p1, radius1)
    circle.setOutline("red")
    circle.setFill("pink")
    circle.draw(win)

    # circle 2
    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    circle = Circle(p3, radius2)
    circle.setOutline("green")
    circle.setFill("blue")
    circle.draw(win)

    # distance formula:
    dist = math.sqrt(((p1.getX() - p3.getX())) **2 + (p1.getY() - p3.getY()) **2)

    # if statement
    if dist < (radius1 + radius2):
        overlap = "The circles overlap."
        overlapped = Text(Point(400 / 2, 400 - 20), overlap)
        overlapped.draw(win)
    else:
        noOverlap = "The circles do not overlap."
        notOverlapping = Text(Point(400 / 2, 400 - 20), noOverlap)
        notOverlapping.draw(win)

    win.getMouse()
    win.close()

    # draw two circles
    # distance formula to find distance between points
    # radius of each circle, there should be a shared space
    # the distance between two circles overlapping
        # dist(c1, c2) < r1 + r2

def main():
    #addTen function
    #nums = [5, 2, -3]
    #addTen(nums)
    # worked

    #squareEach function
    #nums = [5, 6, 3]
    #squareEach(nums)
    # worked

    #sumList function
    #sumList(nums)

    #toNumbers
    strList = [5, 6, 3]
    toNumbers(strList)

    #writeSumofSquares()

    #starter()
    # worked

    #print(leapYear(2020))
    # worked

    #circleOverlap()
    # worked
    pass
main()
