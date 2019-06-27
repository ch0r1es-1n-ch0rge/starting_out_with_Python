# Write a program that uses nested loops to draw this pattern:
#
# * * * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# Initialize Base Size
BASE_SIZE = 8

# Repetition Structure
for row in range(BASE_SIZE, 1, -1):
    for column in range(row - 1):
        print('* ', end='')
    print()

