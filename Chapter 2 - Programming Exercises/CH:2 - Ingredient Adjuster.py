# A cookie recipe calls for the following ingredients:
#   - 1.5 cups of sugar
#   - 1 cup of butter
#   - 2.75 cups of flour
# The recipe produces 48 cookies with this amount of the ingredients. Write a program that asks the user how many
# cookies he or she wants to make, then displays the number of cups of each ingredient needed for the specified number
# of cookies.

# Initialize Constant Variables
SUGAR = 1.5
BUTTER = 1
FLOUR = 2.75
COOKIES = 48

# Get the number of cookies from user
user_cookies = int(input('Enter the number of cookies needed: '))

# Calculate the number of sugar, butter, and flour needed
user_sugar = (user_cookies / COOKIES) * SUGAR
user_butter = (user_cookies / COOKIES) * BUTTER
user_flour = (user_cookies / COOKIES) * FLOUR

# Display the number of sugar, butter, flour needed
print('For:', user_cookies, 'cookies')
print('You need!')
print('Sugar:', format(user_sugar, '.2f'), 'cup(s)')
print('Butter:', format(user_butter, '.2f'), 'cup(s)')
print('Flour:', format(user_flour, '.2f'), 'cup(s)')
