import csv

class FileReader:
    
    def __init__ (self):
        pass

    def people_read(self, file):
        with open(file, encoding = 'utf-8') as f:
            people = f.read().splitlines()
        return people
        
    def get_all_bills(self, file):
        bills  = []
        with open(file, encoding = 'utf-8') as f:
            bills_raw = f.read().splitlines()
            for bill_raw in bills_raw:
                bills.append(bill_raw.split())
        return bills
        
    def read_csv_bills(self, file):
        bills  = []
        with open('test.csv', 'r') as file:
            reader = csv.reader(file)
            bills = list(reader)
            self.remove_empty_fields(bills)
        bills.pop(0) #remove header
        return bills

    def remove_empty_fields(self, bills):
        for bill in bills:
            self.check_missing_obligatory_fields(bill)
            while "" in bill:
                bill.remove("")
            if(len(bill) < 4):
                print("campos obligatorios vacios, chequear entrada.")
                exit(1)

    def check_missing_obligatory_fields(self, bill):
        for i in range(0, 4):
            if bill[i] == '':
                print(f"En {bill}\nCampos obligatorios vacios, chequear.")
                exit(1)


