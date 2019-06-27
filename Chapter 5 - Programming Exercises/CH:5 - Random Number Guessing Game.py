# Write a program that generates a random number in the range of 1 through 100, and asks the user to guess what the
# number is. If the user's guess is higher than the random number, the program should display "Too high, try again." If
# the user's guess is lower than the random number, the should display "Too low, try again." If the user guesses the
# number, the application should congratulate the user and generate a new random number so the game can start over.
# Optional Enhancement: Enhance the game so it keeps count of the number of guesses that the user makes. When the user
# correctly guesses the random number, the program should display the number of guesses.

# Import Random Module
import random


# Create Main Function
def main():
    random_number = random_generator()
    user_guess = int(input('Enter a number from 1 through 100: '))

    guess_total = 0
    keep_going = 0
    while keep_going == 0:
        if not guess_game(random_number, user_guess):
            keep_going = 0
            user_guess = int(input('Enter another number from 1 through 100: '))
            guess_total += 1
        else:
            keep_going = 1

    print('Number of guess it took until you found the correct random number:', guess_total)


def random_generator():
    num = random.randint(1, 100)
    return num


def guess_game(rand, user):
    if user > rand:
        print('Too high, try again.')
        return False
    elif user < rand:
        print('Too low. try again.')
        return False
    else:
        print()
        print('Congratulations! You guessed the correct random number.')
        return True


main()
