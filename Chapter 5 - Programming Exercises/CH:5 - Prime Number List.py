# This exercise assumes that you have already written the is_prime function in Programming Exercise 17. Write another
# program that displays all of the prime numbers from 1 to 100. The program should have a loop that calls the is_prime
# function.


# Create Main Function
def main():
    print('Prime Numbers')
    print('-' * 12)
    for num in range(1, 101):
        if is_prime(num):
            print(num)


def is_prime(number):
    keep_going = True
    for num in range(2, number):
        if number % num == 0:
            keep_going = False
        return keep_going


main()
