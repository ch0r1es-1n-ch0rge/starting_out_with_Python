# Write a function named mac that accepts two integer values as arguments and returns the value that is the greater of
# the two. For example, if 7 and 12 are passed as arguments to the function, the function should return 12. Use the
# function in a program that prompts the user to enter two integer values. The program should display the value that is
# the greater of the two.


# Create Main Function
def main():
    first_integer = int(input('Enter an integer: '))
    second_integer = int(input('Enter another integer: '))
    calculate_max(first_integer, second_integer)


def calculate_max(first, second):
    if first == second:
        print()
        print('The two integers entered are even!')
    else:
        print()
        print('The greatest of the two integer entered is:', max(first, second))


main()
