# You have a group of friends coming to visit for your high school reunion, and you want to take them out to eat at a
# local restaurant. You aren't sure if any of them have dietary restrictions, but your restaurant choices are as
# follows:
#
#   - Joe's Gourmet Burgers --- Vegetarian: No, Vegan: No, Gluten-Free: No
#   - Main Street Pizza Company --- Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
#   - Corner Cafe --- Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
#   - Mama's Fine Italian --- Vegetarian: Yes, Vegan: No, Gluten-Free: No
#   - The Chef's Kitchen --- Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
#
# Write a program tha tasks whether any member of your party are vegetarian, vegan, or gluten-free, to which then
# display only the restaurants to which you may take the group.

# Get initial answer from user
user_vegetarian = input('Is anyone in your party vegetarian? (Y for Yes or N for No): ')
user_vegan = input('Is anyone in your party vegan? (Y for Yes or N for No): ')
user_gluten_free = input('Is anyone in your party gluten-free? (Y for Yes or N for No): ')

if user_vegetarian.upper() == 'N' and user_vegan.upper() == 'N' and user_gluten_free.upper() == 'N':
    print()
    print('Here are your restaurant choices:')
    print("\tJoe's Gourmet Burgers")
    print('\tMain Street Pizza Company')
    print('\tCorner Cafe')
    print("\tMama's Fine Italian")
    print("\tThe Chef's Kitchen")
elif user_vegetarian.upper() == 'Y' and user_vegan.upper() == 'N' and user_gluten_free.upper() == 'N':
    print()
    print('Here are your restaurant choices:')
    print('\tMain Street Pizza Company')
    print('\tCorner Cafe')
    print("\tMama's Fine Italian")
    print("\tThe Chef's Kitchen")
elif (user_vegetarian.upper() == 'N' and user_vegan.upper() == 'Y' and user_gluten_free.upper() == 'N') or \
        (user_vegetarian.upper() == 'Y' and user_vegan.upper() == 'Y' and user_gluten_free.upper() == 'Y'):
    print()
    print('Here are your restaurant choices:')
    print('\tCorner Cafe')
    print("\tThe Chef's Kitchen")
elif (user_vegetarian.upper() == 'N' and user_vegan.upper() == 'N' and user_gluten_free.upper() == 'Y') or \
        (user_vegetarian.upper() == 'Y' and user_vegan.upper() == 'N' and user_gluten_free.upper() == 'Y'):
    print()
    print('Here are your restaurant choices:')
    print('\tMain Street Pizza Company')
    print('\tCorner Cafe')
    print("\tThe Chef's Kitchen")

