import unittest
from banking import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("123", 100)

    def test_initial_balance(self):
        self.assertEquals(self.account.get_balance(), 100, "Idk man something happened")
        
    def test_deposit(self):
        self.account.deposit(50)
        self.assertEquals(self.account.get_balance(), 150, "Deposit unsuccessful")

    def test_withdraw(self):
        self.account.withdraw(50)
        self.assertEquals(self.account.get_balance(), 50, "Withdrawal unsuccessful")
        
    def test_invalid_withdrawal(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(5000)
        self.assertEquals(str(context.exception), "Invalid withdrawal amount.")
        
    def test_negative_deposit(self):
        with self.assertRaises(ValueError) as context:
            self.account.deposit(-5)
        self.assertEquals(str(context.exception), "Deposit amount must be greater than zero.")
        
    def tearDown(self):
        super().tearDown()
        
if __name__ == '__main__':
    unittest.main()