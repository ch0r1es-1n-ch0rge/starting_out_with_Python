# Assuming there are no accidents or delays, the distance that a car travels down the state can be calculated with the
# following formula:
#
#                   Distance = Speed x Time
#
# A car is traveling at 70 miles per hour. Write a program that displays the following:
#   The distance the car will travel in 6 hours.
#   The distance the car will travel in 10 hours.
#   The distance the car will travel in 15 hours.

# Constant Car Variable
# CAR1 = 6
# CAR2 = 10
# CAR3 = 15

CAR1 = 5
CAR2 = 8
CAR3 = 12

# Constant MPH Variable
# TRAVELING = 70

TRAVELING = 60

# Calculate traveling distance of each car
distance1 = TRAVELING * CAR1
distance2 = TRAVELING * CAR2
distance3 = TRAVELING * CAR3

# Display the distances of each car onto the console
print('The distance of the car traveling for 6 hours is:', format(distance1, '.2f'), 'miles.')
print('The distance of the car traveling for 10 hours is:', format(distance2, '.2f'), 'miles.')
print('The distance of the car traveling for 15 hours is:', format(distance3, '.2f'), 'miles.')
