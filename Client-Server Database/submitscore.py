#!/usr/bin/python

"""Add a new score to the database.

This code adds a players' new highscore to the database,
relative to the player and the level.
"""

# Turn on debug mode
import cgitb
import cgi
import json
import pymysql

import processing


def score_empty(player_id, level_number):
    """Check if a username does not already exist.

    This function checks if a username does not already
    exist in the highscores database. If the user doesn't
    already exist, it returns True. Otherwise, it returns False
    """

    connection, cursor = processing.connect_to_database()
    # Get list of all existing users
    # Get the top 10 high scores from the database, list the highest first
    cursor.execute("SELECT scores_test.player_id, scores_test.level_id FROM scores_test "
                   "WHERE scores_test.player_id='" + player_id + "' AND "
                   "scores_test.level_id='" + level_number + "'")

    scores = [(row[0], row[1]) for row in cursor.fetchall()]

    # Length of list is 0 if score for that player/level doesn't exist
    if len(scores) == 0:
        return True
    else:
        return False


def add_score(player_id, level_number, score):
    connection, cursor = processing.connect_to_database()

    # Insert the score
    cursor.execute("INSERT INTO scores_test VALUES(" + player_id + ", " + level_number + ", " + score + ")")
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
        player_id = processing.get_player_id(player_name)

        if player_id != None and score_empty(player_id, level_number):
            add_score(player_id, level_number, score)
            print(json.dumps([player_name, level_number, score]))
        else:
            # If score already exists or player not yet added
            print(json.dumps(None))
    else:
        # If player/level/score not provided or doesn't exist
        print(json.dumps(None))