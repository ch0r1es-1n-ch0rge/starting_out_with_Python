# The color red, blue, and yellow are known as the primary colors because they cannot be made by mixing other colors.
# When you mix two primary colors, you get a secondary color, as shown here:
#       When you mix red and blue, you get purple.
#       When you mix red and yellow, you get orange.
#       When you mix blue and yellow, you get green.
# Design a program that prompts the user to enter the names of two primary colors to mix. If the user enters anything
# other than "red," "blue," or "yellow," the program should display an error message. Otherwise, the program should
# display the name of the secondary color that results.

# Get primary colors from user
user_primary1 = input('Enter a primary color to mix (red, blue or yellow): ')
user_primary2 = input('Enter another primary color to mix (red, blue, or yellow): ')

# Decision Structure
if (user_primary1.capitalize() == 'Red' and user_primary2.capitalize() == 'Blue') or \
        (user_primary1.capitalize() == 'Blue' and user_primary2.capitalize() == 'Red'):
    print('Primary Colors:', user_primary1, 'and', user_primary2)
    print('makes...')
    print('Secondary Color: Purple')
elif (user_primary1.capitalize() == 'Red' and user_primary2.capitalize() == 'Yellow') or \
        (user_primary1.capitalize() == 'Yellow' and user_primary2.capitalize() == 'Red'):
    print('Primary Colors:', user_primary1, 'and', user_primary2)
    print('makes...')
    print('Secondary Color: Orange')
elif (user_primary1.capitalize() == 'Blue' and user_primary2.capitalize() == 'Yellow') or \
        (user_primary1.capitalize() == 'Yellow' and user_primary2.capitalize() == 'Blue'):
    print('Primary Colors:', user_primary1, 'and', user_primary2)
    print('makes...')
    print('Secondary Color: Green')
else:
    print('Error...')
