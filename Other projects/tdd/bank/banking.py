class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Invalid withdrawal amount.")

    def get_balance(self):
        return self.balance