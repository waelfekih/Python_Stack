class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount( 0)

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self
    
    def make_yield(self, int_rate):
        self.account.yield_interest(int_rate)
        return self

    def display_user_balance(self):
        print(self.name , self.email)
        self.account.display_account_info()
        return self
        


class BankAccount:
    
    def __init__(self, balance): 
        #self.int_rate = int_rate
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
        print(f" balance: {self.balance}")
        
    
    def yield_interest(self, int_rate):
        if self.balance > 0:
            self.balance += (self.balance * int_rate)
        return self

gabriel = User("gabriel" , "gabriel@gmail.com")
gabriel.make_deposit(500).make_deposit(250).make_withdrawal(175).make_yield(0.02).display_user_balance()