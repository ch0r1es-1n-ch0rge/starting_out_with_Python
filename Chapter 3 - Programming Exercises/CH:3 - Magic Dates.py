# The date June 10, 1960, is special because when it is written in the following format, the month times the day equals
# the year:
# 6/10/60
# Design a program that asks the user to enter a month (in numeric form), a day, and a two digit year. The program
# should then determine whether the month times the day equals the year. If so, it should display a message saying the
# date is magic. Otherwise, it should display a message saying the date is not magic.

# Get month, day, and year from user
user_month = int(input('Enter a month (in numeric form): '))
user_day = int(input('Enter a day (in numeric form): '))
user_year = int(input('Enter a year (last two digit): '))

# Calculate magic number
magic_num = user_month * user_day

# Decision Structure
if magic_num == user_year:
    print('The date is MAGIC.')
else:
    print('The date is NOT MAGIC.')
