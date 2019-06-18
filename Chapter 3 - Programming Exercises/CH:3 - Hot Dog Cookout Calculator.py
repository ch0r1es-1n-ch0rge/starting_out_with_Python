# Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a program that calculates the
# number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, with minimum amount of
# leftovers. The program should ask the user for the number of people attending the cookout and the number of hot dogs
# each person will be given. The program should display the following details:
#
# - The minimum number of packages of hot dogs required.
# - The minimum number of packages of hot dog buns required.
# - The number of hot dogs that will be left over.
# - The number of hot dog buns that will be left over.

# Get required information from user
attendee = int(input('Enter the number of people attending the cookout: '))
hot_dogs = int(input('Enter the number of hot dogs each person will be eating at the cookout: '))

# Decision Structure
if attendee * hot_dogs % 8 == 0 and attendee * hot_dogs % 10 == 0:
    print('Packages of hot dog buns required:', attendee * hot_dogs // 8)
    print('Packages of hot dogs required:', attendee * hot_dogs // 10)
    print('The number of hot dogs that will be left over: 0')
    print('The number of hot dog buns that will be left over: 0')
elif attendee * hot_dogs % 8 == 0 and attendee * hot_dogs % 10 != 0:
    print('Packages of hot dog buns required:', attendee * hot_dogs // 8)
    print('Packages of hot dogs required:', attendee * hot_dogs // 10 + 1)
    print('The number of hot dogs that will be left over:', (attendee * hot_dogs // 10 + 1) * 10 - attendee * hot_dogs)
    print('The number of hot dog buns that will be left over:', attendee * hot_dogs % 8)
elif attendee * hot_dogs % 8 != 0 and attendee * hot_dogs % 10 == 0:
    print('Packages of hot dog buns required:', attendee * hot_dogs // 8 + 1)
    print('Packages of hot dogs required:', attendee * hot_dogs // 10)
    print('The number of hot dogs that will be left over:', attendee * hot_dogs % 10)
    print('The number of hot dog buns that will be left over:',
          (attendee * hot_dogs // 8 + 1) * 8 - attendee * hot_dogs)
else:
    print('Packages of hot dog buns required:', attendee * hot_dogs // 8 + 1)
    print('Packages of hot dogs required:', attendee * hot_dogs // 10 + 1)
    print('The number of hot dogs that will be left over:', (attendee * hot_dogs // 10 + 1) * 10 - attendee * hot_dogs)
    print('The number of hot dog buns that will be left over:',
          (attendee * hot_dogs // 8 + 1) * 8 - attendee * hot_dogs)
