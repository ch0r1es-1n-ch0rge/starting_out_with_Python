# In mathematics, the notation n! represents the factorial of the nonnegative integer n. The factorial of n is the
# product of all the nonnegative integers from 1 to n. For example,
#
#                               7! = 1 x 2 x 3 x 4 x 5 x 6 x7 = 5,040
# and
#
#                               4! = 1 x 2 x 3 x 4 = 24
#
# Write a program that lets the user enter a nonnegative integer then uses a loop to calculate the factorial of that
# number. Display the factorial.

# Get nonnegative integer from user
starting_nonnegative = int(input('Enter a nonnegative integer: '))

# Initiate factorial
factorial = 1

# Repetition Structure
for num in range(2, starting_nonnegative + 1):
    factorial *= num

# Output the factorial
print()
print('Factorial of:', starting_nonnegative, 'is', format(factorial, ',.2f'))
