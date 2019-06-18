# On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are as follows:
#   - Pocket 0 is green.
#   - For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered pockets are black.
#   - For pockets 11 through 18. the odd-numbered pockets are black and the even-numbered pockets are red.
#   - For pockets 19 through 28. the odd-numbered pockets are red and the even-numbered pockets are black.
#   - For pockets 29 through 36. the odd-numbered pockets are black and the even-numbered pockets are red.
# Write a program that asks the user to enter a pocket number and displays whether the pocket is green, red, or black.
# The program should display an error message if the user enters a number that is outside the range of 0 through 36.

# Get pocket number from user
pocket_num = int(input('Enter a pocket number in the range of 0 through 36: '))

# Decision Structure
if pocket_num == 0:
    print('Green')
elif 1 >= pocket_num <= 10:
    if pocket_num % 2 == 0:
        print('Black')
    else:
        print('Red')
elif 11 >= pocket_num <= 18:
    if pocket_num % 2 == 0:
        print('Red')
    else:
        print('Black')
elif 19 >= pocket_num <= 28:
    if pocket_num % 2 == 0:
        print('Black')
    else:
        print('Red')
elif 29 >= pocket_num <= 36:
    if pocket_num % 2 == 0:
        print('Red')
    else:
        print('Black')
else:
    print('Error...', pocket_num, ' is outside the range of 0 through 36.', sep='')
