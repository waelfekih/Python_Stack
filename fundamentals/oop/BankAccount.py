class BankAccount:
    
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
        
    def withdraw(self, amount):
        
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
        else :
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        return self
        
    def display_account_info(self):
        print(f"Your Account Balance is: {self.balance} " )
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
        

acc1 = BankAccount(.01 , 1000)
acc2 = BankAccount(.025 , 2500)

acc1.deposit(120).deposit(50).deposit(75).withdraw(450).yield_interest().display_account_info()
acc2.deposit(1200).deposit(1500).withdraw(1000).withdraw(600).withdraw(200).withdraw(2500).yield_interest().display_account_info()





    

    
    





