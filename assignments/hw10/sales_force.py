"""
Name: Celine Imani

Problem: To show that I understand objects and lists

Certification of Authenticity: I, Celine Imani, swear that this assignment was entirely my own work.
"""
from sales_person import SalesPerson

class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(file_name):
        # get the data file in
        file_name = eval(input("Import the sales data file: "))
        # read the file
        infile = open(file_name, 'r')
        # gotta read the lines baby
        for line in infile:
            employee_id, name, sales = infile.split(",")
            new_person = SalesPerson(employee_id, name, sales)
            SalesPerson.append(new_person)
            return SalesPerson

    def quota_report(quota):
        sales_people = SalesPerson
        return sales_people


    def top_seller(self):
        best = sales_people(infile.readline())
        # process subsequent lines of the file
        for line in infile:
            # turn the line into a record
            s = ssales_people(line)
            if s.sales() > best.sales():
                best = s
            infile.close()
            return best

    def individual_sales(self, employee_id):
        if employee_id:
            return employee_id
        else:
            return None

