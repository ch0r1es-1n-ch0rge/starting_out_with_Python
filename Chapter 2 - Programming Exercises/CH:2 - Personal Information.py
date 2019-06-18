# 1. Personal Information
# Write a program that displays the following information:
#   - Your name
#   - Your address, with city, state, and ZIP
#   - Your telephone number
#   - Your college major

# Get name
user_name = input('Full Name: ')

# Get address
address = input('Address: ')
city = input('City: ')
state = input('State: ')
zip_code = int(input('ZIP Code: '))

# Get telephone number
user_phone_number = int(input('Telephone Number: '))

# Get college major
college_major = input('College Major: ')

# Display user information
print('Name: ', user_name)
print('Address: ', address, ',', city, ',', state, ',', zip_code)
print('Phone: ', user_phone_number)
print('College Major: ', college_major)
