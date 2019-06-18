# Figure 3-19 shows a simplified flowchart for troubleshooting a bad Wi-Fi connection. Use the flowchart to create a
# program that leads a person through the steps of fixing a bad Wi-Fi connection.

# Output prompt to the user
print('This program will walk you through the steps to troubleshoot your Wi-Fi connection.')
print('Reboot the computer and try to connect.')

# Get answer from user
user_answer = input('Did that fix the problem? (Y for Yes or N for No): ')

# Decision Structure
if user_answer.upper() == 'N':
    print('Reboot the router and try to connect.')
    user_answer = input('Did that fix the problem? (Y for Yes or N for No): ')
    if user_answer.upper() == 'N':
        print('Make sure the cables between the router and modem are plugged in firmly.')
        user_answer = input('Did that fix the problem? (Y for Yes or N for No): ')
        if user_answer.upper() == 'N':
            print('Move the router to a new location and try to connect.')
            user_answer = input('Did that fix the problem? (Y for Yes or N for No): ')
            if user_answer.upper() == 'N':
                print('Get a new router.')

# Decision Structure
if user_answer.upper() == 'Y':
    print('I am glad you were able to connect to your Wi-Fi router.')
