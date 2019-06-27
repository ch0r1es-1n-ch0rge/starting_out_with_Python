# Write a program that asks the user to enter the amount that he or she has budgeted for a month. A loop should then
# prompt the user to enter each of his or her expenses for the month and keep a running total. When the loop finishes,
# the program should display the amount that the user is over or under budget.

# Get initial budget from user
user_budget = float(input('Enter your budget: '))

# Initialize total
total = 0

# Initialize sentinel value
keep_going = 'Y'

# Repetition Structure
while keep_going.upper() == 'Y':
    monthly_expenses = float(input('Enter an expense: '))
    total += monthly_expenses
    keep_going = input('Do you wish to input more expenses? (Y for Yes or N for No): ')

# Decision Structure
if (user_budget - total) == 0:
    print('Budget:', user_budget)
    print('Monthly Expenses:', total)
    print('You are exactly at budgeted amount.')
elif total > user_budget:
    print('Budget:', user_budget)
    print('Monthly Expenses:', total)
    print('You are over your budgeted amount by: $', format(total - user_budget, ',.2f'), ' dollars.', sep='')
else:
    print('Budget:', user_budget)
    print('Monthly Expenses:', total)
    print('You are under your budgeted amount by: $', format(user_budget - total, ',.2f'), ' dollars.', sep='')
