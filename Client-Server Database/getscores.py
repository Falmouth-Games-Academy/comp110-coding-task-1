#!/usr/bin/python

"""Respond with a list of the the top 10 high scores.
"""

import cgi
import cgitb
import json

import pymysql

import processing

def get_top_ten(level_number):
    connection, cursor = processing.connect_to_database()

    # Get the top 10 high scores from the database, list the highest first
    cursor.execute("SELECT players_test.name, levels_test.level_name, score FROM scores_test "
                   "INNER JOIN players_test ON scores_test.player_id = players_test.player_id "
                   "INNER JOIN levels_test ON scores_test.level_id = levels_test.level_id "
                   "WHERE scores_test.level_id='" + level_number + "' "
                   "ORDER BY score DESC LIMIT 10")

    highscores = [(row[0], row[1], row[2]) for row in cursor.fetchall()]
    return highscores

if __name__ == "__main__":
    cgitb.enable()
    # Print necessary headers
    print("Content-Type: text/html; charset=utf-8\n\n")

    form = cgi.FieldStorage()
    level_number = processing.get_level_number(form)

    if level_number is not None:
        highscores = get_top_ten(level_number)
        print(json.dumps(highscores))
    else:
        print(json.dumps(None))

