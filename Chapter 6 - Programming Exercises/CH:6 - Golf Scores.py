# The Springfork Amateur Golf Club has a tournament every weekend. The club president has asked you to write a two
# programs:
# 1. A program that will read each player's name and golf score as keyboard input, then save these as records in a file
# named golf.txt. (Each record will have a field for the player's name and a field for the player's score.)
# 2. A program that reads the records from the golf.txt file and displays them.


# Create Main Function
def main():
    write_file()
    open_file()


def write_file():
    outfile = open('golf.txt', 'w')

    keep_going = 'Y'
    while keep_going == 'Y' or keep_going == 'y':
        print('Enter the following tournament data.')
        player_name = input('Enter the name of the player: ')
        player_score = input("Enter the player's score: ")

        outfile.writelines(player_name + '\n')
        outfile.writelines(player_score + '\n')

        print()
        keep_going = input('Do you want to enter more data? (Y for Yes, N for No): ')

    outfile.close()
    print('Tournament data has been written to golf.txt file.')


def open_file():
    infile = open('golf.txt', 'r')

    names = infile.readline()

    print('Name\t\t Score')
    print('-' * 18)

    while names != '':
        names = names.rstrip('\n')
        scores = float(infile.readline())
        print(names.capitalize(), '\t\t', scores)
        names = infile.readline()

    infile.close()


main()
