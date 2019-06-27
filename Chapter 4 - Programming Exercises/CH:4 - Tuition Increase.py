# At one college, the tuition for a fill -time student is $8,000 per semester. It has been announced that the tuition
# will increase by 3 percent each year for the next 5 years. Write a program with a loop that displays the projected
# semester tuition for the next 5 years.

# Constant Variable
STARTING_TUITION = 8000

# Output table
print('Semester\t\tProjected Tuition')
print('-' * 40)

# Repetition Structure
for semester in range(1, 11):
    STARTING_TUITION *= 1.03

    for output in range(1):
        print(semester, '\t\t\t\t$', format(STARTING_TUITION, '.2f'))
