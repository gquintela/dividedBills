from person import *

class People:
    
    def __init__ (self, people_list):
        self.people_list_name = people_list
        self.people = {}
        self.qty = 0
        self.populate()

    def populate (self):
        for person in self.people_list_name:
            self.people[person] = Person(person)
            self.qty = self.qty + 1
        return self.people
        
    def __str__(self):
        for person in self.people_list:
            print(person)
            
    def __repr__(self):
        return self.people_list
