# This exercise assumes you have completed Programming Exercise 7, Random Number File Writer. Write a program that reads
# the random numbers from the file, displays the number, then displays the following data:
# - The total of the numbers
# - The number of random numbers read from the file


# Create Main Function
def main():
    read_file()


def read_file():
    infile = open('random_numbers.txt', 'r')

    num_sum = 0
    counter = 0

    for numbers in infile:
        numbers = numbers.rstrip('\n')
        numbers = int(numbers)
        num_sum += numbers
        counter += 1

    print('Sum of random numbers in the file:', num_sum)
    print('Number of random numbers in the file:', counter)

    infile.close()


main()
