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

    connection, cursor = processing.connect_to_database()

    cursor.execute("SELECT players_test.name, levels_test.level_name, scores_test.score FROM scores_test "
                   "INNER JOIN players_test ON scores_test.player_id = players_test.player_id "
                   "INNER JOIN levels_test ON scores_test.level_id = levels_test.level_id "
                   "WHERE players_test.name='" + player_name + "' AND levels_test.level_id=" + level_number +
                   " ORDER BY score DESC LIMIT 1")

    best_score = [(row[0], row[1], row[2]) for row in cursor.fetchall()]

    if len(best_score) > 0:
        return best_score[0][2]
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
            print(json.dumps(None))
    else:
        print(json.dumps(None))
