from file_reader import *
from people import *

class BillManager:
    
    def __init__ (self):
        self.a_file_reader = FileReader()
        self.people = People(self.a_file_reader.people_read("people.txt"))
        self.bills = self.a_file_reader.get_all_bills("bills.txt")

    def print_people_name(self):
        print(self.people.people_list_name)
        
    def print_bills(self):
        print(self.bills)
        
    def proccess_bills(self):
        for bill in self.bills:
            #input check
            if bill[0] not in self.people.people_list_name:
                print(f"{bill[0]} hizo un gasto pero no figura en archivo de entrada de personas, corregir.")
                exit(1)
            
            qty_to_be_divided = self.people.qty
            people_excluded = []
            
            if(len(bill) > 2 ):
                # there are people excluded
                qty_to_be_divided = self.people.qty - (len(bill) - 2)
                for i in range(2, len(bill)):
                    people_excluded.append(bill[i])
            ammount_charged_per_person = round(float(bill[1]) / qty_to_be_divided, 2)
            #record bill in every people affected
            for person in self.people.people_list_name:
                if person not in people_excluded:
                    self.write_bill(person, ammount_charged_per_person)
                if person == bill[0]:
                    self.write_to_paid_list(bill[0], bill[1])
        
                        
    def write_bill(self, person_to_bill, ammount_charged_per_person):
        for person in self.people.people:
            if person == person_to_bill:
                self.people.people[person_to_bill].to_pay_list.append(ammount_charged_per_person)
                self.people.people[person_to_bill].balance = self.people.people[person_to_bill].balance - ammount_charged_per_person
                
    def write_to_paid_list(self, person_who_paid, ammount_paid):
        self.people.people[person_who_paid].paid_list.append(float(ammount_paid))
        self.people.people[person_who_paid].balance = self.people.people[person_who_paid].balance + float(ammount_paid)
    
    def print_summary_per_person(self):
        for person in self.people.people.keys():
            self.people.people[person].print_summary()

    def get_transferences_to_be_done():
        pass
