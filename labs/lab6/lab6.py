"""
Name: Celine Imani
lab5.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    # getting the name
    name= input("Please enter your first and last name: ")

    #splitting the name into two
    split = name.split(" ")

    #putting the name in reverse order
    reverse_Order = split[1] + ', ' + split[0]

    print(reverse_Order)


def company_name():
    #time to ask the user for the domain name
    domain = input("Please enter a domain: ")

    #split the domain name
    split = domain.split(".")

    print(split[1])

def initials():
    #ask the user how many names are being typed
    nameAmount = eval(input("How many names are being used?"))

    for i in range(nameAmount):
        acc = 0

        #we now ask their first name
        firstName = input("Enter the name of student 1: ")

        #ask their last name, the example used their first name
        lastName = input("Enter " + str(firstName) + "'s last name: ")

        #create the initials
        combine =  firstName[0] + lastName[0]

        print(str(firstName) + "'s initials are: " + str(combine))

def names():

    #ask the user for the list of names
    x = input("Enter people's names, separated by commas: ")

    #we now have to split all the names by space and comma
    names = x.split(", ")

    #we create a 'for loop' for our system to gather all the split names
    for i in names:
        #we split up the names
        name = i.split(" ")

        print("The initials are: " + str(name[0][0] + name[1][0]))

def thirds():
    #ask how many sentences
    amount = eval(input("How many sentences will be input?"))

    #put the for loop so each sentence can go through
    for i in range(amount):
        acc = 0

        #ask the sentences
        sentences = input("Please write sentence: ")

        #put the sequence
        third = sentences[2:-1:3]

        print(str(third))



def word_average():
    # ask the user the amount of sentences being inputted, so it knows how to run
    amount = eval(input("How many sentences will be input?"))

    # put a for loop so it goes through each sentence
    for i in range(amount):
        acc = 0

        #ask for the sentences
        sentences = input("Please write your sentence: ")

        #found the amount of words
        words = sentences.split(" ")

        #now we gotta find the number of words
        for l in words:
            acc = acc + len(l)
        num_words = len(words)
        average = acc / len(words)

        print(str(average))

def pig_latin():
    sentence = input("Please write the sentence: ")
    sentence = sentence.lower()
    words = sentence.split(" ")

    for word in words:
        print(word[1: ] + word[0] + "ay")



def main():
    #name_reverse()
    #company_name()
    #initials()
    #names()
    #thirds()
    #word_average()
    #pig_latin()


main()
