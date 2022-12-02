from person import *


class People:

    def __init__(self, people_list):
        self.people_list_name = people_list
        self.people = {}
        self.qty = 0
        self.populate()
        self.set_people_number_in_group_for_all_people()

    def populate(self):
        for person in self.people_list_name:
            self.people[person] = Person(person)
            self.qty = self.qty + 1
        return self.people

    def get_people_qty(self):
        return self.qty

    def set_people_number_in_group_for_all_people(self):
        for person in self.people_list_name:
            self.people[person].people_qty_in_group = self.qty

    def __str__(self):
        for person in self.people_list:
            print(person)

    def __repr__(self):
        return self.people_list
