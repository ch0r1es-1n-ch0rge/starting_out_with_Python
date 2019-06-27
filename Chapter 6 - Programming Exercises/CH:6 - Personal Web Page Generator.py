# Write a program that asks the user for his or her name, then asks the user to enter a sentence that describes himself
# or herself. Here is an example of the program's screen:
#
# Enter your name: Julie Taylor [Enter]
# Describe yourself: I am a computer science major, a member of the Jazz club, and I hope to work as a mobile app
# developer after I graduate. [Enter]
#
# Once the user has entered the requested input, the program should create an HTML file, containing the input, for a
# simple Web page. Here is an example of the HTML content, using the sample input previously shown:
#
# <html>
# <head>
# </head>
# <body>
#    <center>
#       <h1>Julie Taylor</h1>
#    </center>
#    <hr />
#    I am a computer science major, a member of the Jazz club, and I hope to work as a mobile app developer after I
#    graduate.
#    <hr />
# </body>
# </html>


# Create Main Function
def main():
    user_name = input('Enter your name: ')
    user_description = input('Describe yourself: ')

    write_to_html(user_name, user_description)


def write_to_html(name, description):
    outfile = open('simple_html.html', 'w')
    outfile.write('<html>' + '\n' + '<head>' + '\n' + '</head>' + '\n' + '<body>' + '\n' + '\t' + '<center>' + '\n' +
                  '\t\t' + '<h1>' + name + '</h1>' + '\n' + '\t' + '</center>' + '\n' + '\t' + '<hr />' + description +
                  '<hr />' + '\n' + '</body>' + '\n' + '</html>')

    outfile.close()


main()
