# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. The
# program should first ask for the number of years. The outer loop will iterate once for each year. The inner loop will
# iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for the inches of
# rainfall for that month. After all iterations, the program should display the number of months, the total inches of
# rainfall, and the average rainfall for the entire period.

# Get the number of years of rainfall
user_years = int(input('Enter the number of years: '))

# Initialize starting monthly rainfall
monthly_rainfall = 0

# Repetition Structure
for year in range(1, user_years + 1):
    for month in range(1, 13):
        rainfall = float(input('Enter the amount of rainfall (in inches) this month: '))
        monthly_rainfall += rainfall

# Calculate the total number of months of rainfall data
total_months = user_years * 12

# Output data collected
print('Total number of months of rainfall data:', total_months, 'months')
print('Total number of rainfall (in inches):', monthly_rainfall, 'inches')
print('Average rainfall per month for the entire period:', format((monthly_rainfall / total_months), '.2f'), 'inches')
