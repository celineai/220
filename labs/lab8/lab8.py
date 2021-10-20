"""
Name: Celine Imani
lab8.py
"""
# to import the encode function
from lab7 import encode

# to import the encode better function
from lab7 import encode_better

def number_words(infile_name, outfile_name):
    # testing i
    i = 1

    # program must read the contents of the input text files
    # creating the input
    infile_name = "walrus.txt"
    infile = open(infile_name, "r")

    # creating the output
    outfile_name = "new_walrus.txt"
    outfile = open(outfile_name, "w")

    # number the words
    for line in infile:
        new_line = line.split()
        for word in new_line:
            outfile.write(str(i) + " " + word + "\n")
            i += 1

def hourly_wages(in_file_name, out_file_name):
    # just like before takes an in_file and out_file for parameters
    # open these files
    infile = open("hourly_wages.txt", "r")
    outfile = open("hourly_wages_output.txt", "w")

    #make a text files
    # at least two lines
    # first_name, last_name, hourly_wage, hours_worked
    # ex: alex smyth 10.00 5 (spaces used)
    # go through each line

    for line in infile:
        new_line = line.split()

    # the 2nd index is wage
    # add a 1.65 to each person's wage
        new_line[2] = str(float(new_line[2]) + 1.65)
        outfile.write("".join(new_line) + "\n")

def calc_check_sum(isbn):
    # isbn / universal identifier
    # check_sum is used for error checking
    # always 10 characters in the isbn, multiple by reverse of their index
    # len(isbn) = 10

    sum = 0
    isbn = str(isbn)
    isbn = isbn.split
    for i in range(len(isbn)):
        num = isbn[i] * (10 - i)
        sum = sum + num
    return sum% 11



def send_message(infile, friend):
    # rename the file to whatever your friend's name.txt
    # creating the input
    infile_name = "the_message.txt"
    infile = open(infile_name, "r")

    # creating the output
    outfile_name = friend + ".txt"
    outfile = open(outfile_name, "w")

    for line in infile:
        outfile.write(line + "\n")



def send_safe_message(file, friend, key):
    # rename the file to whatever your friend's name.txt
    # creating the input
    infile_name = "the_message.txt"
    infile = open(infile_name, "r")

    # creating the output
    outfile_name = friend + ".txt"
    outfile = open(outfile_name, "w")

    for line in infile:
        new_line = encode(line)
        outfile.write(new_line + "\n")

def send_uncrackable_message(file, friend, pad):
    # rename the file to whatever your friend's name.txt
    # creating the input
    infile_name = "the_message.txt"
    infile = open(infile_name, "r")

    # creating the output
    outfile_name = friend + ".txt"
    outfile = open(outfile_name, "w")

    for line in infile:
        new_line = encode_better(line)
        outfile.write(new_line + "\n")

def main():
    #number_words("walrus.txt", "new_walrus.txt")
    #hourly_wages("hourly_wages.txt", "hourly_wages_output.txt")
    #print(calc_check_sum(0072946520))
    #send_message("the_message.txt", name)
    #send_safe_message("the_message.txt", name)
    #send_uncrackable_message("the_message.txt", name, moye-ravv)
    pass

main()