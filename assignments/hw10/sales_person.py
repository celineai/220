"""
Name: Celine Imani

Problem: To show that I understand objects and lists

Certification of Authenticity: I, Celine Imani, swear that this assignment was entirely my own work.
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sale = sale
        self.sales.append(sale)

    def total_sales(self):
        self.total = 0
        for sale in self.sales:
            self.total += sale
        return float(self.total)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if quota > self.total:
            return True
        else:
            return False

    def compare_to(self, other):
        other.total_sales()
        if other > self:
            return -1
        elif self > other:
            return 1
        else:
            return 0

    def __str__(self):
        return self.employee_id + "-" + self.name + ":" + self.total_sales()
