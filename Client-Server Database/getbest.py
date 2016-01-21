#!/usr/bin/python

"""Get the highest score for a particular player on a particular level.

The code in this module processes a get request and prints the highest
score for the requested player and level.
"""

import cgi
import cgitb
import json

import pymysql

import processing


def get_best_score(player_name, level_number):
    """Return the best score for the given player and level.

    This function returns the best score for the given player
    on the given level. If the player does not have a score on
    that level, it returns None.
    """

    connection, cursor = processing.connect_to_database()
    cursor.execute("SELECT score FROM scores "
                   "INNER JOIN players ON scores.player_id = players.player_id "
                   "INNER JOIN levels ON scores.level_id = levels.level_id "
                   "WHERE players.player_name='" + player_name + "' AND levels.level_id=" + level_number)
    best_score = [(row[0]) for row in cursor.fetchall()]

    # If length isn't greater than 0 there is no existing best score
    if len(best_score) > 0:
        return best_score[0]
    else:
        return None


if __name__ == "__main__":
    # Turn on debug mode
    cgitb.enable()
    # Print necessary headers
    print("Content-Type: text/html; charset=utf-8\n\n")

    form = cgi.FieldStorage()
    player_name = processing.get_player_name(form)
    level_number = processing.get_level_number(form)

    if player_name is not None and level_number is not None:
        best_score = get_best_score(player_name, level_number)
        if best_score is not None:
            print(json.dumps(best_score))
        else:
            # If score doesn't exist for that player/level
            print(json.dumps(None))
    else:
        # If player/level not provided
        print(json.dumps(None))
