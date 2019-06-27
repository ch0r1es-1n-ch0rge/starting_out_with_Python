# A painting company has determined that for every 112 square feet of wall space, one gallon of paint and eight hours of
# labor will be required. The company charges $35.00 per hour for labor. Write a program that asks the user to enter the
# square feet of wall space to be painted and the price of the paint per gallon. The program should display the
# following data:
#
# - The number of gallons of paint required
# - The hours of labor required
# - The cost of the paint
# - The labor charges
# - The total cost of the paint job


# Create Main Function
def main():
    wall_space = float(input('Enter the square footage of the wall space: '))
    paint_price = float(input('Enter the price of the paint per gallon: '))
    estimate(wall_space, paint_price)


def estimate(space, price):
    paint_required = space / 112
    print('The number of gallons of paint required:', format(paint_required, '.2f'))
    labor_hours = paint_required * 8
    print('The hours of labor required:', format(labor_hours, '.2f'))
    paint_cost = paint_required * price
    print('The cost of the paint: $', format(paint_cost, ',.2f'), sep='')
    labor_charges = labor_hours * 35
    print('The labor charges: $', format(labor_charges, ',.2f'), sep='')
    job_total = paint_cost + labor_charges
    print('The total cost of the paint job: $', format(job_total, ',.2f'), sep='')


main()
