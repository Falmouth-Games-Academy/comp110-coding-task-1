#!/usr/bin/python

# Turn on debug mode
import cgitb
import cgi
import json
import pymysql

import processing


def update_score(player_id, level_number, score):
    connection, cursor = processing.connect_to_database()

    cursor.execute("UPDATE scores_test SET scores_test.score='" + score + "' "
                   "WHERE scores_test.player_id='" + player_id + "' AND "
                   "scores_test.level_id='" + level_number + "'")
    connection.commit()


def is_best(player_id, level_number, score):
    connection, cursor = processing.connect_to_database()

    cursor.execute("SELECT score FROM scores_test "
                   "WHERE scores_test.player_id='" + player_id + "' AND "
                   "scores_test.level_id='" + level_number + "'")

    current_best = [(row[0]) for row in cursor.fetchall()]

    if int(score) > current_best[0]:
        return True
    else:
        return False


if __name__ == "__main__":
    cgitb.enable()
    # Print necessary headers
    print("Content-Type: text/html; charset=utf-8\n\n")

    form = cgi.FieldStorage()
    player_name = processing.get_player_name(form)
    player_id = processing.get_player_id(player_name)
    level_number = processing.get_level_number(form)
    score = processing.get_score(form)

    if is_best(player_id, level_number, score):
        update_score(player_id, level_number, score)
        print(json.dumps([player_name, level_number, score]))
    else:
        print(json.dumps(None))