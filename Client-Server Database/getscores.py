#!/usr/bin/python

"""Respond with a list of the the top 10 high scores.

The code in this file responds with a list of the
top 10 high scores for the given level.
"""

import cgi
import cgitb
import json

import pymysql

import processing

def get_top_ten(level_number):
    """Return a list of the top 10 high scores of a given level.

    This function retrieves a list of the top 10 high scores for
    the given level in descending order from the database, and
    then returns the list.
    """

    connection, cursor = processing.connect_to_database()
    # Get the top 10 high scores from the database, list the highest first
    cursor.execute("SELECT players.player_name, levels.level_name, score FROM scores "
                   "INNER JOIN players ON scores.player_id = players.player_id "
                   "INNER JOIN levels ON scores.level_id = levels.level_id "
                   "WHERE scores.level_id=%s"
                   "ORDER BY score DESC LIMIT 10", level_number)

    highscores = [(row[0], row[1], row[2]) for row in cursor.fetchall()]
    return highscores

if __name__ == "__main__":
    # Turn on debug mode
    cgitb.enable()
    # Print necessary headers
    print("Content-Type: text/html; charset=utf-8\n\n")

    form = cgi.FieldStorage()
    level_number = processing.get_level_number(form)

    if level_number is not None:
        highscores = get_top_ten(level_number)
        print(json.dumps(highscores))
    else:
        # If level number not provided
        print(json.dumps(None))

