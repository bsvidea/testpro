
class Bank:
    #magic method
    #self refers current object
    def __init__(self):  #invoked automatically whenever we can create an object.
        self.balance=0  #current object
        
    def deposit(self,amount):
        self.balance=self.balance+amount #lobject variable
        
        


x=Bank()
x.deposit(10000)
x.deposit
print(x.balance)
