# Many financial expert advise that property owners should insure their homes or buildings for at least 80 percent of
# the amount it would cost to replace the structure. Write a program that asks the user to enter the replacement cost of
# a building, then displays the minimum amount of insurance he or she should buy for the property.


# Create Main Function
def main():
    replacement_cost = float(input('Enter the amount that will cost to replace the building: '))
    insurance_calculation(replacement_cost)


def insurance_calculation(cost):
    insurance_cost = cost * 0.8
    print('The minimum amount of insurance he or she should buy for the property: $',
          format(insurance_cost, ',.2f'), sep='')


main()
