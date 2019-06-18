# Write a program that prompts the user to enter a number within the range of 1 through 10. The program should display
# the Roman numeral version of that number. If  the number is outside the range of 1 through 10, the program should
# display an error message. The following table shows the Roman numerals for the numbers 1 through 10:
#
#   Number      Roman Numeral
# -----------------------------
#   1           I
#   2           II
#   3           III
#   4           IV
#   5           V
#   6           VI
#   7           VII
#   8           VIII
#   9           IX
#   10          X

# Constant Variables
ONE = 'I'
TWO = 'II'
THREE = 'III'
FOUR = 'IV'
FIVE = 'V'
SIX = 'VI'
SEVEN = 'VII'
EIGHT = 'VIII'
NINE = 'IX'
TEN = 'X'

# Get input from user
user_num = int(input('Enter a number from 1 through 10: '))

# Decision Structure
if user_num == 1:
    print('You entered', user_num)
    print('The Roman Numeral equivalent is...')
    print('Roman Numeral:', ONE)
elif user_num == 2:
    print('You entered', user_num)
    print('The Roman Numeral equivalent is...')
    print('Roman Numeral:', TWO)
elif user_num == 3:
    print('You entered', user_num)
    print('The Roman Numeral equivalent is...')
    print('Roman Numeral:', THREE)
elif user_num == 4:
    print('You entered', user_num)
    print('The Roman Numeral equivalent is...')
    print('Roman Numeral:', FOUR)
elif user_num == 5:
    print('You entered', user_num)
    print('The Roman Numeral equivalent is...')
    print('Roman Numeral:', FIVE)
elif user_num == 6:
    print('You entered', user_num)
    print('The Roman Numeral equivalent is...')
    print('Roman Numeral:', SIX)
elif user_num == 7:
    print('You entered', user_num)
    print('The Roman Numeral equivalent is...')
    print('Roman Numeral:', SEVEN)
elif user_num == 8:
    print('You entered', user_num)
    print('The Roman Numeral equivalent is...')
    print('Roman Numeral:', EIGHT)
elif user_num == 9:
    print('You entered', user_num)
    print('The Roman Numeral equivalent is...')
    print('Roman Numeral:', NINE)
elif user_num == 10:
    print('You entered', user_num)
    print('The Roman Numeral equivalent is...')
    print('Roman Numeral:', TEN)
else:
    print('ERROR!!! Your input is outside the range of 1 through 10.')
