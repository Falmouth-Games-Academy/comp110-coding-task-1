
#!/usr/bin/python

#Turn on debug mode.
import cgitb
cgitb.enable()

#Print necessary headers.
print("Content-Type: text/html; charset=utf-8\n\n")

#Connect to the database.
import cgi
form = cgi.FieldStorage()
if "player" not in form or "newplayer" not in form:
  print "Error"
else:
  print ("Hello" form["player"].value)
  
#Connect to the database.
import pymysql
conn = pymysql.connect(
  db = 'example',
  user = 'root'
  passwd = 'password' #changed this incase it matter
  host = 'localhost')
c = conn.cursor()

#Insert some example data - Having some problem with this as my database says there is an error.
c.execute("UPDATE players SET player.first_name = "newplayer" WHERE player.first_name = "player")
conn.commit

#Print database
c.execute("SELECT * FROM players)
print([r[0], r[1]) for r in c.fetchall()])
