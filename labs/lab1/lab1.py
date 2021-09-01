"""
Name: Celine Imani
lab1.py

Problem: This function calculates the area of a rectangle
"""

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

#calc_rec_area()

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)

#calc_volume()

def shooting_percentage():
    player = eval(input("Enter the player's shots: "))
    total = eval(input("Enter the total amount shots: "))
    percantage = player/total * 100
    print("Percentage =", percantage)

#shooting_percentage()

def coffee():
    pounds = eval(input("Enter the amount of pounds: "))
    total = (10.50 * pounds) + (.86 * pounds) + 1.50
    print("Total cost =", total)

#coffee()

def kilometers_to_miles():
    km = eval(input("Enter the input of kilometers traveled: "))
    miles = km / 1.61
    print("The amount of miles traveled =", miles)

kilometers_to_miles()