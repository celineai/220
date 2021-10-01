"""

Name: Celine Imani
traffic.py

Problem: For this program we have to figure out the average traffic patterns for the DOT.

Certificate of Authenticity:
I certify that this assignment is entirely my own work.

"""

def main():

    #first we have to gather the amount of roads that were surveyed
    roads = eval(input("How many roads were surveyed? "))

    #total kept getting set up as 180 lets move it around the for loop
    total = 0

    #then we ask how many days the roads were surveyed, we do this by using a for loop
    for i in range(roads):
        # first lets set up an accumulator
        acc = 0

        #now we set up our question asking how many roads were surveyed
        days = eval(input("How many days was road " + str(i + 1) + " surveyed? "))

        # after how many days, we ask how many cars traveled on each day
        # try putting it in a nested for loop ?
        for d in range(days): #had to put a different letter due to errors, kept getting road 3 for road 1

            #the system asking for the user input, we put extra spaces as a way to indent the code
            cars = eval(input("     How many cars traveled on day " + str(d + 1) + "?"))

            #now we bring the acc in so cars can stop printing only the last input
            acc = cars + acc

            #we then calculate the average of each day
            #we find the average through diving acc by how many days
            day_avg = acc / days

            # we gotta make a total variable for all the cars
            # because our acc keeps resetting and going back to 180
            total = total + cars

        #now we print the average each day after each day
        print("Road " + str(i + 1) + " average vehicles per day: " + str(round(day_avg,2)))


    # after we find the average for each one, we print the total amount of cars traveled
    print("Total number of vehicles traveled on all roads: " + str(total))

    #to find the total average of the cars travelling
    overall = total / roads

    #just to avoid parenthesis errors let make an extra variable
    rounded_total = round(overall, 2)

    #now finally... finally... we can print the overall average
    print("Average number of vehicles per road:" + str(rounded_total))


if __name__ == "__main__":
    main()
