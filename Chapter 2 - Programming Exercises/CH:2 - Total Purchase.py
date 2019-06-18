# A customer in a store is purchasing five items. Write a program that asks for the price of each item, then displays
# the subtotal of the sale, the amount of sales tax, and the total. Assume the sales tax is 7 percent.

# Constant Value
SALES_TAX = 0.07

# Get price of 5 items
item_price1 = float(input('Enter the price of item 1: '))
item_price2 = float(input('Enter the price of item 2: '))
item_price3 = float(input('Enter the price of item 3: '))
item_price4 = float(input('Enter the price of item 4: '))
item_price5 = float(input('Enter the price of item 5: '))

# Calculate Subtotal
sub_total = item_price1 + item_price2 + item_price3 + item_price4 + item_price5

# Calculate Sales Tax
sales_tax_amount = sub_total * SALES_TAX

# Calculate Total
total = sub_total + sales_tax_amount

# Display subtotal, amount of sales tax, and total
print('Subtotal: $', format(sub_total, ',.2f'), sep='')
print('Amount of Sales Tax: $', format(sales_tax_amount, ',.2f'), sep='')
print('Total: $', format(total, ',.2f'), sep='')
