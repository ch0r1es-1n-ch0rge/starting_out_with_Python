# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk. Write a program
# that calculates the average of all the numbers stored in the file.


# Create Main Function
def main():
    read_file()


def read_file():
    infile = open('numbers.txt', 'r')

    num_sum = 0
    counter = 0

    for numbers in infile:
        numbers = numbers.rstrip('\n')
        numbers = int(numbers)
        num_sum += numbers
        counter += 1

    num_average = num_sum / counter
    print('Average of integers in the file:', num_average)

    infile.close()


main()
