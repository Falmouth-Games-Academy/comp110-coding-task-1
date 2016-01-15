#!/usr/bin/python

# Turn on debug mode
import cgitb
import cgi
import json
import pymysql

import processing

cgitb.enable()

# Print necessary headers
print("Content-Type: text/html; charset=utf-8\n\n")

form = cgi.FieldStorage()

player_name = str(form.getvalue("player")).upper()
level_number = form.getvalue("level")
score = form.getvalue("score")

# Connect to the database
conn = pymysql.connect(
        db='highscores',
        user='root',
        passwd='falser110',
        host='localhost')
c = conn.cursor()

player_ids = processing.get_player_id(player_name)
player_id = player_ids[0]

# Insert the score
c.execute("INSERT INTO scores_test VALUES(" + str(player_id) + ", " + level_number + ", " + score + ")")
conn.commit()

c.execute("SELECT * FROM scores_test")
highscores = [(row[0], row[1], row[2]) for row in c.fetchall()]
print(json.dumps(highscores))