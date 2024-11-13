class Account:
    def __init__(self,acc_no,balance):
        self.accnt_no = acc_no
        self.balance = balance
    
    def debit(self,amnt):
        self.balance -= amnt
    
    def credit(self,amnt):
        self.balance += amnt
    
    def print(self):
        print("Balance of account no: ",self.accnt_no," is: ",self.balance)

user1 = Account("212520",10000)
user1.debit(500)
user1.credit(1000)
user1.print()