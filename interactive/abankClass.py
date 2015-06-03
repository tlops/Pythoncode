"""
 The deposit and withdraw methods each change the account balance. 
 The withdraw method also deducts a fee of 5 dollars from the balance
 if the withdrawal (before any fees) results in a negative balance.
 Since we also have the method get_fees, you will need to have a
 variable to keep track of the fees paid.

 A lesson on class
"""
class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        name = " "
        self.name = name
        self.initial_balance = initial_balance
        self.fee = 0
        
       
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.amount = amount
        self.initial_balance = amount + self.initial_balance
        return self.initial_balance
    
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        
        self.amount = amount
        self.initial_balance = self.initial_balance - amount
        if self.initial_balance >= 0:
            return self.initial_balance
        
        elif self.initial_balance < 0:
            self.initial_balance = self.initial_balance - 5
            self.fee +=5
        
        
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.initial_balance
       
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fee
    
    
    
    
    
my_account = BankAccount(10)
my_account.withdraw(15)
my_account.deposit(20)
print my_account.get_balance(), my_account.get_fees()

account1 = BankAccount(10)
account1.withdraw(15)
account2 = BankAccount(15)
account2.deposit(10)
account1.deposit(20)
account2.withdraw(20)
print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()

my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5) 
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50) 
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
print my_account.get_balance(), my_account.get_fees()


account1 = BankAccount(20)
account1.deposit(10)
account2 = BankAccount(10)
account2.deposit(10)
account2.withdraw(50)
account1.withdraw(15)
account1.withdraw(10)
account2.deposit(30)
account2.withdraw(15)
account1.deposit(5)
account1.withdraw(10)
account2.withdraw(10)
account2.deposit(25)
account2.withdraw(15)
account1.deposit(10)
account1.withdraw(50)
account2.deposit(25)
account2.deposit(25)
account1.deposit(30)
account2.deposit(10)
account1.withdraw(15)
account2.withdraw(10)
account1.withdraw(10)
account2.deposit(15)
account2.deposit(10)
account2.withdraw(15)
account1.deposit(15)
account1.withdraw(20)
account2.withdraw(10)
account2.deposit(5)
account2.withdraw(10)
account1.deposit(10)
account1.deposit(20)
account2.withdraw(10)
account2.deposit(5)
account1.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account2.deposit(10)
account2.deposit(15)
account2.deposit(20)
account1.withdraw(15)
account2.deposit(10)
account1.deposit(25)
account1.deposit(15)
account1.deposit(10)
account1.withdraw(10)
account1.deposit(10)
account2.deposit(20)
account2.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account1.deposit(10)
account2.withdraw(20)
print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()
