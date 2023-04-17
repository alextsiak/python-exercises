"""
For this challenge, create a bank account class that has two attributes:

    owner
    balance

and two methods:

    deposit
    withdraw

As an added requirement, withdrawals may not exceed the available balance.
"""

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit accepted. New balance: {self.balance}")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Sorry, but you don't have enough funds to do that. Current balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrawal accepted. New balance: {self.balance}")