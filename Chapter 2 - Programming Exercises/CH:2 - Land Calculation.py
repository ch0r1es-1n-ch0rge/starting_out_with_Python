# . Land Calculation
# One acre of land is equivalent to 43,560 square feet. Write a program that asks the user to enter the total square
# feet in a tract of land and calculates the number of acres in the tract.
# Hint: Divide the amount entered by 43,560 to get the number of acres.

# Constant Variable
ONE_ACRE = 43560

# Get the total square feet of tract
square_feet = int(input('Enter the total square feet of tract: '))

# Acre Calculation
acres = square_feet / ONE_ACRE

# Output Calculation
print(square_feet, 'square feet of tract is equivalent to', format(acres, ',.2f'), 'acres of tract.')
