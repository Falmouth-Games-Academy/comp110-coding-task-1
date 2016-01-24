#!/usr/bin/python

# Turn on debug mode.
import cgitb
import pymysql
import json

cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html; charset=utf-8\n\n")

import cgi
form = cgi.FieldStorage()

# Connect to the database.
conn = pymysql.connect(
    db='highscores',
    user='root',
    passwd='samwillsfal',
    host='localhost')
c = conn.cursor()

def update_player():
    first_name = str(form.getvalue('first_name'))
    new_first_name = str(form.getvalue('new_first_name'))
    last_name = str(form.getvalue('last_name'))
    new_last_name = str(form.getvalue('new_last_name'))
    score = str(form.getvalue('score'))
    print("Hello " + first_name + " You want to change your name to " + new_first_name)

    update_player = c.execute("UPDATE players "
    "SET first_name=%s, last_name=%s WHERE first_name=%s",
    (new_first_name, new_last_name, first_name))

    conn.commit()
    print ("Name updated")
    
'''
The main gets request from form then displays appropriate text or error.
'''
def main():

    if 'request' not in form:
        print("Missing request")
    else:
        request = str(form.getvalue('request'))
        if request == 'update_player':
            update_player()

if __name__ == "__main__":
    main()
