class account:
    def __init__(self,balance,accnum):
        self.balance=balance
        self.accnum=accnum


    # debit

    def debit(self,amount):
        self.balance -= amount
        print("Rs" ,amount, "is debited from ur account")
        print("the total balance is", self.get_bal())

     #credit
    def credit(self,amount):
        self.balance  += amount
        print("Rs" , amount,  "is credited to ur account")
        print("the total balnce is " , self.get_bal())

    #total bal call

    def get_bal(self):
       return self.balance

acc1=account(10000,2341)
print(acc1.balance, acc1.accnum)
acc1.debit(500)
acc1.credit(1000)



