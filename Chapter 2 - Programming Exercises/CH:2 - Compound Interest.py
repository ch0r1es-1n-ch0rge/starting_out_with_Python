# When a bank account pays compound interest, it pays interest not only on the principle amount that was deposited into
# the account, but also on the interest that has accumulated over time. Suppose you wan to deposit some money into a
# savings account, and let the account earn compound interest for a certain number of years. The formula for calculating
# the balance of the account after a specified number of years is:
#
#                               A = P (1 + (r / n)^n*t
#
# The terms in the formula are:
# A is the amount of money in the account after the specified number of years.
# P is the principle amount that was originally deposited into the account.
# r is the annual interest rate.
# n is the number of times per year that interest is compounded.
# t is the specified number of years.
#
# Write a program that makes the calculation for you. The program should ask the user to input the following:
#   - The amount of principle originally deposited into the account
#   - The annual interest rate paid by the account
#   - The number of times per year that the interest is compounded (For example, if interest is compounded monthly,
#   enter 12. If interest is compounded quarterly, enter 4.)
#   - The number of years the account will be left to earn interest
#
# Once the input data has been entered, the program should calculate and display the amount of money that will be in the
# account after the specified number of years.

# Note: The user should enter the interest rate as a percentage. For example, 2 percent would be entered as 2, not as
# .02. The program will then have to divide the input by 100 to move the decimal point to the correct position.

# Get principle amount, annual interest, number of times per year, and the number of years left to earn interest
principle_amount = float(input('Enter the principle amount deposited into the account: '))
annual_interest = int(input('Enter the annual interest rate on the account: '))
times_per_year = int(input('Enter the number of times per year that the interest is compounded (For example, if '
                           'interest is compounded monthly, enter 12. If interest is compounded quarterly, enter 4): '))
number_of_years = int(input('Enter the number of years the account will be left to earn interest: '))

# Calculate is the amount of money in the account after the specified number of years
AMOUNT = principle_amount * ((1 + ((annual_interest / 100) / times_per_year)) ** (times_per_year * number_of_years))

# Display result
print('\nThe amount you will earn after ', number_of_years, ' years is $', format(AMOUNT, ',.2F'), sep='')
