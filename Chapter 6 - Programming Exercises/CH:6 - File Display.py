# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk. Write a program
# that displays all of the numbers in the file.


# Create Main Function
def main():
    read_file()


def read_file():
    infile = open('numbers.txt', 'r')

    for numbers in infile:
        numbers = numbers.rstrip('\n')
        numbers = float(numbers)
        print(numbers)

    infile.close()


main()
