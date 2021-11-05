"""
Name: Celine Imani

Problem: We must show that I know how conditionals and graphics work

Certification of Authenticity:
I, Celine Imani, swear this work is entirely my own with the
help of the CSCI CSL's instructor: Logan
"""

# questions need to ask:
    # why won't it hit again?
# once those questions are answered see if you can start
# importing the second ball and fixing the functions

# importing the graphic library
from graphics import *

# importing the random library
import random

# create the colors for ball 1
r1 = random.randint(0, 255)
g1 = random.randint(0, 255)
b1 = random.randint(0, 255)

# creates the colors for ball 2
r2 = random.randint(0, 255)
g2 = random.randint(0, 255)
b2 = random.randint(0, 255)


# acknowledges it hits the wall vertically
def hit_vertical(ball, window):
    if ball.getCenter().getY() + ball.getRadius() > 500:
        return True
    elif ball.getCenter().getY() - ball.getRadius() < 0:
        return True
    else:
        return False

# acknowledges it hits the wall horizontally
def hit_horizontal(ball, window):
    if ball.getCenter().getX() + ball.getRadius() > 500:
        return True
    elif ball.getCenter().getX() - ball.getRadius() < 0:
        return True
    else:
        return False

# acknowledges if the balls hit
def did_collide(ball, ball2):
     # if ball 1's x + radius equals ball's 2 x - radius then return true
     if ball.getCenter().getX() + ball.getRadius() == ball2.getCenter().getX() - ball2.getRadius:
         return True
     elif ball.getCenter().getX() - ball.getRadius() == ball2.getCenter().getX() + ball2.getRadius:
         return True
     else:
         return False

# switches the value signs so the ball can go into the opposite
def swap_sign(x):
    if x < 0:
        x += 2 * x
    else:
        x -= 2 * x
    return x


def main():
    # first let's start by creating the graphic window
    # creating the window
    w = 500
    h = 500
    win = GraphWin("Bumper Cars!", w, h)
    win.setBackground("white")

    # lets reference x and y before hand
    # they have to be random variables
    # random variables for ball 1
    x1 = random.randint(0, 500)
    y1 = random.randint(0, 500)

    # random variables for ball 2
    x2 = random.randint(0, 500)
    y2 = random.randint(0, 500)

    # let's try the radius
    # let's call it r
    # radius for the first circle
    rad = random.randint(10, 40)
    # radius for the second circle
    rad2 = random.randint(10, 40)

    # this while statement will only work when x is greater than 0
    # the circle gains random int
    # creation of ball 1
    c1 = Circle(Point(x1, y1), rad)

    # creation of ball 2
    c2 = Circle(Point(x2, y2), rad2)

    # the circle gets a random color
    # color for ball 1
    c1.setFill(color_rgb(r1, g1, b1))

    # color for ball 2
    c2.setFill(color_rgb(r2, g2, b2))

    # we draw the circle
    # drawing circle 1
    c1.draw(win)

    # drawing circle 2
    c2.draw(win)

    # moves the circle by 20
    move_val = 20

    # the while function to run the code
    while True:
        # helps slows down the ball
        time.sleep(.5)

        # let's try getting the first circle to move
        # helps when the ball hits the wall horizontally
        # CIRCLE ONE HORIZONTAL
        if hit_horizontal(c1, w):
            # it moves this amount of value till it's swapped into reverse
            move_val = swap_sign(move_val)

            # so now the ball moves that amount/direction now
            c1.move(move_val, 0)
        else:
            # ball just keeps moving as is
            c1.move(move_val, 0)

        # CIRCLE TWO HORIZONTAL
        if hit_horizontal(c2, w):
            # it moves the amount of value till it's swapped into reverse
            move_val = swap_sign(move_val)

            # so now the ball moves that amount/direction now
            c2.move(move_val, 0)
        else:
            # ball keeps moving as is
            c2.move(move_val, 0)


        # helps when the ball is about to hit the wall vertically
        # CIRCLE ONE VERTICAL
        if hit_vertical(c1, h):
            # it moves this amount of value till it's swapped into reverse
            move_val = swap_sign(move_val)
            # so now the ball moves that amount/direction now
            c1.move(0, move_val)
        else:
            # ball just keep moving as is
            c1.move(0, move_val)

        # CIRCLE TWO VERTICAL
        if hit_vertical(c2, h):
            # moves this amount till swapped
            move_val = swap_sign(move_val)
            # now moves that amount
            c2.move(0, move_val)
        else:
            # ball just keep moving as is
            c2.move(0, move_val)

        # if the balls hit, they need to bounce off of one another
        if did_collide(c1, c2):
             move_val = swap_sign(move_val)
        #
        else:
             c1.move(move_val, move_val)
             c2.move(move_val, move_val)

        # why is it only hitting one wall, but won't hit anything else?
    # closing the window

    win.getMouse()
    win.close()


main()
