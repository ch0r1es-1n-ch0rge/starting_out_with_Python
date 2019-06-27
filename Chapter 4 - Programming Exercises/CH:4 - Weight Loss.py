# If a moderately active person cuts their calorie intake by 500 calories a day, they can typically lose about 4 pounds
# a month. Write a program that lets the user enter their starting weight, then creates and displays a table showing
# what their expected weight will be at the end of each month for the next 6 months if they stay on this diet.

# Get starting weight from user
starting_weight = float(input('Enter your starting weight: '))

# Output table
print('Month\t\t Weight')
print('-' * 19)

# Repetition Structure
for month in range(1, 7):
    print(month, '\t\t\t', starting_weight)
    starting_weight -= 4
