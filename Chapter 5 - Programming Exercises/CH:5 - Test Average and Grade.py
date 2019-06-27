# Write a program that asks the user to enter five test scores. The program should display a letter grade for each score
# and the average test score. Write the following functions in the program:
# - calc_average. This function should accept five test scores as arguments and return the average of the scores.
# - determine_grade. This function should accept a test score as an argument and return a letter grade for the score
# based on the following grade scale:
#
#       Score                   Letter Grade
#       ------------------------------------
#       90 - 100                    A
#       80 - 89                     B
#       70 - 79                     C
#       60 - 69                     D
#       Below 60                    F


# Create Main Function
def main():
    test_one = float(input('Enter score for test one: '))
    test_two = float(input('Enter score for test two: '))
    test_three = float(input('Enter score for test three: '))
    test_four = float(input('Enter score for test four: '))
    test_five = float(input('Enter score for test five: '))

    average = calc_average(test_one, test_two, test_three, test_four, test_five)
    print('Test Average:', average)

    letter_grade = determine_grade(average)
    print('Letter Grade:', letter_grade)


def calc_average(one, two, three, four, five):
    tests = [one, two, three, four, five]
    test_average = (one + two + three + four + five) / len(tests)
    return test_average


def determine_grade(average):
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average <= 89:
        return 'B'
    elif 70 <= average <= 79:
        return 'C'
    elif 60 <= average <= 69:
        return 'D'
    else:
        return 'F'


main()
