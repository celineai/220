"""
Name:
Celine Imani

Problem:
We must show we know how to use numeric data from a text file

Certification of Authenticity:
I, Celine Imani, swear this work is entirely my own.
"""

#first we have to create the function
def weighted_average(in_file_name, out_file_name):

    #find a way for the program to read the file

    # ask formula for the input
    infile = open("grades.txt", "r")
    #now the output
    outfile = open("avg.txt", "w")

    # a new file can now be created

    # go through each line
    for line in infile:
        #splitting everything
        #getting the names
        #cut the first name because i am so confused
        x = line.split(' ')
        firstName = str(x[0])
        lastName = str(x[1])

        # find the weight & grades
        w = str(x[2::2])

        # remember [ start: end : skip ]
        g = str(x[3::2])

        # weighted average formula
        avgForm = (w + g)


        # FINAL CODE:
        outfile.write(firstName + " " + lastName + "'s Average:" + avgForm + "\n")

def main():
    weighted_average("grades.txt", "avg.txt")
main()
