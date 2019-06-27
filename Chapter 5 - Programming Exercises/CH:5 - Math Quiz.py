# Write a program that gives simple math quizzes. The program should display two random numbers that are to be added,
# such as:
#   247
# + 129
# The program should allow the student to enter the answer. If the answer is correct, a message of congratulations
# should be displayed. If the answer is incorrect, a message showing the correct answer should be display.

# Import random module:
import random


# Create Main Function
def main():
    rand_num1 = random.randint(1, 50)
    rand_num2 = random.randint(1, 50)
    rand_total = rand_num1 + rand_num2
    print('Math Quiz. Add the two numbers below.')
    print()
    print(' ', rand_num1)
    print('+', rand_num2)
    print('-' * 4)
    print()
    user_answer = int(input('Enter the answer: '))
    addition_checker(user_answer, rand_total)


def addition_checker(answer, total):
    if answer == total:
        print('Congratulations! You are correct!')
    else:
        print('Sorry, wrong answer.')
        print('Total =', total)


main()
