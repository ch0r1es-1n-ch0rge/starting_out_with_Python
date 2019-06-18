# The Fast Freight Shipping Company charges the following rates:
#       __________________________________________________________________
#       Weight of Package                                   Rate per Pound
#       ------------------------------------------------------------------
#       2 pounds or less                                    $1.50
#       Over 2 pounds but not more than 6 pounds            $3.00
#       Over 6 pounds but not more than 10 pounds           $4.00
#       Over 10 pounds                                      $4.75
#       ------------------------------------------------------------------
# Write a program that asks the user to enter the weight of a package then displays the shipping charges.

# Get the weight of the package from user
package_weight = int(input('Enter the weight of the package (in pounds): '))

# Decision Structure
if package_weight > 10:
    print('Shipping Charge: $4.75')
elif 10 >= package_weight > 6:
    print('Shipping Charge: $4.00')
elif 6 >= package_weight > 2:
    print('Shipping Charge: $3.00')
else:
    print('Shipping Charge: $1.50')
