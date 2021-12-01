"""
Name: Celine Imani
lab13.py
"""

def is_in_binary(val, values):
    mid = val[len(values)] // 2
    while val == mid and len(values) != 1:
        if val > mid:
            values = mid - 1  #everything before the mid point
        if val < mid:
            values = mid + 1

        if val == values:
            return True
        else:
            return False

def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i, len(values)):
            if j < i:
                lowest = values[j]
                pos = j
        values[pos], values[lowest] = values[lowest], values[pos]

def get_area(rect):
    p1 = rect.getp1()
    p2 = rect.getp2()
    w = abs(p1.getX())
    h = abs(p2.getY())
    return w * h

 def rect_sort(rectangles):
    d = {}
    areas = []
    for rect in rectangles:
        d[get_area(rect)] = rect
        areas.append(get_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        values[i] = dict[]

# capstone:
def trade_alert(filename):
    infile = open(filename, "r")
    data = infile.read().split() #returns a list of string
    - - - - -
    for seconds in range(data):
        if seconds > 850:
            print("alert!")
        elif seconds > 500:
            print("warning!")


def main():
    is_in_binary()
    selection_sort()
    rect_sort()
    trade_alert(trades.txt)
    pass


main()
