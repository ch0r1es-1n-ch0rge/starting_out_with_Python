# When an object is falling because of gravity, the following formula can be used to determine the distance the object
# falls in a specific time period:
#
#                                       d = 1/2gt^2
#
# The variable in the formula are as follows: d is the distance in meters, g is 9.8, and t is the amount of time, in
# seconds, that the object has been falling.
# Write a functions named falling_distance that accepts an object's falling time (in seconds) as an argument. The
# function should return the distance, in meters, that the object has fallen during that time interval. Write a program
# that calls the function in a loop that passes the value 1 through 10 as arguments and displays the return value.


# Create Main Function
def main():
    print('Time (in seconds)\t\t Distance (in meters)')
    print('-' * 44)
    for time in range(1, 11):
        distance = falling_distance(time)
        print(time, '\t\t\t\t\t\t', distance)


def falling_distance(time):
    distance = (1 / 2) * 9.8 * (time ** 2)
    return format(distance, '.2f')


main()
