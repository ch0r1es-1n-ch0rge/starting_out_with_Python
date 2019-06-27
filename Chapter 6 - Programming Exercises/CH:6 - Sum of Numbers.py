# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk. Write a program
# that reads all of the numbers stored in the file and calculates the total.


# Create Main Function
def main():
    read_file()


def read_file():
    infile = open('numbers.txt', 'r')

    num_sum = 0

    for numbers in infile:
        numbers = numbers.rstrip('\n')
        numbers = int(numbers)
        num_sum += numbers

    print('Sum of integers in the file:', num_sum)

    infile.close()


main()
