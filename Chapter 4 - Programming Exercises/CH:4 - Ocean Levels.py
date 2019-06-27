# Assuming the ocean's level is currently rising at about 1.6 millimeters per year, create an application that displays
# the number of millimeters that the ocean will have risen each year for the next 25 years.

# Output table
print('Year\t\t Risen Ocean Levels (in millimeters)')
print('-' * 48)

# Repetition Structure
for year in range(1, 26):
    print(year, '\t\t\t', format(year * 1.6, '.2f'), 'millimeters')
