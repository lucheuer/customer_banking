"""Import the Account class from the Account.py file."""
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        float: The interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    cd_account = Account(balance, 0) #Initialize with interest as 0

    # Calculate interest earned
    interest_earned = balance * (interest_rate / 100 * months / 12)

    # Update the CD account balance by adding the interest earned
    updated_balance = balance + interest_earned

    # Update the account balance
    cd_account.set_balance(updated_balance)

    # You can change the interest rate here, although it is not used for calculating the balance.
    cd_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return updated_balance, interest_earned
