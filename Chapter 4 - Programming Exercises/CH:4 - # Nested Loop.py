# Write a program that uses nested loops to draw this pattern:
#
# ##
# # #
# #  #
# #   #
# #    #
# #     #

# Initialize Step Value
STEP_VAL = 6

# Repetition Structure
for row in range(STEP_VAL):
    print('#', end='')
    for column in range(row):
        print(' ', end='')
    print('#')
