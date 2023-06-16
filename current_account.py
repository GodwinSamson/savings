from Account import Account
class CurrentAccount(Account):
    def __init__(self):
        Account.__init__(self)
        self.withdraw_count = 0

    def withdrawal(self, amount):
        if self.withdraw_count >= 10:
            return "You have reached your daily withdrawal limit"
        elif amount > 5000:
            return "You are trying to spend above your daily limit"
        else:
            self.withdraw_count += 1
            return super().withdraw(amount)
amount = int(input("Enter an amount to withdraw:\n"))
currentAccount = CurrentAccount()
print(currentAccount.withdrawal(amount))

