class BankAccount():
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,credit):
        self.balance+=credit
    def withdraw(self,debit):
        if debit>self.balance:
            print("indufucinet balance")
        else:
            self.balance-=debit
            print(f"{debit} is debited")
    def showbalance(self):
        print(self.balance)

customer1=BankAccount("sameer",100000)
customer1.showbalance()
customer1.deposit(20000)
customer1.withdraw(70000)
customer1.showbalance()