# Write a program with a loop that asks the user to enter a series of positive numbers. The user should enter a negative
# number to signal the end of the series. After all the positive numbers have been entered, the program should display
# their sum.

# Get initial input from user
user_num = int(input('Enter positive numbers to be summed: (Enter a negative to QUIT): '))

# Initialize total
sum_total = 0

# Repetition Structure
while (user_num > 0) and user_num % 2 == 0:
    sum_total += user_num
    user_num = int(input('Enter positive numbers to be summed: (Enter a negative to QUIT): '))

# Output sum of all entered positive numbers
print('Sum of positive numbers:', sum_total)
