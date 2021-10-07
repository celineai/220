"""
Name: Celine Imani
greetings.py

Problem: We have to show our knowledge with graphics by creating a Valentine's day card!

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import time

def main():

        # create window, let's make it long so it's in card shape
        win_width = 300
        win_height = 500
        win = GraphWin("Color Shape", win_width, win_height)
        win.setBackground("pink")

        # writing the message beneath
        # try to see if you can change fonts later
        msg = "Happy Valentine's Day!"
        inst = Text(Point(win_width / 2, win_height - 325), msg)
        inst.draw(win)

        # time to make the heart aha oh no
        # the upper left part
        heartUpperLeft = Circle(Point(125, 225), 30)
        heartUpperLeft.setFill("red")
        heartUpperLeft.setOutline("red")
        heartUpperLeft.draw(win)

        # the upper right part
        heartUpperRight = Circle(Point(175, 225), 30)
        heartUpperRight.setFill("red")
        heartUpperRight.setOutline("red")
        heartUpperRight.draw(win)

        # bottom middle part
        heartBottom = Polygon(Point(96,235), Point(150,300), Point(204, 235))
        heartBottom.setFill("red")
        heartBottom.setOutline("red")
        heartBottom.draw(win)


        # create text for the user to create the arrow
        inst_pt = Point(win_width / 2, win_height - 10)
        instructions = Text(inst_pt, "Click to shoot Cupid's arrow!")
        instructions.draw(win)

        # the creation of the arrow
        arrow = Line(Point(20, win_height - 100), Point(win_width - 200, 300))
        arrow.setArrow("last")
        arrow.setFill("white")
        arrow.setOutline("white")

        arrow.draw(win)

        # trying this out
        num_clicks = 1

        # the arrow animation
        for i in range(num_clicks):
                #make the arrow appear
                win.getMouse()
                time.sleep(.5)
                arrow.move(150, -150)
                # now to make it closable
                # undraw the click
                instructions.undraw()

                # click again to close
                final = "Click to close!"
                instructions = Text(Point(win_width / 2, win_height - 10), final)
                instructions.draw(win)


        win.getMouse()
        win.close()

if __name__ == "__main__":
    main()
