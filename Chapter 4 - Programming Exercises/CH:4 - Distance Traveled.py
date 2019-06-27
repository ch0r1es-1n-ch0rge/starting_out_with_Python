# The distance a vehicle travels can be calculated as follows:
#                                   distance = speed x time
# For example, if a train travels 40 miles per hour for three hours, the distance traveled is 120 miles. Write a program
# that asks the user for the speed of a vehicle (in miles per hour) and the number of hours it has traveled. It should
# then use a loop to display the distance the vehicle has traveled for each hour of that time period.

# Get speed and time from user
user_speed = int(input('Enter the speed of the vehicle (in miles per hour): '))
user_time = int(input('Enter number of hours traveled: '))

# Output time and distance traveled table
print('Time \t\t\tDistance Traveled')
print('-' * 33)

# Initiate distance
user_distance = 0

# Repetition Structure
for time in range(1, user_time + 1):
    print(time, '\t\t\t\t\t', (time * user_speed))
    user_distance += time * user_speed
