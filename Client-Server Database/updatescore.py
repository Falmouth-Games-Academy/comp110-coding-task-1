#!/usr/bin/python

"""Update an existing highscore in the database.

This code updates a player's existing highscore in the database,
if the new score is higher.
"""

import cgi
import cgitb
import json

import pymysql

import processing


def update_score(player_id, level_number, score):
    """Update a score in the database.

    This function updates an existing score in the
    database for a particular player and level.
    """

    connection, cursor = processing.connect_to_database()
    cursor.execute("UPDATE scores SET score='" + score + "' "
                   "WHERE player_id='" + player_id + "' AND "
                   "level_id='" + level_number + "'")
    connection.commit()


def is_best(player_id, level_number, score):
    """Ensure that the score is the player's highest for that level.

    This function checks that the new score is actually better than
    the existing score. If the new score is higher, it returns True.
    If the new score is lower or an old score doesn't exist, it returns
    False.
    """

    connection, cursor = processing.connect_to_database()
    cursor.execute("SELECT score FROM scores "
                   "WHERE player_id='" + player_id + "' AND "
                   "level_id='" + level_number + "'")
    current_best = [(row[0]) for row in cursor.fetchall()]

    # There isn't an existing score if length of list is 0
    if len(current_best) != 0 and int(score) > current_best[0]:
        return True
    else:
        return False


if __name__ == "__main__":
    # Turn on debug mode
    cgitb.enable()
    # Print necessary headers
    print("Content-Type: text/html; charset=utf-8\n\n")

    form = cgi.FieldStorage()
    player_name = processing.get_player_name(form)
    level_number = processing.get_level_number(form)
    score = processing.get_score(form)

    if player_name != None and level_number != None and score != None:
        player_id = processing.get_player_id(player_name)

        if player_id != None and is_best(player_id, level_number, score):
            update_score(player_id, level_number, score)
            print(json.dumps([player_name, level_number, score]))
        else:
            # If player doesn't exist of score isn't best
            print(json.dumps(None))

    else:
        # If player/level/score not provided
        print(json.dumps(None))