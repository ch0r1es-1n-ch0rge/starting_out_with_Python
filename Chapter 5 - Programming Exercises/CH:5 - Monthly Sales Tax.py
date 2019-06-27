# A retail company must file a monthly sales tax report listing the total sales for the month, and the amount of state
# and county sales tax collected. The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.
# Write a program that asks the user to enter the total sales for the month. From this figure, the application should
# calculate and display the following:
#
# - The amount of county sales tax
# - The amount of state sales tax
# - The total sales tax (county plus state)


# Create Main Function
def main():
    monthly_sales = float(input('Enter the sales for the month: '))
    tax_calculator(monthly_sales)


def tax_calculator(sales):
    state_tax = 0.05
    county_tax = 0.025
    monthly_state_tax = sales * state_tax
    monthly_county_tax = sales * county_tax
    total_tax = monthly_state_tax + monthly_county_tax
    print()
    print('The amount of county sales tax: $', format(monthly_county_tax, ',.2f'), sep='')
    print('The amount of state sales tax: $', format(monthly_state_tax, ',.2f'), sep='')
    print('The total sales tax (county plus state): $', format(total_tax, ',.2f'), sep='')


main()
