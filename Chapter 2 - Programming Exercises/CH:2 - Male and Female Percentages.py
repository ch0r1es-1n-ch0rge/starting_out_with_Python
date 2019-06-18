# Write a program that asks the user for the number of males and the number of females registered in a class. The
# program should display the percentage of males and females in the class.
# Hint: Suppose there are 8 males and 12 females in a class. There are 20 students in the class. The percentage of
# males can be calculated as 8 / 20 = 0.4, or 40%. The percentage of females can be calculated a 12 / 20 - 0.6, or 60 %.

# Get the number of male and female students registered
male_students = int(input('Enter the number of male students registered: '))
female_students = int(input('Enter the number of female students registered: '))

# Calculate the total number of students registered
total_students = male_students + female_students

# Calculate the percentage of male and female students
male_percentage = (male_students / total_students) * 100
female_percentage = (female_students / total_students) * 100

# Display the results
print('The percentage of male students registered is ', male_percentage, '%.', sep='')
print('The percentage of female students registered is ', female_percentage, '%.', sep='')
