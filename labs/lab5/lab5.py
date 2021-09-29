"""
Name: Celine Imani
lab5.py
"""
import math
from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():

    # creating the window
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # number of clicks allowed to be used
    num_clicks = 3

    # instructions for your use to create the triangle
    inst_pt = Point(win_width / 2, win_height - 10)
    instructions = Text(inst_pt, "click to create the triangle")
    instructions.draw(win)

    # Add code here to accept the mouse clicks, draw the triangle.
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()

    # coordinates
        # x-coordinates
    x1 = p1.getX()
    x2 = p2.getX()
    x3 = p3.getX()

        # y-coordinates
    y1 = p1.getY()
    y2 = p2.getY()
    y3 = p3.getY()

    # line length ohmygod does the code ever end
    dx = x2 - x1
    dx2 = x1 - x3
    dx3 = x3- x2

    dy = y2 - y1
    dy2 = y1 - y3
    dy3 = y3 - y2

    #   finding the distance
    length1 = math.sqrt((dx** 2) + (dy** 2))
    length2 = math.sqrt((dx2** 2) + (dy2** 2))
    length3 = math.sqrt((dx3** 2) + (dy3** 2))


    #   finding the perim
    perim = length1 + length2 + length3

    # finding the area
    s = (perim) / 2
    area = math.sqrt(s * (( s - length1) * ( s - length2 ) * (s - length3 )))

    # display its area in the graphics window.

    inst_pt = Point(win_width / 2, win_height - 490)
    instructionsArea = Text(inst_pt, "The area is: " + str(area))
    instructionsArea.draw(win)

    # displaying the perimeter
    inst_pt = Point(win_width / 2, win_height - 475)
    instructionsPerim = Text(inst_pt, "The perimeter is: " + str(perim))
    instructionsPerim.draw(win)

    # formula data points
    triangle = Polygon(Point(x1,y1), Point(x2, y2), Point(x3, y3))
    triangle.setOutline("blue")
    triangle.setFill("blue")
    triangle.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    # entries
    #red entry box
    red_box = Entry(Point(win_width / 2, win_height - 160), 5)
    red_box.draw(win)

    #green entry box
    green_box = Entry(Point(win_width / 2, win_height - 130), 5)
    green_box.draw(win)

    #blue entry box
    blue_box = Entry(Point(win_width / 2, win_height - 100), 5)
    blue_box.draw(win)

    #for loop
    for i in range(5):
        win.getMouse()
        red = int(red_box.getText())
        blue = int(blue_box.getText())
        green = int(green_box.getText())
        color = color_rgb(red, blue, green)
        shape.setFill(color)

    # Wait for another click to exit
    win.getMouse()
    win.close()

def process_string():
    s = input("Please write the string here: ")
    #the first character in the string
    first = s[0]

    #the last character in the string
    last = s[-1]

    #characters 2-5
    two_to_five = s[2:5]

    #the concatenation of first and last
    concatenation = s[0] + s[-1]

    #first 3 repeated 10 times
    repeat = s[0] * 3

    #a character printed in a line
    for i in range(len(s)):
        c = s[i]
        print(c)

    #the amount of characters per line
    length = len(s)

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    #printing "hithere"
    #x = values[1] + values[3]

    #printing the sum of 5 and 2.5
    #x = float(values[0]) + float(values[2])

    #making the string
    #x = values[1] * 3

    #list 2.5, "there", 5
    #x = [values[2:5]]

    #list 2.5, 5, 7.2
    #x = [values[2], values[4], float(values[0]) + float(values[2])]

    #sum of 5 + 2.5 + 7.2
    #x = float(values[0]) + float(values[2]) + (float(values[0]) + float(values[2]))

    #number of items in values
    x = len(values)
    print(x)

def another_series():
    #asking user for the terms
    n = eval(input("Enter the amount of terms:"))
    acc = 0

    for i in range(n):
        y = 2 + 2 * (i % 3)
        #sum = acc + y


        print(y, end=" ")
    print()


def main():
    # target()
    # triangle()
    # color_shape()
    # process_string()
    # process_list()
    another_series()

    pass

main()
