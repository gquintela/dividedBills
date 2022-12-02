from file_reader import *
from people import *
from fancy_printer import *


class BillManager:

    def __init__(self, people_txt="people.txt", bills_csv="bills.csv"):
        self.a_file_reader = FileReader(people_txt, bills_csv)
        self.people = People(self.a_file_reader.people_read())
        self.bills = self.a_file_reader.read_csv_bills(bills_csv)
        self.transfer_summary = []
        self.a_fancy_printer = FancyPrinter()

    def proccess_bills(self):
        for bill in self.bills:
            self.assert_person_is_in_list_of_poeple(bill)
            qty_to_be_divided = self.people.qty
            if (len(bill.people_excluded) != 0):
                # there are people excluded
                qty_to_be_divided = self.people.qty - len(bill.people_excluded)
            ammount_charged_per_person = bill.ammount / qty_to_be_divided
            # record bill in every people affected
            self.write_bill(ammount_charged_per_person, bill)

    def assert_person_is_in_list_of_poeple(self, bill):
        if bill.issuer not in self.people.people_list_name:
            print(
                f"{bill.issuer} hizo un gasto pero no figura en archivo de entrada de personas, corregir.")
            exit()

    def write_bill(self, ammount_charged_per_person, bill):
        for person in self.people.people:
            if person == bill.issuer:
                self.people.people[person].bills_paid.append(bill)
            if person not in bill.people_excluded:
                self.people.people[person].bills_to_pay.append(bill)

    def get_balance_list(self):
        balance_list = []
        for person in self.people.people:
            balance_list.append(
                [person, self.people.people[person].get_balance()])
        return balance_list

    def _get_balance(self, e):
        return e[1]

    def _get_name(self, e):
        return e[0]

    def write_summary(self, sender_name, reciever_name, ammount_to_transfer):
        self.transfer_summary.append(
            [sender_name, reciever_name, round(ammount_to_transfer, 2)])

    def _remove_if_balance_near_zero(self, balance_list, person):
        if (abs(self._get_balance(person)) < 5):
            balance_list.remove(person)

    def balance_account(self, balance_list, transfer_sender, transfer_reciever):
        sender_balance = self._get_balance(transfer_sender)
        reciever_balance = self._get_balance(transfer_reciever)
        ammount_to_transfer = min(abs(sender_balance), abs(reciever_balance))
        if (abs(sender_balance) > abs(reciever_balance)):
            # descuento el balance del ultimo al primero
            balance_list[0][1] = balance_list[0][1] + \
                self._get_balance(transfer_reciever)
            # cierra el ultimo, y lo vuelo
            balance_list.remove(transfer_reciever)
        else:
            # descuento el balance del primero al ultimo
            balance_list[len(balance_list) - 1][1] = balance_list[len(
                balance_list) - 1][1] + self._get_balance(transfer_sender)
            # cierra el primero y lo vuelo
            balance_list.remove(transfer_sender)
        self.write_summary(self._get_name(transfer_sender), self._get_name(
            transfer_reciever), ammount_to_transfer)

    def get_transferences_to_be_done(self):
        balance_list = self.get_balance_list()

        while (len(balance_list) > 0):
            balance_list.sort(key=self._get_balance)
            if (len(balance_list) == 1):
                return
            transfer_sender = balance_list[0]
            transfer_reciever = balance_list[len(balance_list) - 1]
            self.balance_account(
                balance_list, transfer_sender, transfer_reciever)

    def run(self):
        self.a_fancy_printer.print_table_people_name(
            self.people.people_list_name)
        self.a_fancy_printer.print_bills(self.bills)
        self.proccess_bills()
        self.get_transferences_to_be_done()
        self.a_fancy_printer.print_summary_per_person(self.people)
        self.a_fancy_printer.print_transfers_summary(self.transfer_summary)

    def get_people_qty(self):
        return len(self.people.people_list)
