# A car's miles-per-gallon (MPG) can be calculated with the following formula:
#                           MPG = Miles driven / Gallons of gas used
# Write a program that asks the user for the number miles driven and the gallons of gas used. It should calculate the
# car's MPG and display the result.

# Get miles driven from the user
miles_driven = float(input('Enter the amount of miles driven: '))

# Get gallons of gas used from the user
gallons_used = float(input('Enter the amount of gas in gallons used: '))

# Calculate: Miles-Per-Gallon (MPG)
miles_per_gallon = miles_driven / gallons_used

# Display results
print('You car is getting', format(miles_per_gallon, '.2f'), 'miles to the gallon.')
