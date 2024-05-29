# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest earned.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    print("--------------------------------------------")
    print("Savings and CD Account Planner and Calculator")
    print("--------------------------------------------")
    print("* This program helps you to plan and calculate the interest")
    print("  you could earn with different savings account structures.")
    print("---------------------------------------------\n")
    
    while True:
        try:
            # Prompt the user to set the savings balance, interest rate, and months for the savings account.
            savings_balance = float(input("Enter the initial balance for your savings account: "))
            savings_interest_rate = float(input("Enter the annual interest rate for your savings account (as a percentage): "))
            savings_months = int(input("Enter the number of months the funds will be held in your savings account: "))
            
            # Call the create_savings_account function and pass the variables from the user.
            updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_months)
            
            # Print out the interest earned and updated savings account balance with interest earned for the given months.
            print("\n------------------------------------------------------------------------------")
            print(f"The interest earned in {savings_months} months on your savings account would be: ${savings_interest_earned:.2f}")
            print(f"In {savings_months} months, the updated balance of your savings account would be ${updated_savings_balance:.2f}")
            print("------------------------------------------------------------------------------\n")
            break
        except ValueError:
            print("Invalid input for savings account. Please enter numeric values only for balance, interest rate, and months.")
        except Exception as e:
            print(f"An error occurred with the savings account: {e}")
            break

    while True:
        try:
            # Prompt the user to set the CD balance, interest rate, and months for the CD account.
            cd_balance = float(input("Enter the initial balance for the CD account: "))
            cd_interest_rate = float(input("Enter the annual interest rate for the CD account (as a percentage): "))
            cd_months = int(input("Enter the number of months the funds will be held in the CD account: "))
            
            # Call the create_cd_account function and pass the variables from the user.
            updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)
            
            # Print out the interest earned and updated CD account balance with interest earned for the given months.
            print("\n------------------------------------------------------------------------------")
            print(f"The interest earned in {cd_months} months on your CD account would be: ${cd_interest_earned:.2f}")
            print(f"In {cd_months} months, your updated CD account balance would be: ${updated_cd_balance:.2f}")
            print("------------------------------------------------------------------------------\n")
            break
        except ValueError:
            print("Invalid input for CD account. Please enter numeric values only for balance, interest rate, and months.")
        except Exception as e:
            print(f"An error occurred with the CD account: {e}")
            break
        
if __name__ == "__main__":
    main() # Call the main function.