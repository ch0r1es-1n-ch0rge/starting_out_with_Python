# Write a program that calculates the total amount of a meal purchased at a restaurant. The program should ask the user
# to enter the charge for the food, then calculate the amounts of a 18 percent tip and 7 percent sales tax. Display
# each of these amounts and the total.

# Constant Variable - Tip
TIP = .18

# Constant Variable - Sales Tax
SALES_TAX = 0.07

# Get the amount for the meal from user
purchased_meal = float(input('Enter the amount for the meal purchased from the restaurant: '))

# Calculate - Tip
tip_on_meal = purchased_meal * TIP

# Calculate - Sales Tax
tax_on_meal = purchased_meal * SALES_TAX

# Calculate - Total of Sale
total_on_purchase = purchased_meal + tip_on_meal + tax_on_meal

# Display purchase amount, tip amount, tax amount, and total
print('The amount of the meal is: $', format(purchased_meal, '.2f'), sep='')
print('The amount of the tip on the meal is: $', format(tip_on_meal, '.2f'), sep='')
print('The amount of the tax on the meal is: $', format(tax_on_meal, '.2f'), sep='')
print('The total for the meal including tax and tip is: $', format(total_on_purchase, '.2f'), sep='')
