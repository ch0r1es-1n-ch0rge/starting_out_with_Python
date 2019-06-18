# Write a program tha asks the user for a number in the range of 1 through 7. The program should display the
# corresponding day of the week,  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday,
# and 7 = Sunday. The program should display an error message if the user enters a number that is outside the range of 1
# through 7.

# Initialize Constants
MONDAY = 'Monday'
TUESDAY = 'Tuesday'
WEDNESDAY = 'Wednesday'
THURSDAY = 'Thursday'
FRIDAY = 'Friday'
SATURDAY = 'Saturday'
SUNDAY = 'Sunday'

# Get input from user
user_selection = int(input('Enter a number from 1 through 7: '))

# Display corresponding day of the week
if user_selection == 1:
    print(MONDAY)
elif user_selection == 2:
    print(TUESDAY)
elif user_selection == 3:
    print(WEDNESDAY)
elif user_selection == 4:
    print(THURSDAY)
elif user_selection == 5:
    print(FRIDAY)
elif user_selection == 6:
    print(SATURDAY)
elif user_selection == 7:
    print(SUNDAY)
else:
    print('Error input out of range.')