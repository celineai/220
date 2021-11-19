"""
Name: Celine Imani

Problem: Show that I understand and can use classes and objects

Certification of Authenticity:
I, Celine Imani, swear all this work is of my own.
"""
from hw9.button import Button
from graphics import *
from random import *

def main():

    "Creating the window."
    win = GraphWin("Three Door Game", 600, 600)
    win.setBackground("pink")

    guess = Text(Point(130, 40), "Which door is the secret door?!")
    guess.draw(win)

    # draw three buttons, each labeled
    # "Door 1" "Door 2" "Door 3" in a graphics window
    door1 = Button(win, Point(100, 300), 6, 1, 'Door 1')
    door1.is_clicked()

    door2 = Button(win, Point(300, 300), 6, 1, 'Door 2')
    door2.is_clicked()

    door3 = Button(win, Point(400, 300), 6, 1, 'Door 3')
    door3.is_clicked()

    quitButton = Button(win, Point(300, 400), 2, 1, "Quit")

    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if door1.is_clicked() or door2.is_clicked() or door3.is_clicked():

        pt = win.getMouse()

    win.close()

# click the secret door = user wins
# clicks the wrong door, is a lost
# when they lose tell the user what the secret door was
# also color the door red
# if they win, color the secret door green
    win.getMouse()
    win.close()


