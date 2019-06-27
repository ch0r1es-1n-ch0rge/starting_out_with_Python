# Write a program that writes a series of random numbers to a file. Each random number should be in the range of 1
# through 500. The application should let the user specify how many random numbers the file will hold.

# Import Random Module
import random


# Create Main Function
def main():
    num_size = int(input('Enter the amount of random numbers to be generated: '))
    write_file(num_size)


def write_file(size):
    outfile = open('random_numbers.txt', 'w')

    for _ in range(size):
        random_numbers = random.randint(1, 500)
        outfile.writelines(str(random_numbers) + '\n')

    outfile.close()

    print(size, 'random numbers have been written to random_numbers.txt file.')


main()
