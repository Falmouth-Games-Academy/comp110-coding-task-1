
#!/usr/bin/python

# Turn on debug mode.
import cgitb
cgitb.enable()

# Print necessary headers.
print(“Content-Type: text/html; charset=utf-8\n\n”)

# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='high_scores',
    user='root',
    passwd='ImprobableDreams',
    host='localhost')

c = conn.cursor()

#import cgi
#Form = cgi.Fieldstorage()

#if "playername" not in form:
#        print("Something went wrong")
#Else
#         print ("hello" + str.getvalue("user"))

#playername = self.request.get('player_name')
#level = self.request.get('level')
#score = self.request.get('score')

# Insert some example data.
c.execute("INSERT INTO scores(player_ID, level_ID, score) VALUES ('2,1,22')")
conn.commit()

# Print the contents of the database.
c.execute("SELECT * FROM scores")
print([(r[0], r[1]) for r in c.fetchall()])
