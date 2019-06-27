# A country collects property tax on the assessment value of property, which is 60 percent of the property's actual
# value. For example, if an acre of land is valued at $10,000, its assessment value is $ 6,000. The property tax is then
# 72 cents for each $100 of the assessment value. The tax for the acre assessed at $6,000 will be $43.20. Write a
# program that asks for the actual value of a piece of property and displays the assessment value and property tax.


# Create Main Function
def main():
    property_value = float(input('Enter the actual value of the property: '))
    tax_assessment(property_value)


def tax_assessment(amount):
    assessment_percentage = 0.6
    property_tax = 0.72 / 100
    tax_value = amount * assessment_percentage * property_tax
    print('Tax on the property: $', format(tax_value, ',.2f'), sep='')


main()
