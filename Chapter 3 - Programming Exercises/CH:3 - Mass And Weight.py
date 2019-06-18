# Scientists measure an object's mass in kilograms and its weight in newtons. If you know the amount of mass of an
# object in kilograms, you can calculate its weight in newtons with the following formula:
#
#                               weight = mass x 9.8
#
# Write a program that asks the user to enter an object's mass, then calculates its weight. If the object weighs more
# than 500 newtons, display a message indicating that it is too heavy. If the object weighs less than 100 newtons,
# display a message indicating that it is too light.

# Constant Variables
HEAVY = 'Too Heavy.'
LIGHT = 'Too Light.'

# Get mass in kilograms from user
user_mass = float(input('Enter your mass in kilograms: '))

# Calculate weight in newtons
weight_in_newtons = user_mass * 9.8

# Decision Structure
if weight_in_newtons >= 500:
    print('Weight:', format(weight_in_newtons, '.2f'), 'newtons.')
    print(HEAVY)
elif weight_in_newtons <= 100:
    print('Weight:', format(weight_in_newtons, '.2f'), 'newtons.')
    print(LIGHT)
else:
    print('Your weight in newtons is...')
    print('Weight:', format(weight_in_newtons, '.2f'), 'newtons.')
