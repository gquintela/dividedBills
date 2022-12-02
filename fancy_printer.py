from tabulate import tabulate


class FancyPrinter:
    def __init__(self) -> None:
        pass

    def print_table_people_name(self, names_list):
        print("PEOPLE INVOLVED: \n")
        print(tabulate([name] for name in names_list))

    def print_bills(self, bills_list):
        print("\nTHE FOLLOWING BILLS WILL BE PROCCESSED: \n")
        bills_for_printing = []
        for bill in bills_list:
            formatted_ammount = self.format_for_currency(bill.ammount)
            formatted_people_excluded = ""
            if len(bill.people_excluded) > 0:
                for person in bill.people_excluded:
                    formatted_people_excluded = formatted_people_excluded + " " + person
            bill_for_printing = [
                bill.date, bill.issuer, formatted_ammount, bill.description, formatted_people_excluded]
            bills_for_printing.append(bill_for_printing)
        print(tabulate(bills_for_printing, headers=[
              "DATE", "ISSUER", "AMMOUNT", "DESCRIPTION", "EXCLUDED", "EXCLUDED", "EXCLUDED", "EXCLUDED"]))

    def format_for_currency(self, ammount):
        return "$ " + str("{:.2f}".format(ammount))

    def print_summary_per_person(self, people):
        for person in people.people:
            self.print_thick_line()
            print(f"{person} summary: \n".upper())

            print(f"{person} paid:\n".upper())
            self.print_paid_bills(people.people[person].bills_paid)
            print(
                f"\nTotal paid: {self.format_for_currency(people.people[person].sum_of_bills_paid())}".upper())

            print(f"\n{person} has to pay:\n".upper())
            self.print_to_pay_bills(
                people.people[person].bills_to_pay, people.qty)

            print(
                f"\nTotal to pay (without discounting own payments): {self.format_for_currency(people.people[person].sum_of_bills_to_pay())}".upper())
            print(
                f"\nBalance: {self.format_for_currency(people.people[person].get_balance())}\n".upper())

    def print_paid_bills(self, list_of_paid_bills):
        header = ["DATE", "DESCRIPTION", "AMMOUNT"]
        rearranged_table = []
        for bill_paid in list_of_paid_bills:
            rearranged_table.append(
                [bill_paid.date, bill_paid.description, self.format_for_currency(bill_paid.ammount)])
        print(tabulate(rearranged_table, headers=header))

    def print_to_pay_bills(self, list_of_paid_bills, people_qty):
        header = ["DATE", "DESCRIPTION", "AMMOUNT", "ORIGINAL VALUE"]
        rearranged_table = []
        for bill_to_pay in list_of_paid_bills:
            ammount_to_pay = bill_to_pay.ammount / \
                (people_qty - len(bill_to_pay.people_excluded))  # polemico
            rearranged_table.append(
                [bill_to_pay.date, bill_to_pay.description, self.format_for_currency(ammount_to_pay),  self.format_for_currency(bill_to_pay.ammount)])
        print(tabulate(rearranged_table, headers=header))

    def print_transfers_summary(self, summary_list):
        self.print_thick_line()
        print("TRANSFERS SUMMARY: \n")
        header = ["FROM", "TO", "AMMOUNT"]
        rearranged_table = []
        for transfer in summary_list:
            rearranged_table.append(
                [transfer[0], transfer[1], self.format_for_currency(transfer[2])])
        print(tabulate(rearranged_table, headers=header))

    def print_thick_line(self):
        print("=================================================")
        print("=================================================")
        print("=================================================\n")
