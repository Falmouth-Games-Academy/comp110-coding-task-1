#!/usr/bin/python

#Turn on debug mode.
import cgitb
import pymsql
import json
cgitb.enable()

#Print necessary headers.
print("Content-Type: text/html; charset=utf-8\n\n")

#Connect to the database.
import cgi
form = cgi.FieldStorage()
  
#Connect to the database.
conn = pymysql.connect(
  db = 'example',
  user = 'root'
  passwd = 'password' #changed this incase it matter
  host = 'localhost')
c = conn.cursor()


#Get some example data
def print_highscore():
  c.execute = ("SELECT players.first_name,  scores.score 
  FROM scores 
  INNER JOIN players  
  ON player_id = players.id  
  ORDER BY score DESC  
  LIMIT 1")
  
  print ("<br/><br/><b>Top score</b><br/>")
  print ([(r[0], r[1], r[2]) for r in c.fetchall()])
  
def main():
  print_highscore()
  
if __name__ == "__main__":
  main()

connection.close()
