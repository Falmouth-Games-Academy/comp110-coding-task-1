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
c.execute = ("SELECT players.first_name, players.last_name, scores.score 
FROM scores 
INNER JOIN player
ON player_id = players.id
ORDER BY scores DESC
LIMIT 10")

score_table = ([(r[0], r[1], r[2]) for r in c.fetchall()])
print(score_table)

connection.close()




