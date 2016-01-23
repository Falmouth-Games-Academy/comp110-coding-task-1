#!/usr/bin/python

"""Add a new score to the database.

This code adds a players' new highscore to the database,
relative to the player and the level.
"""


import cgi
import cgitb
import json
import pymysql

import processing


def score_empty(player_id, level_number):
    """Check if a username does not already exist.

    This function checks if an entry for the given level and player
    does not already exist in the highscores database. If it doesn't
    already exist, it returns True. Otherwise, it returns False
    """

    connection, cursor = processing.connect_to_database()
    # Get entry for that player and level
    cursor.execute("SELECT * FROM scores "
                   "WHERE player_id=%s AND level_id=%s", (player_id, level_number))
    scores = [(row[0], row[1]) for row in cursor.fetchall()]

    # Length of list is 0 if score for that player/level doesn't exist
    if len(scores) == 0:
        return True
    else:
        return False


def level_exists(level_number):
    """Check if a given level number already exists.

    This function checks if an entry for the given level already exists
    in the database. If it does exist, it returns False, if it doesn't exist,
    it returns True.
    """

    connection, cursor = processing.connect_to_database()
    # Get entry for that level number
    cursor.execute("SELECT * FROM levels WHERE level_id=%s", (level_number,))
    level = [(row[0], row[1]) for row in cursor.fetchall()]

    # Length of list is 0 if level doesn't exist
    if len(level) == 0:
        return False
    else:
        return True


def add_score(player_id, level_number, score):
    """Add a score to the database.

    This function adds a score for a given player and
    level to the database.
    """

    connection, cursor = processing.connect_to_database()
    # Insert the score
    cursor.execute("INSERT INTO scores VALUES(%s, %s, %s)", (player_id, level_number, score))
    connection.commit()


if __name__ == "__main__":
    cgitb.enable()
    # Print necessary headers
    print("Content-Type: text/html; charset=utf-8\n\n")

    form = cgi.FieldStorage()
    player_name = processing.get_player_name(form)
    level_number = processing.get_level_number(form)
    score = processing.get_score(form)

    if player_name != None and level_number != None and score != None:
        if not level_exists(level_number):
            processing.add_level(level_number)

        player_id = processing.get_player_id(player_name)
        if player_id != None and score_empty(player_id, level_number):
            add_score(player_id, level_number, score)
            print(json.dumps([player_name, level_number, score]))
        else:
            # If score already exists or player not in database
            print(json.dumps(None))

    else:
        # If player/level/score not provided
        print(json.dumps(None))