"""
Name: Celine Imani
interest.py

Problem: We need to find out the monthly interest rate.

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

def main():
    #variables the user inserts
    annual = eval(input("Enter the annual interest rate: "))
    cycle = eval(input("Enter the amount days in the billing cycle: "))
    previous = eval(input("Enter the previous net balance: "))
    payment = eval(input("Enter the amount paid: "))
    billing = eval(input("The day of billing: "))

    #remainder of days left
    remainder =  cycle - billing

    #results
    step1 = previous * cycle
    step2 = payment * remainder
    step3 = step1 - step2
    step4 = step3 / cycle

    #monthly
    monthly = ( annual / 12 ) / 100

    #percantage(
    monthly_interest_charge = monthly * step4

    print(round(monthly_interest_charge, 2))

if __name__ == "__main__":
    main()
