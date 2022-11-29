from bill_manager import *

a_bill_manager = BillManager()

print("People involved: ")
a_bill_manager.print_people_name()

print("\nThe following bills will be proccessed: ")
a_bill_manager.print_bills()
print("\n--------------------")

a_bill_manager.proccess_bills()

a_bill_manager.get_transferences_to_be_done()

print("Transfer summary: \n")
a_bill_manager.print_transfers_summary()