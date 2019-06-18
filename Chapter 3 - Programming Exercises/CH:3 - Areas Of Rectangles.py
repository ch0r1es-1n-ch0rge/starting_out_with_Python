# The area of a rectangle is the rectangle's length times its width. Write a program that asks for the length and width
# of two rectangles. The program should tell the user which rectangle has the grater area, or if the areas are the same.

# Get length and width of two triangles from the user
user_length1 = float(input('Enter the length of the 1st triangle: '))
user_width1 = float(input('Enter the width of the 1st triangle: '))

user_length2 = float(input('Enter the length of the 2nd triangle: '))
user_width2 = float(input('Enter the width of the 2nd triangle: '))

# Calculate the area of the two triangles
area1 = user_length1 * user_width1
area2 = user_length2 * user_width2

# Decision Structure for which triangle is greater or the same
if area1 > area2:
    print('The area of 1st triangle is greater than the area of the 2nd triangle.')
elif area1 < area2:
    print('The area of the 2nd triangle is greater than the area of the 1st triangle.')
else:
    print('The area of both triangles are the same.')
