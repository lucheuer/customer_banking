""" Create an Account class with methods"""

class Account:
    """Class representing a bank account"""
    
    def __init__(self, balance, interest):
        """Initialize an account object with a balance and interest"""
        self.balance = balance
        self.interest = interest

    def set_balance(self, balance):
        """Sets the balance for the account"""
        self.balance = balance
        
    def get_balance(self):
        """Get the current balance of the account."""
        return self.balance

    def set_interest(self, interest):
        """Set the interest rate for the account"""
        self.interest = interest
    
    def get_interest(self):
        """Get the interest rate of the account."""
        return self.interest
