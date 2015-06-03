class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        name = "Tolu"
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


def Users ():
        cust = ["my_account", "account1", "account2" ]
        trans_holder = dict()
        cust_holder = dict()
        filename = raw_input("Enter the file that contains the operations: ")
        if len(filename) < 1: filename = "bankOp.txt"
        fhandler = open(filename)
        for line in fhandler:
                line = line.rstrip()
                words = line.split('.')
                user = words[0]
                transaction = words[1] #.split.('(')
                transaction = transaction.split('(')[0]
                trans_holder[transaction]=trans_holder.get(transaction,0) + 1#transaction
                cust_holder[user]=cust_holder.get(user,0) + 1#transaction
        print trans_holder
        print cust_holder


Users()
account1 = BankAccount(20)
account2 = BankAccount(10)
my_account = BankAccount(10)



print my_account.get_balance(), my_account.get_fees()


print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()
