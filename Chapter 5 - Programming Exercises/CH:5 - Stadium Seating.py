# There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost $15, and Class C seats
# cost $10. Write a program that asks how many tickets for each class of seats were sold, then displays the amount of
# income generated from ticket sales.


# Create Main Function
def main():
    a_class = int(input('Enter the amount of seats sold for Class A: '))
    b_class = int(input('Enter the amount of seats sold for Class B: '))
    c_class = int(input('Enter the amount of seats sold for Class C: '))
    income(a_class, b_class, c_class)


def income(a, b, c):
    a_income = a * 20
    b_income = b * 15
    c_income = c * 10
    print()
    print('Total Income: $', a_income + b_income + c_income, sep='')


main()
