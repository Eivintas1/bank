# Evan Aleinikovas Task 3
# create online banking application using OOP 
# for company Fortuna investments & trading ltd

import unittest

# Base class for Bank Account
class BankAccount:
    def __init__(self, accountNumber, accountBalance):
        self.accountNumber = accountNumber
        self.accountBalance = accountBalance

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid amount"
        self.accountBalance += amount
        return self.accountBalance
    
    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid amount"
        if amount > self.accountBalance:
            return "Insufficient funds"
        self.accountBalance -= amount
        return self.accountBalance
    
    def checkBalance(self):
        return self.accountBalance
    
# child class for Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, accountNumber, accountBalance, interestRate = 5.0):
        super().__init__(accountNumber, accountBalance)
        self.interestRate = interestRate

    def calculateInterest(self):
        return self.accountBalance * self.interestRate / 100

    def applyInterest(self):
        interest = self.calculateInterest()
        self.accountBalance += interest
        return interest
    
# child class for Current Account
class CurrentAccount(BankAccount):
    def __init__(self, accountNumber, accountBalance, transactionFee = 2.50):
        super().__init__(accountNumber, accountBalance)
        self.transactionFee = transactionFee

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid amount"
        totalAmount = amount + self.transactionFee
        if totalAmount > self.accountBalance:
            return "Insufficient funds"
        
        self.accountBalance -= totalAmount
        return self.accountBalance
    
#main program for payment processing system
def main():
    print("=============================================================")
    print("Fortuna Investments & Trading Ltd - Payment Processing System")
    print("=============================================================")

# User selects account type
    print("Select account type:")
    print("1. Savings Account")
    print("2. Current Account")

    choice = input("Enter choice (1 or 2): ")

    accountNumber = input("Enter Account Number: ")
    accountBalance = float(input("Enter Initial Balance: "))

    if choice == "1":
        print("An interest rate of 5% will be applied to your savings account.")
        account = SavingsAccount(accountNumber, accountBalance, interestRate = 5.0)

    elif choice == "2":
        print("A transaction fee of $2.50 will be applied on each withdrawal.")
        account = CurrentAccount(accountNumber, accountBalance, transactionFee = 2.50)
    else:
        print("Invalid choice. Exiting.")
        return
    
    while True:
        print("\nSelect operation:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Calculate Interest (Savings Account only) ")
        print("5. Exit")
        
        operation = input("Enter choice (1-5): ")

        if operation == "1":
            amount = float(input("Enter deposit amount: "))
            newBalance = account.deposit(amount)
            print("New balance after deposit: ", newBalance)

        elif operation == "2":
            amount = float(input("Enter withdrawal amount: "))
            newBalance = account.withdraw(amount)
            print("New balance after withdrawal: ", newBalance)

        elif operation == "3":
            balance = account.checkBalance()
            print("Current balance: ", balance)

        elif operation == "4":
            if isinstance(account, SavingsAccount):
                interest = account.calculateInterest()
                print("Calculated interest: ", interest)
            else:
                print("Interest calculation is only available for Savings Accounts.")

        elif operation == "5":
            print("Exiting. Thank you for banking with Fortuna Investments & Trading Ltd.")
            break
    
main()

# Unit tests for the banking application
class TestBankingApplication(unittest.TestCase):
    
    def test001(self):
        account = BankAccount("12345", 1000)
        self.assertEqual(account.deposit(500), 1500)

    def test002(self):
        account = BankAccount("12345", 1000)
        self.assertEqual(account.withdraw(300), 700)

    def test003(self):
        account = SavingsAccount("54321", 2000, interestRate=5.0)
        self.assertEqual(account.calculateInterest(), 100)
    
unittest.main()

    