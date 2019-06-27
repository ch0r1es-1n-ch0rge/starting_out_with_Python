# Write a program that displays a table of the Celsius temperatures 0 through 20 and their Fahrenheit equivalents. The
# formula for converting a temperature from Celsius to Fahrenheit is
#                                       F = (9/5) * C + 32
# where F is the Fahrenheit, and C is the Celsius temperature. Your program must use a loop to display the table.

# Constant Variable
TEMP_RANGE = 20

# Output Temperature Table
print('Celsius\t\t Fahrenheit')
print('-' * 23)

# Repetition Structure
for celsius in range(0, TEMP_RANGE + 1):
    print(celsius, '\t\t\t', format(9 / 5 * celsius + 32, '.2f'))
