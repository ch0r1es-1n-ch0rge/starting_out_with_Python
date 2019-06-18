# A software company sells a package that retails for $99. Quantity discounts are given according to the following
# table:
#                               Quantity                Discount
#                               --------------------------------
#                               10 - 19                 10%
#                               20 - 49                 20%
#                               50 - 99                 30%
#                               100 or more             40%
#                               --------------------------------
# Write a program that asks the user to enter the number of packages purchased. The program should then display the
# amount of the discount (if any) and the total amount of the purchase after the discount.

# Constant Variable
RETAIL_PACKAGE = 99

# Get the number of packages purchased
packages_purchased = int(input('Enter the number of packages purchased: '))

# Decision Structure
if packages_purchased >= 100:
    print('Discount: 40%')
    print('Final Amount (w/ 40% discount): $', (RETAIL_PACKAGE * packages_purchased) -
          (RETAIL_PACKAGE * packages_purchased * 0.4), sep='')
elif 50 <= packages_purchased <= 99:
    print('Discount: 30%')
    print('Final Amount (w/ 30% discount): $', (RETAIL_PACKAGE * packages_purchased) -
          (RETAIL_PACKAGE * packages_purchased * 0.3), sep='')
elif 20 <= packages_purchased <= 49:
    print('Discount: 20%')
    print('Final Amount (w/ 20% discount): $', (RETAIL_PACKAGE * packages_purchased) -
          (RETAIL_PACKAGE * packages_purchased * 0.2), sep='')
elif 10 <= packages_purchased <= 19:
    print('Discount: 10%')
    print('Final Amount (w/ 10% discount): $', (RETAIL_PACKAGE * packages_purchased) -
          (RETAIL_PACKAGE * packages_purchased * 0.1), sep='')
else:
    print('Discount: 0%')
    print('Final Amount: $', RETAIL_PACKAGE * packages_purchased, sep='')
