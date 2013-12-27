from agents import *


#stats functions
def stats(when):
    print when, "Agent Cash =",agent.cash,"Company Cash =",company.cash, "Company Stock =", company.stock
    return ""
#populate the world




agent = Agent()
company = Company()


for i in range(5):
    
    agent.seek_employment(company)

    agent.work()
    print stats("Stats after working:")
    agent.spend()
    print stats ("Stats after spending:")

    company.set_output()
    company.set_wage()


