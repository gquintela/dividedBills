from file_reader import *
from people import *
from fancy_printer import *

class BillManager:
    
    def __init__ (self):
        self.a_file_reader = FileReader()
        self.people = People(self.a_file_reader.people_read("people.txt"))
        self.bills = self.a_file_reader.read_csv_bills("test.csv")
        self.transfer_summary = []
        self.a_fancy_printer = FancyPrinter()

    def proccess_bills(self):
        for bill in self.bills:
            #input check
            if bill[0] not in self.people.people_list_name:
                print(f"{bill[0]} hizo un gasto pero no figura en archivo de entrada de personas, corregir.")
                exit(1)
            
            qty_to_be_divided = self.people.qty
            people_excluded = []
            
            if(len(bill) > 4 ):
                # there are people excluded
                for i in range(4, len(bill)):
                    people_excluded.append(bill[i])
                qty_to_be_divided = self.people.qty - len(people_excluded)
            ammount_charged_per_person = round(float(bill[1]) / qty_to_be_divided, 2)
            #record bill in every people affected
            for person in self.people.people_list_name:
                if person not in people_excluded:
                    self.write_bill(person, ammount_charged_per_person, bill)
                if person == bill[0]:
                    self.write_to_paid_list(bill)
        
                        
    def write_bill(self, person_to_bill, ammount_charged_per_person, bill):
        bill_with_ammount = bill
        bill_with_ammount.append(ammount_charged_per_person)
        for person in self.people.people:
            if person == person_to_bill:
                self.people.people[person_to_bill].to_pay_list.append(ammount_charged_per_person)
                self.people.people[person_to_bill].balance = self.people.people[person_to_bill].balance - ammount_charged_per_person
                self.people.people[person_to_bill].bills_to_pay.append(bill_with_ammount)
                
    def write_to_paid_list(self, bill):
        person_who_paid = bill[0]
        ammount_paid = bill[1]
        self.people.people[person_who_paid].paid_list.append(float(ammount_paid))
        self.people.people[person_who_paid].balance = self.people.people[person_who_paid].balance + float(ammount_paid)
        self.people.people[person_who_paid].bills_paid.append(bill)

    def get_balance_list(self):
        balance_list = []
        for person in self.people.people.keys():
            balance_list.append([person, self.people.people[person].balance])
        return balance_list
        
    def _get_balance(self, e):
        return e[1]
    
    def _get_name(self, e):
        return e[0]

    def write_summary(self, sender_name, reciever_name, ammount_to_transfer):
        self.transfer_summary.append([sender_name, reciever_name, ammount_to_transfer])

    def _remove_if_balance_near_zero(self, balance_list, person):
        if(abs(self._get_balance(person)) < 5):
            balance_list.remove(person)

    def balance_account(self, balance_list, transfer_sender, transfer_reciever):
        sender_balance = self._get_balance(transfer_sender)
        reciever_balance = self._get_balance(transfer_reciever)
        ammount_to_transfer = min(abs(sender_balance), abs(reciever_balance))
        if(abs(sender_balance) > abs(reciever_balance)):
            #descuento el balance del ultimo al primero
            balance_list[0][1] = balance_list[0][1] + self._get_balance(transfer_reciever)
            # cierra el ultimo, y lo vuelo
            balance_list.remove(transfer_reciever)
        else:
            #descuento el balance del primero al ultimo
            balance_list[len(balance_list) - 1][1] = balance_list[len(balance_list) - 1][1] + self._get_balance(transfer_sender)
            # cierra el primero y lo vuelo
            balance_list.remove(transfer_sender)
        self.write_summary(self._get_name(transfer_sender), self._get_name(transfer_reciever), round(ammount_to_transfer,2))
        
    def get_transferences_to_be_done(self):
        balance_list = self.get_balance_list()
        
        while(len(balance_list) > 0):
            balance_list.sort(key = self._get_balance)
            if(len(balance_list) == 1):
                return
            transfer_sender = balance_list[0]
            transfer_reciever = balance_list[len(balance_list) - 1]
            self.balance_account(balance_list, transfer_sender, transfer_reciever)

    def run(self):
        self.a_fancy_printer.print_table_people_name(self.people.people_list_name)
        self.a_fancy_printer.print_bills(self.bills)
        self.proccess_bills()
        self.get_transferences_to_be_done()
        self.a_fancy_printer.print_summary_per_person(self.people)
        self.a_fancy_printer.print_transfers_summary(self.transfer_summary)