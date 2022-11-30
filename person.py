class Person:
    
    def __init__ (self, name):
        self.name = name
        self.paid_list = []
        self.to_pay_list = []
        self.balance = 0.0
        self.bills_paid = []
        self.bills_to_pay = []

    
    def print_summary(self):
        print("Name: " + str(self.name))
        print("Paid list: " + str(self.paid_list))
        print("Total paid: " + str(round(sum(self.paid_list),2)))
        print("To pay list: " + str(self.to_pay_list))
        print("Total to pay: " + str(round(sum(self.to_pay_list),2)))       
        print("Balance: " + str(round(self.balance, 2)))
        print("---o---")