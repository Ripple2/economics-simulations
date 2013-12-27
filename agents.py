class Agent():
    def __init__(self):
        self.wage = 1
        self.cash = 0
        self.demand = 1
        self.productivity = 1
        self.company = None

    def seek_employment(self,company):
        self.company = company
        self.wage = self.company.wage

    def work(self): #Interaction between worker and company!
        produce = self.productivity 
        self.company.stock += produce
        self.company.cash -= self.company.wage
        self.cash += self.company.wage

    def spend(self):
        consumption = self.demand * self.company.price
        self.cash -= consumption
        self.company.cash = consumption
        self.company.stock -= self.demand


class Company():
    def __init__(self):
        self.stock = 0
        self.cash = 0
        self.wage = 1
        self.output = 1
        self.price = 1

    def set_output(self):
        pass

    def set_wage(self):
        pass

