class Account:
    accountName = "Sam"
    accountBalance = 1000000
    accountNumber = 2323222234
    def __init__(self):
        self.accountBalance
        self.accountName
        self.accountNumber
    def deposit(self, amount):
        self.accountBalance = self.accountBalance + amount
        return f"Your new amount is {self.accountBalance}"
    def withdraw(self, amount):
        self.accountBalance = self.accountBalance - amount
        return f"Your current account balance is now {self.accountBalance}"