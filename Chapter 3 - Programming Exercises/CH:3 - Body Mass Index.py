# Write a program that calculates and displays a person's body mass index (BMI). The BMI is often used to determine
# whether a person is overweight or underweight for his or her height. A person's BMI is calculated with the following
# formula:
#                               BMI = weight x 703 / height^2
# where weight is measured in pounds and height is measured in inches. The program should ask the user to enter his or
# her wight and height, then display the user's BMI. The program should also display a message indicating whether the
# person has optimal weight, is underweight, or is overweight. A person's weight is considered to be optimal if his or
# her BMI is between 18.5 and 25. If the BMI is less than 18.5, the person is considered to be underweight. If the BMI
# is greater than 25, the person is considered to be overweight.

# Get weight and height from user
user_weight = int(input('Enter your weight (in pounds): '))
user_height = int(input('Enter your height (in inches): '))

# Calculate BMI
user_bmi = user_weight * 703 / (user_height**2)

# Decision Structure
if user_bmi > 25:
    print('Based on BMI:', format(user_bmi, '.2f'))
    print('Considered: OVERWEIGHT')
elif user_bmi < 18.5:
    print('Based on BMI:', format(user_bmi, '.2f'))
    print('Considered: UNDERWEIGHT')
else:
    print('Based on BMI:', format(user_bmi, '.2f'))
    print('Considered: OPTIMAL WEIGHT')
