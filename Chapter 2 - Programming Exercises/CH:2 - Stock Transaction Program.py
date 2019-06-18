# Last month, Joe purchased some stock in Acme Software, Inc. Here are the details of the purchase:
#
#   - The number of shares that Joe purchased was 2,000.
#   - When Joe purchased the stock, he paid $40.00 per share.
#   - Joe paid his stockbroker a commission that amounted to 3 percent of the amount he paid for the stock.
#
# Two weeks later, Joe sold the stock. Here are the details of the sale:
#
#   - The number of shares that Jor sold was 2,000.
#   - He sold the stock for $42.75 per share.
#   - He paid his stockbroker another commission that amounted to 3 percent of the amount he received for the stock.
#
# Write a program that displays the following information:
#
#   - The amount of money Joe paid for the stock.
#   - The amount of commission Joe paid his broker when he bought the stock.
#   - The amount for which Joe sold the stock.
#   - The amount of commission Joe paid his broker when he sold the stock.
#   - Display the amount of money that Joe had left when he sold the stock and paid his broker (both times). If this
#   amount is positive, then Joe made a profit. If the amount is negative, then Joe lost money.

# Initialize Constant Variables
PURCHASED_SHARES = 2000
PURCHASED_AMOUNT = 40

COMMISSION = 0.03

SHARES_SOLD = 2000
AMOUNT_SOLD = 42.75

# Calculate total of purchase and sale of stock
total_paid = PURCHASED_SHARES * PURCHASED_AMOUNT
total_sold = SHARES_SOLD * AMOUNT_SOLD

# Calculate commission on both transactions
purchase_commission = total_paid * COMMISSION
sale_commission = total_sold * COMMISSION

# Calculate final total after commission
final_paid = total_paid - purchase_commission
final_sale = total_sold - sale_commission

# Display the results
print('Amount paid: $', format(total_paid, ',.2f'), sep='')
print('Commission on purchased stock: $', format(purchase_commission, ',.2f'), sep='')
print('Amount sold: $', format(total_sold, ',.2f'), sep='')
print('Commission on sale of stock: $', format(sale_commission, ',.2f'), sep='')
print('Amount after commission: $', format(final_sale, ',.2f'), sep='')
