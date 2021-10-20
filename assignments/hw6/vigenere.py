"""
Name:
Celine Imani

Problem:
Creating a program that can decipher and print out the Vigenere decipher

Certification of Authenticity:
I, Celine Imani, certify that this assignment is entirely my own work.
"""

#import the graphics library
from graphics import *

# we create the code function
# MAKE SURE TO PUT MESSAGE, KEYWORD
def code(message, k):

    # create the window to put the message
    win_width = 500
    win_height = 300

    # name the GUI 'Vigenere'
    win = GraphWin("Vigenere", win_width, win_height)

    # now i have to design the graphical user interface
    # ask the user for message print
    message_text_pt = Point(100, 100)
    message_text = Text(message_text_pt, "Message to Code: ")
    message_text.draw(win)

    # where user puts message entry box
    message_entry = Entry(Point(275, 100), 20)
    message_entry.draw(win)

    # ask the user for key word print
    keyword_text_pt = Point(100, 150)
    keyword_text = Text(keyword_text_pt, "Keyword: ")
    keyword_text.draw(win)

    # where user puts key word entry box
    keyword_entry = Entry(Point(190, 150), 10)
    keyword_entry.draw(win)

    # create the encode button
    outline = Rectangle(125, 200)
    labelCenter = Point(200, 200)
    label = Text(labelCenter, "ENCODE")
    outline.draw(win)
    label.draw(win)

    # assigning entries
    for i in range():
        # converting the message entry box
        win.getMouse()
        message = int(message_entry.getText())

        # converting the keyword entry box
        win.getMouse()
        k = int(keyword_entry.getText())

    # now for the actual deciphering
    # the accumulation
    acc = ""
    for i in range(len(message)):
        c = message[i]
        key = k[i % len(k)]

        keyword = (ord(key) - 25)

        # shift c by the key
        ch = (ord(c) + keyword)

        # convert c back to a chr
        c = chr(ch)

        # add c to the acc
        acc = acc + c

    #the result for the code
    results_pt = Point(200, 175)
    results = Text(results_pt, str(acc))
    results.draw(win)

    #undraw the code button
    outline.undraw()
    label.undraw()

    #draw the instructions of closing
    final = "Click Anywhere to Close"
    instructions = Text(Point(200, 200), final)
    instructions.draw(win)

    win.getMouse()
    win.close()

#we put the code function in the main function
#we make sure to assign the variables both message and keyword
def main():
    #print(code())
if __name__ == "__main__":
    main()