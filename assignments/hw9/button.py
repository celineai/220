"""
Name: Celine Imani

Problem: Show that I understand and can use classes

Certification of Authenticity:
I, Celine Imani, swear all this work is of my own.
"""
from graphics import *

class Button:
    def __init__(self, win, center, width, height, String):
        self.text = String

        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()

        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h

        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)

        self.shape = Rectangle(p1, p2)
        self.shape.draw(win)

        self.text = Text(center, text)
        self.text.draw(win)
        self.set_label()

    def get_label(self):
        return self.text.getText()

    def draw(win):
        win.shape.draw(win)

    def undraw():
        shape.undraw()

    def is_clicked(point):
        point.text.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def set_label(label):
         """Setting the button to inactive"""
         label.shape.setFill('red')
         label.shape.setWidth(1)
         label.active = False
