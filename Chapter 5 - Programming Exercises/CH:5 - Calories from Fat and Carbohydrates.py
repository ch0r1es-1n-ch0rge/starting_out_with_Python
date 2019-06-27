# A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her evaluation, she
# asks members for the number of fat grams and carbohydrate grams that they consume in a day. Then, she calculates the
# number of calories that results from the fat, using the following formula:
#
#                                       calories from fat = fat grams x 9
#
# Next, she calculates the number of calories that results from the carbohydrates, using the following formula:
#
#                                       calories from carbs = carb grams x 4
#
# The nutritionist asks you to write a program that will make these calculations.


# Create Main Function
def main():
    fats = int(input('Enter the number of fat (in grams) intake: '))
    carbs = int(input('Enter the number carb (in grams) intake: '))
    calories_calculation(fats, carbs)


def calories_calculation(f, c):
    fat_calories = f * 9
    carb_calories = c * 4
    print('Fat Calories:', fat_calories, 'calories')
    print('Carbohydrate Calories:', carb_calories, 'calories')


main()
