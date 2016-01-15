#!/usr/bin/python

import json

import pymysql

# Print necessary headers
print("Content-Type: text/html; charset=utf-8\n\n")

# Connect to the database
conn = pymysql.connect(
        db='highscores',
        user='root',
        passwd='falser110',
        host='localhost')
cursor = conn.cursor()

# Get the top 10 high scores from the database
cursor.execute("SELECT players_test.name, levels_test.level_name, score FROM scores_test "
          "INNER JOIN players_test ON scores_test.player_id = players_test.player_id "
          "INNER JOIN levels_test ON scores_test.level_id = levels_test.level_id "
          "ORDER BY score DESC LIMIT 10")

highscores = [(row[0], row[1], row[2]) for row in cursor.fetchall()]
print(json.dumps(highscores))

