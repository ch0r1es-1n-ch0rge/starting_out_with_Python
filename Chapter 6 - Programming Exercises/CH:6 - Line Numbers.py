# Write a program that asks the user for the name of a file. The program should display the contents of the file with
# each line preceded with a line number followed by a colon. The line numbering should start at 1.


# Create Main Function
def main():
    filename = input('Enter the file name: ')
    open_file(filename)


def open_file(file):
    filename = file + '.txt'
    infile = open(filename, 'r')

    line_num = 0

    for num in range(5):
        num = infile.readline()
        num = num.rstrip('\n')
        num = int(num)
        line_num += 1
        print('Line ', line_num, ': ', num, sep='')

    infile.close()


main()
