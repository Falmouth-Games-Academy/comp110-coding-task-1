
#!/usr/bin/python
# Turn on debug mode.

import cgitb
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

# Print the top 10 scores in the database.
c.execute("SELECT * FROM scores"
        "ORDER BY score DESC")
print([(r[0], r[1]) for r in c.fetchall()])

