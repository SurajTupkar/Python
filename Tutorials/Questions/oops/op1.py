# Create Account class with 2 attributes - balance and account no
# Create methods for debit,credit & printing the balance

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.accountno=acc

    def debit(self,amm):
        self.balance=self.balance-amm
        print("Debited the amount from your acc: ",amm)
    # print("Debit ammount: ",amm)
    
    def credit(self,amm):
        self.balance=self.balance+amm
        print("Credit amount in your in account",amm)

    def prbal(self):
        print("Your current account balance is",self.balance)


ban=Account(200,123)
print("Your Account No:",ban.accountno)
ban.prbal()
ban.credit(20)
ban.prbal()

ban.debit(40)
ban.prbal()