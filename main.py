from bill_manager import *

a_bill_manager = BillManager()

print("People involved: ")
a_bill_manager.print_people_name()

print("\nThe following bills will be proccessed: ")
a_bill_manager.print_bills()
print("\n--------------------")

a_bill_manager.proccess_bills()

print(a_bill_manager.print_summary_per_person())