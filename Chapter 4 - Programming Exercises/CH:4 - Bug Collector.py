# A bug collector collects bugs every day for five days. Write a program that keeps a running total of the number of
# bugs collected during the five days. The loop should ask for the number of bugs collected for each day, and when the
# loop is finished, the program should display the total number of bugs collected.

# Initialize total and day
total = 0
day = 0

# Repetition Structure
# while day < 5:
while day < 7:
    bugs_collected = int(input('Enter the number of bugs collected: '))
    total += bugs_collected
    day += 1

# Output the total number of bugs collected
print('After 5 days, the total number of bugs collected:', total, 'bugs')
