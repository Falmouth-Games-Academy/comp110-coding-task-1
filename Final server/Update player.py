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
