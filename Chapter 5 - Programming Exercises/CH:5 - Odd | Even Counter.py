# In this chapter, you saw an example of how to write an algorithm that determines whether a number is even or odd.
# Write a program that generates 100 random numbers and keeps a count of how many of these random numbers are even, and
# how many of them are odd.

# Import Random Module
import random


# Create Main Function
def main():
    odd_num, even_num = odd_even_counter()
    print('Number of Odd Numbers:', odd_num)
    print('Number of Even Numbers:', even_num)


def odd_even_counter():
    odd = 0
    even = 0
    counter = 0
    while counter < 100:
        random_num = random.randrange(1, 100)
        counter += 1
        if random_num % 2 == 0:
            even += 1
        else:
            odd += 1

    return odd, even


main()
