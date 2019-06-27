# One foot equals 12 inches. Write a program named feet_to_inches that accepts a number of feet as an argument and
# returns the number os inches in that many feel. Use the function in a program that prompts the user to enter a number
# of feet then displays the number of inches in that many feet.

# Create Main Function
def main():
    user_feet = float(input('Enter the number of feet to be converted to inches: '))
    feet_to_inches(user_feet)


def feet_to_inches(feet):
    inches_conversion = feet * 12
    print('Feet:', feet, 'feet')
    print('Converting...')
    print('Inches:', inches_conversion, 'inches')


main()
