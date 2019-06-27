# Suppose you have a certain amount of money in a savings account that earns compound monthly interest, and you want to
# calculate the amount that you will have after a specific number of months. The formula is as follows:
#                                       F = P x (1 + i)^t
# The term in the formula are:
# - F is the future value of the account after the specified time period.
# - P is the present value of the account.
# - i is hte monthly interest rate.
# - t is the number of months.
# Write a program that prompts the user to enter the account's present value, monthly interest rate, and the number of
# months that the money will be left in the account. The program should pass these values to a function that returns the
# future value of the account, after the specified number of months. The program should display the account's future
# value.


# Create Main Function
def main():
    present_value = float(input('Enter the current value of your savings account: '))
    interest_rate = float(input('Enter the monthly interest rate: '))
    months = int(input('Enter the number of months the account will accumulate interest: '))

    if interest_rate <= .99:
        interest_rate = interest_rate
    else:
        interest_rate = interest_rate / 100

    f_val = future_value(present_value, interest_rate, months)
    print('After ', months, ' months. With an interest rate of ', interest_rate,
          ' percent. The future value of your savings account will be $', f_val, sep='')


def future_value(present, interest, time):
    return format(present * (1 + interest) ** time, ',.2f')


main()
