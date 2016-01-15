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
sql = "SELECT 'first_name', 'last_name', 'score' 
FROM scores 
ORDER BY scores DESC
LIMIT 0, 10"


c.execute(sql, ("url.ac.uk",))
results = c.fetchall()
print(result)

connection.close()
