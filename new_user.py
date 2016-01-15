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

form = cgi.FieldStorage()
playername = str(form.getvalue('playername'))

if "playername" not in form:
        print("Error")
else:
        print ("Hello " + playername + "<br />")

# Insert new user
c.execute("INSERT INTO players VALUES (NULL,'" + playername + "')")
conn.commit()

# Print the contents of the database.
c.execute("SELECT * FROM players")
print([(r[0], r[1]) for r in c.fetchall()])