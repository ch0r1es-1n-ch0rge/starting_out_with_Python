# A company has determined that its annual profit is typically 23 percent of total sales. Write a program that asks
# the user to enter the projected amount of total sales, then displays the profit that will be made from that amount.
# Hint: Use the value 0.23 to represent 23 percent.

# Constant Value
PROFIT_PERCENTAGE = 0.23

# Get total sale
projected_sales = float(input('Enter the projected sales: '))

# Calculate annual profit
annual_profit = projected_sales * PROFIT_PERCENTAGE

# Display total sales
print('The annual profit is $', format(annual_profit, ',.2f'), sep='')
