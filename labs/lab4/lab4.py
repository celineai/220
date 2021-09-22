"""
Name: Celine Imani
lab4.py
"""

from graphics import *
import math

def squares():

    """
    You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """

    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move the square
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds the square
    shape = Rectangle(Point(20, 20), Point(40, 40))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the square
    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)


    #undraw the original instructions
    instructions.undraw()

    # click again to close
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to close!")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():

    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """

    # creating the window
    w = 400
    h = 400
    win = GraphWin("Rectangle", w, h)

    #user clicks
    p1 = win.getMouse()
    p2 = win.getMouse()

    #the length and width
    length = abs(p2.getY() - p1.getY())
    width = abs(p2.getX() - p1.getX())

    #the formulas
    area = (length * width)
    perimeter = 2 * (length + width)

    #the text
    inst_pt = Point(w / 2, h - 5)
    instructions = Text(inst_pt, "The area is: " + str(area))
    instructions.draw(win)

    inst_pt2 = Point(w / 2, h - 20)
    instructions2 = Text(inst_pt2, "The perimeter: " + str(perimeter))
    instructions2.draw(win)

    #creating the shape
    rect = Rectangle(p1, p2)
    rect.setOutline("green")
    rect.setFill("green")
    rect.draw(win)

    #ending
    win.getMouse()
    win.close()



def circle():
    # creating the window
    width = 400
    height = 400
    win = GraphWin("Circle", width, height)

    #user clicks
    p1 = win.getMouse()
    p2 = win.getMouse()

    #formula data points
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()

    # radius
    r = (((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    r = math.sqrt(r)

    # drawing the circle
    c = Circle(p1, r)
    c.setOutline("red")
    c.setFill("red")
    c.draw(win)

    #printing the text
    inst_pt = Point(width / 2, height - 10)
    instructionsRadius = Text(inst_pt, "The radius is: " + str(r))
    instructionsRadius.draw(win)

    win.getMouse()
    win.close()

def pi2():
    #ask the user how many times
    n = eval(input("Enter the amount of terms: "))
    acc = 0
    for i in range(n):
        num = 4
        denom = 1 + 2 * i
        frac = (num/denom) * ((-1) ** i)
        acc = acc + frac
    print(math.pi - acc)

def main():
    #squares()
    #rectangle()
    #circle()
    pi2()

main()
