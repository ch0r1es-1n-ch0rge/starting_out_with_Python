# Create a change-counting game that gets the user to enter the number of coins required to make exactly one dollar. The
# program should prompt the user to enter the number of pennies, nickles, dimes, and quarters. If the total value of the
# coins entered is equal to one dollar, the should congratulate the user for winning the game. Otherwise, the program
# should display a message indicating whether the amount entered was more than or less than one dollar.

# Constant Variables
PENNIE = 1
NICKLE = 5
DIME = 10
QUARTER = 25
DOLLAR = 100

# Get number of pennies, nickles, dimes, and quarters from user
user_penny = int(input('Enter the number of pennies you have: ')) * PENNIE
user_nickel = int(input('Enter the number of nickels you have: ')) * NICKLE
user_dime = int(input('Enter the number of dimes you have: ')) * DIME
user_quarter = int(input('Enter the number of quarters you have: ')) * QUARTER

# Decision Structure
if user_penny + user_nickel + user_dime + user_quarter > DOLLAR:
    print('Sum of coins entered:', user_penny + user_nickel + user_dime + user_quarter - DOLLAR, 'cents more than $1.')
elif user_penny + user_nickel + user_dime + user_quarter < DOLLAR:
    print('Sum of coins entered:', DOLLAR - user_penny + user_nickel + user_dime + user_quarter, 'cents less than $1.')
else:
    print('Congratulations! You won! Sum of coins entered equals $1.')
