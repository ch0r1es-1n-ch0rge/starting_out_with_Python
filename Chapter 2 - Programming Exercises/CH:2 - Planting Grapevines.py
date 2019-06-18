# A vineyard is planting several new rows of grapevines, and needs to know how many grapevines to plant in each row.
# She has determined that after measuring the length of a future row, she can use the following formula to calculate
# the number of vines that will fit in the row, along with the trellis end-post assemblies that will need to be
# constructed at each end of the row:
#                                       V = (R - 2E) / S
# The terms in the formula are:
# V is the number of grapevines that will fit in the row.
# R is the length of the row, in feet.
# E is the amount of space, in feet, used by an end-post assembly.
# S is the space between vines, in feet.
#
# Write a program that makes the calculation for the vineyard owner. The program should ask the user to input the
# following:
#
# The length of the row, in feet
# The amount of space used by an end-post assembly
# The amount of space between the vines, in feet
#
# Once the input data has been entered, the program should calculate and display the number of grapevines that will fit
# in the row.

# Get row length, end-post spacing, and spacing between the vines
row_length = float(input('Enter the length of the row, in feet: '))
end_post_spacing = float(input('Enter the amount of space used by the end-post assembly: '))
vine_spacing = float(input('Enter the amount of space between the vines, in feet: '))

# Calculate the number grapevines
number_of_grapevines = int((row_length - 2 * end_post_spacing) / vine_spacing)

# Display the result
print('The number of grapevines that will fit in the specified vineyard is', number_of_grapevines, 'vines.')
