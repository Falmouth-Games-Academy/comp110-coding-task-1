"""Store functions for processing data.

This module contains functions for processing data.
"""

import cgi

import pymysql

def get_player_name(form):
    if "player" not in form:
        return None
    else:
        player_name = str(form.getvalue("player")).upper()
        player_name = chop_name(player_name, 3)
        return player_name

def get_level_number(form):
    if "level" not in form:
        return None
    else:
        level_number = form.getvalue("level")
        return level_number

def get_score(form):
    if "score" not in form:
        return None
    else:
        score = form.getvalue("score")
        return score

def chop_name(name, characters):
    chopped_name = name[:characters]
    return chopped_name

def get_player_id(player_name):
    # Connect to the database
    connection, cursor = connect_to_database()

    cursor.execute("SELECT players_test.player_id FROM players_test "
                   "WHERE players_test.name='" + player_name + "'")
    player_id = [row[0] for row in cursor.fetchall()]
    if len(player_id) != 0:
        # Convert to string for consistency
        return str(player_id[0])
    else:
        return None

def connect_to_database():
    # Connect to the database
    connection = pymysql.connect(
            db='highscores',
            user='root',
            passwd='falser110',
            host='localhost')
    cursor = connection.cursor()
    return connection, cursor

