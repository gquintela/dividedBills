from bill_manager import *
import sys

args_passed = len(sys.argv)

if args_passed not in [1, 3]:
    print("USAGE:")
    print("python3 main.py <txt file> <csv file>")
    print("   where:")
    print("   'txt file' is a file with one person in each line")
    print("   and:")
    print("   'csv file' is a file with the bills in a csv format, see bills.csv example.")
    exit(0)

people_txt = "people.txt"
bills_csv = "bills.csv"

if args_passed == 3:
    people_txt = sys.argv[1]
    bills_csv = sys.argv[2]

a_bill_manager = BillManager(people_txt, bills_csv)
a_bill_manager.run()
