class Bill:

    def __init__(self, date, issuer, ammount, description, people_excluded):
        self.assert_mandatory_fields(issuer, ammount, description)
        self.date = date
        self.issuer = issuer
        self.ammount = ammount
        self.description = description
        self.people_excluded = people_excluded

    def assert_mandatory_fields(self, issuer, ammount, description):
        if issuer == "" or ammount <= 0 or description == "":
            print("Campos obligatorios vacios, chequear.")
            exit()

    def __repr__(self):
        output_str = f"date: {self.date}\n\
            issuer: {self.issuer}\n\
            ammount: {self.ammount}\n\
            description: {self.description}\n\
            people_excluded: {self.people_excluded}\n"
        return output_str
