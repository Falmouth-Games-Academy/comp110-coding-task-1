#!/usr/bin/python

#Turn on debug mode.
import cgitb
import pymysql
import json
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

#Get highscores for top 10
def print_highscores():
  c.execute = ("SELECT players.first_name, players.last_name, scores.score 
  FROM scores 
  INNER JOIN players
  ON player_id = players.id
  ORDER BY score DESC
  LIMIT 10")
  
  print ("<b>Top 10 scores</b><br/>")
  print ([(r[0], r[2], r[2]) for r in c.fetchall()])

#print this in main
def main():
  print_highscores()
  
if __name__ == "__main__":
  main()
  
connection.close()
