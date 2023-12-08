import math

'''SCRIPT FUNCTION: To calculate either Investment Gains or Bond Monthly Repayments'''

def investment():
    while True:
        try:
            # Prompt user for investment information
            money_deposited = float(input('Enter the amount of money that they are depositing\n> ')) # Money Deposited
            interest_rate = float(input('Enter the interest rate(%):\n> ')) / 100 # Interest Rate
            num_years = float(input('Enter the term/duration of investment(years):\n> ')) # Number of Years

            print('Please select COMPOUND or SIMPLE to see Total Amount after investment')
            interest = input('(Type the option word to select)\n> ') # Interest Type

        except Exception as e:
            print(f'Oops something went wrong: {e}\nTry again!')
            continue

        # Calculate Investment based on Interest type
        if interest.lower() == 'compound':
            # Calculations for Compound Interest
            a = math.pow(1 + interest_rate, num_years)
            total_amount = money_deposited*a
            print(f'[COMPOUND] Your total amount after investment will be: R {round(total_amount, 2)}')
            break            
        elif interest.lower() == 'simple':
            # Calculations for Simple Interest
            a = 1 + interest_rate*num_years
            total_amount = money_deposited*a
            print(f'[SIMPLE] Your total amount after investment will be: R {round(total_amount, 2)}')       
            break     
        else:
            print('\nOOPS, That was not a valid option please try again...')
            continue        
    # Return back to Main Menu
    print('Enter any key to continue...')
    input()
    return menu()

def bond():
     while True:
        try:
            # Prompt user for investment information
            house_value = float(input('Enter the present value of house\n> ')) # House Value
            interest_rate = float(input('Enter the interest rate(%):\n> ')) / 100 # Interest Rate
            num_months = float(input('Enter the duration taken to repay bond(months):\n> ')) # Number of Months

        except Exception as e:
            print(f'Oops something went wrong: {e}\nTry again!')
            continue

        # Calculate repayment total amount
        x = (interest_rate*house_value)
        y = (1 - math.pow(1 + interest_rate, -num_months))
        total_amount = x / y
        print(f'[BOND REPAYMENTS] Monthly Repayments will be - R {round(total_amount, 2)} p/month')

        # Return back to Main Menu
        print('Enter any key to continue...')
        input()
        return menu()
     
def menu():
    # Menu Content
    _menu = '''
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan

Enter either 'investment' or 'bond' from the menu above to proceed:
'''
    while True:
        # Get user's selection
        user_selection = input(_menu)

        # Determine users's selection
        if user_selection.lower() == 'investment':
            print('SELECTED OPTION: "Investment" ...')
            investment()
        elif user_selection.lower() == 'bond':
            print('SELECTED OPTION: "Bond" ...')
            bond()
        else:
            print('Invalid Option, Try Again!')
            continue
menu()
# EOF - Branden v Staden