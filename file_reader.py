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
        
