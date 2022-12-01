from tabulate import tabulate

class FancyPrinter:
    def __init__(self) -> None:
        pass

    def print_table_people_name(self, names_list):
        print("PEOPLE INVOLVED: \n")
        print(tabulate([name] for name in names_list ))

    def print_bills(self, bills_list):
        print("\nTHE FOLLOWING BILLS WILL BE PROCCESSED: \n")
        print(tabulate(bills_list, headers=["PERSON", "AMMOUNT", "CONCEPT", "DATE", "EXCLUDED", "EXCLUDED", "EXCLUDED", "EXCLUDED"]))

    def print_summary_per_person(self, people):
        for person in people.people:
            self.print_thick_line()
            print(f"{person} summary: \n".upper())

            print(f"{person} paid:\n".upper())
            self.print_paid_bills(people.people[person].bills_paid)          
            print(f"\nTotal paid: ${sum(people.people[person].paid_list)}".upper())

            print(f"\n{person} has to pay:\n".upper())
            self.print_to_pay_bills(people.people[person].bills_to_pay)            

            print(f"\nTotal to pay (without discounting own payments): $ {round(sum(people.people[person].to_pay_list, 2))}".upper())
            print(f"\nBalance: ${round(people.people[person].balance, 2)}\n".upper())

    def print_paid_bills(self, list_of_paid_bills):
        header = ["DATE", "CONCEPT", "AMMOUNT"]
        rearranged_table = []
        for bill_paid in list_of_paid_bills:
            rearranged_table.append([bill_paid[3],bill_paid[2],f"$ {bill_paid[1]}"])
        print(tabulate(rearranged_table, headers = header))

    def print_to_pay_bills(self, list_of_paid_bills):
        header = ["DATE", "CONCEPT", "AMMOUNT", "ORIGINAL VALUE"]
        rearranged_table = []
        for bill_to_pay in list_of_paid_bills:
            rearranged_table.append([bill_to_pay[3],bill_to_pay[2],f"$ {bill_to_pay[len(bill_to_pay) - 1]}" ,  f"$ {bill_to_pay[1]}"])
        print(tabulate(rearranged_table, headers = header))

    def print_transfers_summary(self, summary_list):
        self.print_thick_line()
        print("TRANSFERS SUMMARY: \n")

        header = ["FROM", "TO", "AMMOUNT"]
        print(tabulate(summary_list, headers = header))

    def print_thick_line(self):
        print("=================================================")
        print("=================================================")
        print("=================================================\n")