#!/usr/bin/python
# Turn on debug mode.

import cgi, cgitb
cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html; charset=utf-8\n\n")
print()

# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='high_scores',
    user='root',
    passwd='ImprobableDreams',
    host='localhost')

c = conn.cursor()

#import cgi
form = cgi.FieldStorage()
playername = str(form.getvalue('playername'))

if "playername" not in form:
        print("Error")
if "level" not in form:
                print("Error")
if "score" not in form:
                print("Error")
else:
        print ("Hello " + str(playername))

score =form.getvalue('score')
player = str(form.getvalue('playername'))
level = form.getvalue('level')


# Insert new user
c.execute("SELECT * FROM players WHERE player LIKE name")
c.execute("UPDATE scores SET score = " + score +" WHERE player_ID = " +playerID + " AND level_ID = "+ level +" ")
conn.commit()


# Print the contents of the database.
c.execute("SELECT * FROM scores")
print([(r[0], r[1], r[2]) for r in c.fetchall()])
