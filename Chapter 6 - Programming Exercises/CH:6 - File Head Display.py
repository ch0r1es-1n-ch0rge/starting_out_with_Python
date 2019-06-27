# Write a program that asks the user for the name of a file. The program should display only the first five lines of the
# file's contents. If the file's contains less than five lines, it should display the file's entire contents.


# Create Main Function
def main():
    filename = input('Enter the file name: ')
    open_file(filename)


def open_file(file):
    filename = file + '.txt'
    infile = open(filename, 'r')

    for num in range(5):
        num = infile.readline()
        num = num.rstrip('\n')
        num = int(num)
        print(num)

    infile.close()


main()
