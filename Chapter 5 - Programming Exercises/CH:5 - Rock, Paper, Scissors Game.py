# Write a program that lets the user play the game of Rock, Paper, Scissors against the computer. The program should
# work as follows:
# 1. When the program begins, a random number in the range of 1 through 3 is generated. If the number is 1, then the
# computer has chosen rock. If the number is 2, then the computer has chosen paper. If the number is 3, then the
# computer has chosen scissors. (Don't display the computer's choice yet.)
# 2. The user enters his or her choice of "rock," "paper," "scissors" at the keyboard.
# 3. The computer's choice is displayed.
# 4. A winner is selected according to the following rules:
#   - If one player chooses rock and the other player chooses scissors, then rock wins. (Rock smashes scissors.)
#   - If one player chooses scissors and the other player chooses paper, then scissors wins. (Scissors cuts paper.)
#   - If one player chooses paper and the other player chooses rock, then paper wins. (Paper wraps rock.)
#   - If both players make the same choice, the game must be played again to determine the winner.

# Import Random Module
import random


# Create Main Function
def main():
    keep_going = True
    while keep_going:
        random_number = number_generator()
        user_choice = input('Enter either rock, paper, or scissors: ')
        computer_choice = computer_picks(random_number)
        keep_going = game_decision(user_choice, computer_choice)


def number_generator():
    num = random.randint(1, 3)
    return num


def computer_picks(rand):
    if rand == 1:
        return 'Rock'
    elif rand == 2:
        return 'Paper'
    else:
        return 'Scissors'


def game_decision(user, computer):
    if user.capitalize() == 'Rock' and computer == 'Scissors':
        print()
        print('You chose:', user)
        print('Computer chose:', computer)
        print('You win! Rock smashes scissors.')
        return False
    elif user.capitalize() == 'Scissors' and computer == 'Rock':
        print()
        print('You chose:', user)
        print('Computer chose:', computer)
        print('You lost! Rock smashes scissors.')
        return False
    elif user.capitalize() == 'Scissors' and computer == 'Paper':
        print()
        print('You chose:', user)
        print('Computer chose:', computer)
        print('You win! Scissors cuts paper.')
        return False
    elif user.capitalize() == 'Paper' and computer == 'Scissors':
        print()
        print('You chose:', user)
        print('Computer chose:', computer)
        print('You lost! Scissors cuts paper.')
        return False
    elif user.capitalize() == 'Rock' and computer == 'Paper':
        print()
        print('You chose:', user)
        print('Computer chose:', computer)
        print('You lost! Paper wraps rock.')
        return False
    elif user.capitalize() == 'Paper' and computer == 'Rock':
        print()
        print('You chose:', user)
        print('Computer chose:', computer)
        print('You win! Paper wraps rock.')
        return False
    else:
        print()
        print('You chose:', user)
        print('Computer chose:', computer)
        print('You and the computer picked the same sign. The game must be played again to determine the winner.')
        return True


main()
