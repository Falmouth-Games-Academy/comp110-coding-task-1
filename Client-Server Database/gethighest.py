#!/usr/bin/python

"""Get the highest score for a particular player on a particular level.

The code in this module processes a get request and prints the highest
score for the requested player and level.
"""

import cgi
import json

import pymysql

# Print necessary headers
print("Content-Type: text/html; charset=utf-8\n\n")

form = cgi.FieldStorage()

if "player" not in form or "level" not in form:
    print(json.dumps("Player or level not provided"))
else:
    player_name = str(form.getvalue("player")).upper()
    level_number = form.getvalue("level")

# Connect to the database
conn = pymysql.connect(
        db='highscores',
        user='root',
        passwd='falser110',
        host='localhost')
cursor = conn.cursor()

cursor.execute("SELECT players_test.name, levels_test.level_name, scores_test.score FROM scores_test "
               "INNER JOIN players_test ON scores_test.player_id = players_test.player_id "
               "INNER JOIN levels_test ON scores_test.level_id = levels_test.level_id "
               "WHERE players_test.name='" + player_name + "' AND levels_test.level_id=" + level_number +
               " ORDER BY score DESC LIMIT 1")

highscores = [(row[0], row[1], row[2]) for row in cursor.fetchall()]
print(json.dumps(highscores))

