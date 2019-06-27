# Programming Exercise #6 in Chapter 2 was the Sales Tax program. For that exercise, you were asked to write a program
# that calculates and displays the county and state sales tax on a purchase. If you have already written that program,
# redesign it so the subtasks are in functions. If you have not already written that program, write it using functions.


# Create Main Function
def main():
    amount = purchase_amount()
    s_tax = state_tax(amount)
    c_tax = county_tax(amount)
    t_tax = total_tax(s_tax, c_tax)
    final_sale(amount, t_tax)


def purchase_amount():
    amount = float(input('Enter the purchase amount: '))
    print('The purchase amount is: $', format(amount, ',.2f'), sep='')
    return amount


def state_tax(amount):
    state_tax_percentage = 0.05
    state_purchase_tax = amount * state_tax_percentage
    print('The state tax on the purchase amount is: $', format(state_purchase_tax, ',.2f'), sep='')
    return state_purchase_tax


def county_tax(amount):
    county_tax_percentage = 0.025
    county_purchase_tax = amount * county_tax_percentage
    print('The county tax on the purchase amount is: $', format(county_purchase_tax, ',.2f'), sep='')
    return county_purchase_tax


def total_tax(state, county):
    print('The total amount of tax collected on the purchase amount is: $', format(state + county, ',.2f'), sep='')
    return state + county


def final_sale(amount, county):
    print('The total sale amount is: $', format(amount + county, ',.2f'), sep='')


main()
