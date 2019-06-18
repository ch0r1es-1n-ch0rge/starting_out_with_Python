# Serendipity Booksellers has a book club that awards points to its customers based on the number of books purchased
# each month. The points are awarded as follows:
#   - If a customer purchased 0 books, he or she earns 0 points.
#   - If a customer purchased 2 books, he or she earns 5 points.
#   - If a customer purchased 4 books, he or she earns 15 points.
#   - If a customer purchased 6 books, he or she earns 30 points.
#   - If a customer purchased 8 books, he or she earns 60 points.
# Write a program that asks the user to enter the number of books that he or she has purchased this month, then displays
# the number of points awarded.

# Get number of purchased books from user
books_purchased = int(input('Enter the number of books purchased this month: '))

# Decision Structure
if books_purchased >= 8:
    print('Points earned: 60 points.')
elif 8 > books_purchased >= 6:
    print('Points earned: 30 points.')
elif 6 > books_purchased >= 4:
    print('Points earned: 15 points.')
elif 4 > books_purchased >= 2:
    print('Points earned: 5 points.')
elif 2 > books_purchased >= 0:
    print('Points earned: 0 points.')
