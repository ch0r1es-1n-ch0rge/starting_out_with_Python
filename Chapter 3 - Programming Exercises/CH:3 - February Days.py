# The month of February normally has 28 days. But if it is a leap year, February has 29 days. Write a program that asks
# the user to enter a year. The program should then display the number of days in February that year. Use the following
# criteria to identify leap year:
#   1. Determine whether the year is divisible by 100. If it is, then it is a leap year if and only if it is also
#      divisible by 400. For example, 2000 is a leap year, but 2100 is not.
#   2. If the year is not divisible by 100, then it is a leap year if and only if it divisible by 4. For example, 2008
#   is a leap year, but 2009 is not.

# Get the year from user
user_year = int(input('Enter a year: '))

# Decision Structure
if user_year % 400 == 0:
    print('In the year ', user_year, '.', sep='')
    print('February has 29 days.')
elif (user_year % 100 != 0) and (user_year % 4 == 0):
    print('In the year ', user_year, '.', sep='')
    print('February has 29 days.')
else:
    print('In the year ', user_year, '.', sep='')
    print('February has 28 days.')
