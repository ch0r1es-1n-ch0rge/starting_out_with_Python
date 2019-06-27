# Write a program that asks the user to enter a distance in kilometers, then converts that distance to miles. The
# conversion formula is as follows:
#                                       Miles = Kilometers x 0.6214


# Create Main Function
def main():
    kilometer = float(input('Enter a kilometer distance to be converted to miles: '))
    kilo_converter(kilometer)


def kilo_converter(kilo):
    miles = kilo * 0.6214
    print()
    print('Input Distance (in kilometer):', kilo, 'kilometers')
    print('Conversion to miles:', format(miles, '.2f'), 'miles')


main()
