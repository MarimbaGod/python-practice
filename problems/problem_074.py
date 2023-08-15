# Write a class that meets these requirements.
#
# Name:       BankAccount
#
# Required state:
#    * opening balance, the amount of money in the bank account
#
# Behavior:
#    * get_balance()      # Returns how much is in the bank account
#    * deposit(amount)    # Adds money to the current balance
#    * withdraw(amount)   # Reduces the current balance by amount
#
# Example:
#    account = BankAccount(100)
#
#    print(account.get_balance())  # prints 100
#    account.withdraw(50)
#    print(account.get_balance())  # prints 50
#    account.deposit(120)
#    print(account.get_balance())  # prints 170

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        # self.balance = self.balance + amount   #OR THIS WORKS
        #needed the +=

    def withdraw(self, amount):
        self.balance -= amount


#test
# account = BankAccount(100)
# account.deposit(50)

# print(account.get_balance())










#
# There is pseudocode for you to guide you.

# class BankAccount
    # method initializer(self, balance)
        # self.balance = balance

    # method get_balance(self)
        # returns the balance

    # method withdraw(self, amount)
        # reduces the balance by the amount

    # method deposit(self, amount)
        # increases the balance by the amount



# code along. THIS ONE HAS THE IF STATEMENT FOR OVERDRAFT
# class BankAccount:
#     def __init__(self, opening_balance):
#         # self.opening_balance = opening_balance
#         self.total = opening_balance

#     def get_balance(self):
#         return self.total

#     def withdraw(self, amount):
#         if amount > self.total:
#             Print("You too broke D:")
#         else:
#             self.total -= amount
#             print(self.total)

#     def deposit(self, amount):
#         self.total += amount
#         print(self.total)
