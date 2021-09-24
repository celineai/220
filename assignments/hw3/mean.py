"""
Name: Celine Imani
interest.py

Problem: We must show that we understand computing means.

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
import math

def main():
#the program first needs to take the user's data
    acc = 0

    #we must find out how many values
    number_input = eval(input("Enter the amount of values:"))

    #now we have to ask for all the values
    for i in range(number_input):
        values = eval(input("Enter the values:" + str(i + 1)))

    for i in range(number_input):
         #the root mean square formula
         #unlike the mean, the sum is squared
         rms_sum = (values)**2
         #now we can easily perform the operation
         rms_average = math.sqrt(rms_sum / ((number_input)**2))

         #now the harmonic mean
         #all the inputs are divided by one
         harmonic_sum = 1 / (number_input)
         #theyre all divided by input number
         harmonic_mean = number_input / harmonic_sum

         #formula for the geometric value


    #print the values
    print(round(rms_average,3))
    print(round(harmonic_mean, 3))
    #print(round(geometric))

if __name__ == "__main__":
    main()


