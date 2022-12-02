
class Person:

    def __init__(self, name):
        self.name = name
        self.bills_paid = []
        self.bills_to_pay = []
        self.people_qty_in_group = 0

    def print_summary(self):
        print("Name: " + str(self.name))
        print("Paid list: " + str(self.paid_list))
        print("Total paid: " + str(round(sum(self.paid_list), 2)))
        print("To pay list: " + str(self.to_pay_list))
        print("Total to pay: " + str(round(sum(self.to_pay_list), 2)))
        print("Balance: " + str(round(self.balance, 2)))
        print("---o---")

    def sum_of_bills_paid(self):
        res = 0
        for bill_paid in self.bills_paid:
            res = res + bill_paid.ammount
        return res

    def sum_of_bills_to_pay(self):
        res = 0
        for bill_to_pay in self.bills_to_pay:
            effective_ammount_to_divide = self.people_qty_in_group - \
                len(bill_to_pay.people_excluded)
            res = res + (bill_to_pay.ammount / effective_ammount_to_divide)
        return res

    def get_balance(self):
        return self.sum_of_bills_paid() - self.sum_of_bills_to_pay()
