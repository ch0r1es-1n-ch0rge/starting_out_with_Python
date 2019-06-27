# Assume a file containing a series of names (as strings) is named names.txt and exists on the computer's disk. Write a
# program that displays the number of names that are stored in the file. (Hint: Open the file and read every string
# stored in it. Use a variable to keep a count of he number of items that are read from the file.)


# Create Main Function
def main():
    read_file()


def read_file():
    infile = open('names.txt', 'r')

    counter = 0

    for _ in infile:
        counter += 1

    print('Number of lines in the file:', counter)

    infile.close()


main()
