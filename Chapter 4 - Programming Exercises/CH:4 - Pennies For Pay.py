# Write a program that calculates the amount of money a person would earn over a period of time if his or her salary is
# one penny the first day, two pennies the second day, and continues to double each day. The program should ask the user
# for the number of days. Display a table showing what the salary was for each day, then show the total pay at the end
# of the period. The output should be displayed in a dollar amount, not the number of pennies.

# Get the number of days from user
user_days = int(input('Enter the number of days of pay: '))

# Output Day and Salary Table
print('Day\t\tSalary')
print('-' * 23)

# Initialize total
total_salary = 0

# Repetition Structure
for day in range(1, user_days + 1):
    user_salary = 0.01 * 2 ** (day - 1)
    print(day, '\t\t', format(user_salary, ',.2f'))
    total_salary += user_salary

# Output total pay
print('\nIn', user_days, 'day(s).')
print('Total Pay: $', format(total_salary, ',.2f'), ' dollars', sep='')
