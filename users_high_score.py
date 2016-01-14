#!/usr/bin/python
# Turn on debug mode.

import cgi, cgitb
cgitb.enable()


# Print necessary headers.
print("Content-Type: text/html; charset=utf-8\n\n")


# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='high_scores',
    user='root',
    passwd='ImprobableDreams',
    host='localhost')


c = conn.cursor()

form = cgi.FieldStorage()
playername = str(form.getvalue('playername'))
score = form.getvalue('score')
level = form.getvalue('level')

if "playername" not in form or "level" not in form or "score" not in form:
        print("Error")
else:
        print ("Hello " + playername)



# Print the top 10 scores in the database.
c.execute("SELECT * FROM scores WHERE ") #Not sure how to do this yet
# I need to look up the user name and get the ID number and then update the score for that ID
print([(r[0], r[1], r[2]) for r in c.fetchall()])
