#!/usr/bin/python

#Turn on debug mode.
import cgitb
cgitb.enable()

#Print necessary headers.
print("Content-Type: text/html; charset=utf-8\n\n")

#Connect to the database.
import cgi
form = cgi.FieldStorage()
  
#Connect to the database.
import pymysql
conn = pymysql.connect(
  db = 'example',
  user = 'root'
  passwd = 'password' #changed this incase it matter
  host = 'localhost')
c = conn.cursor()


#Get some example data
sql = "SELECT players.first_name,  scores.score 
FROM scores 
INNER JOIN players  
ON player_id = players.id  
ORDER BY scores DESC  
LIMIT 1"


c.execute(sql, ("bsccg03.ga.fal.io/",))
results = c.fetchall()
print(result)

connection.close()
