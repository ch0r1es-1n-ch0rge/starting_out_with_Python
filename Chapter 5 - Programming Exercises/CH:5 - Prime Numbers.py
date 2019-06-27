# A prime number is a number that is only evenly divisible by itself and 1. FOr example, the number 5 is prime because
# it can only be evenly divided by 1 and 5. The number 6, however, is not prime because it can be divided evenly by 1,
# 2, 3, and 6.
# Write a Boolean function named is_prime which takes an integer as an argument and returns true if the argument is a
# prime number, or false otherwise. Use the function in a program that prompts the user to enter a number then displays
# a message indicating whether the number is prime.
#
# TIP: Recall that the % operator divides one number by another and returns the remainder of the division. In an
# expression such as num1 % num2, the % operator will return 0 if num1 is evenly divisible by num2.


# Create Main Function
def main():
    num = get_num()
    print()
    if is_prime(num):
        print(num, 'is prime!')
    else:
        print(num, 'is not prime!')


def get_num():
    user_num = int(input('Enter an integer to find out if it is a prime number: '))
    return user_num


def is_prime(number):
    if number < 2:
        return False
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


main()
