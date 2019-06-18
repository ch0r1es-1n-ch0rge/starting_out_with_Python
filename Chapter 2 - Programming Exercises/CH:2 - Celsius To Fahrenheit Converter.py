# Write a program that converts Celsius temperatures to Fahrenheit temperatures. The formula is as follows:
#                                           F = (9/5)C + 32
# The program should ask the user to enter a temperature in Celsius, then display the temperature converted to
# Fahrenheit.

# Get the temperature in Celsius from the user
user_temp = float(input('Enter the temperature in Celsius: '))

# Calculate the conversion of Celsius to Fahrenheit
c_to_f = ((9 / 5) * user_temp) + 32

# Display the result of the conversion
print('Input Temperature:', user_temp, 'Celsius')
print('Converting...')
print('Conversion Temperature:', format(c_to_f, '.1f'), 'Fahrenheit')
