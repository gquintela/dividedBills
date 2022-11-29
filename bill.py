Class Bill:
    
    def __init__ (self):
        self.issuer = ""
        self.ammount = 0.0
        self.people_excluded = []
        
    def __repr__(self):
        return [self.issuer, self.ammount, self.people_excluded]
    