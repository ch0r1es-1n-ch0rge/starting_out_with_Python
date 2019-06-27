# Write a program that asks the user to enter the monthly costs for the following expenses incurred from operating his
# or her automobile: loan payment, insurance, gas, oil, tires, and maintenance. The program should then display the
# total monthly cost of these expenses, and the total annual cost of these expenses.


# Create Main Function
def main():
    loan_payment = float(input('Enter the monthly loan amount: '))
    insurance = float(input('Enter the monthly insurance amount: '))
    gas = float(input('Enter the monthly cost of gas: '))
    oil = float(input('Enter the monthly of cost of oil: '))
    tires = float(input('Enter the monthly of cost of tires: '))
    maintenance = float(input('Enter the monthly of cost of maintenance: '))
    automobile_cost(loan_payment, insurance, gas, oil, tires, maintenance)


def automobile_cost(l, i, g, o, t, m):
    monthly_total = l + i + g + o + t + m
    print('The monthly automobile cost is: $', format(monthly_total, '.2f'), sep='')


main()
