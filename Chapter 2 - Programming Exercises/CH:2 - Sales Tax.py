# Write a program that will ask the user to enter the amount of a purchase. The program should then compute the state
# and county sales tax. Assume the state tax is 5 percent and the county sales tax is 2.5 percent. The program should
# display the amount of the purchase, the state sales tx, the county sales tax, the total sales tax, and the total of
# the sale (which is the sum of the amount of the purchase plus the total sales tax).
#
# Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.

# Constant Variable - State Tax
# STATE_TAX = 0.05

STATE_TAX = 0.045

# Constant Variable - County Tax
COUNTY_TAX = 0.025

# Get purchase amount from user
purchase_amount = float(input('Enter the purchase amount: '))

# Compute - State Tax
state_purchase_tax = purchase_amount * STATE_TAX

# Compute - County Tax
county_purchase_tax = purchase_amount * COUNTY_TAX

# Compute - Total Tax
total_tax = state_purchase_tax + county_purchase_tax

# Compute - Total Sale
total_sale = purchase_amount + total_tax

# Display purchase amount, state tax, county tax, total tax, and total sale
print('The purchase amount is: $', format(purchase_amount, ',.2f'), sep='')
print('The state tax on the purchase amount is: $', format(state_purchase_tax, ',.2f'), sep='')
print('The county tax on the purchase amount is: $', format(county_purchase_tax, ',.2f'), sep='')
print('The total amount of tax collected on the purchase amount is: $', format(total_tax, ',.2f'), sep='')
print('The total sale amount is: $', format(total_sale, ',.2f'), sep='')
