# Write a program that asks the user to enter a number of seconds and works as follows:
#   - There are 60 seconds in a minute. If the number of seconds entered by the user is greater than or equal to 60, the
#     program should convert the number of seconds to minutes and seconds.
#   - There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater than or equal to
#     3,600, the program should convert the number of seconds to hours, minutes, and seconds.
#   - There are 86,400 seconds in a day. If the number of seconds entered by the user is greater than or equal to
#     86,400, the program should convert the number of seconds to days, hours, minutes, and seconds.

# Get the number of seconds from user
user_seconds = int(input('Enter the number of seconds to be converted: '))

# Calculate days, hours, minutes, and seconds
days = int(user_seconds / 86400)
hours = int((user_seconds % 86400) / 3600)
minutes = int(((user_seconds % 86400) % 3600) / 60)
seconds = int((int(user_seconds % 86400) / 3600) % 60)

# Decision Structure
if user_seconds >= 86400:
    print('Entered:', user_seconds, 'seconds')
    print('Equivalent to...')
    print('Day(s):', days)
    print('Hour(s):', hours)
    print('Minute(s):', minutes)
    print('Second(s):', seconds)
elif 3600 <= user_seconds < 86400:
    print(user_seconds // 3600, 'hour')
else:
    print(user_seconds // 60, 'minute')
