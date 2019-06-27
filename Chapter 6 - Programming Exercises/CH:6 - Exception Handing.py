# Modify the program that you wrote for Exercise 6 so it handles the following exceptions:
# - It should handle any IOError exception that are raised when the file is opened and data is read from it.
# - It should handle any ValueError exception that are raised when the items that are read from the file are converted
# to a number.


# Create Main Function
def main():
    read_file()


def read_file():
    try:
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

    except IOError:
        print('Error. File does not exist.')

    except ValueError:
        print('Error: The file contains non-numeric values.')


main()
