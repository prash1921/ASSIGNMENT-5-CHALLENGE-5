import sys
class account:
    bank="canara bank"
def __init__(self,title=None,balance=0):
  self.title=title
  self.balance=balance
  print("welcome to bank",account bank)
   
def deposit(self,deposit):
  self.balance =self.balance+deposit
  print("balance after deposit:"self.balance)
  return self.balance

def withdrawl(self,amount):
    amount= float(input("enter amount to be withdrawn:"))
    if self.balance < amount:
        print("insufficient balance")
    else:
            self.balance=self.balance-withdrawn
            print("balance after withdraw:",self.balance)
            def get_balance(self):
                return self.balance
class savingsaccount(account):
    def__init__(self,title=none,balance=0,interestrate=0)
    super().__init__(titlt, Balance)
    self.interestrate=interestRate
    def interestamount(self):
        print("interestRate:",self.interestRate)
    s=savingsaccount("prashansha",2000,5) 
    print(s.deposit(500))
    s.withdraw(500)
    print(s.withdraw(1000))
    print(s.get_balance())
    print(s.interestrate())

        



