# Running on a particular treadmill you burn 4.2 calories per minute. Write a program that uses a loop to display the
# number of calories burned after 10, 15, 20, 25, and 30 minutes.

# Initiate starting time
first_minutes = 10
time = 10
# Repetition Structure
while first_minutes <= 30:
    # calories_burned = int(first_minutes * 4.2)
    calories_burned = int(first_minutes * 3.9)
    print('Calories Burned at', time, 'minutes:', calories_burned, 'calories')
    first_minutes += 5
    time += 5
