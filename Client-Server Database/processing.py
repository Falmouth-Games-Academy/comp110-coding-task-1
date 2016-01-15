"""Store functions for processing data.

This module contains functions for processing data.
"""

import pymysql

def chop_name(name, characters):
    chopped_name = name[:characters]
    return chopped_name

def get_player_id(player_name):
    # Connect to the database
    conn = pymysql.connect(
            db='highscores',
            user='root',
            passwd='falser110',
            host='localhost')
    cursor = conn.cursor()


    cursor.execute("SELECT players_test.player_id FROM players_test "
                   "WHERE players_test.name='" + player_name + "'")
    player_id = [row[0] for row in cursor.fetchall()]
    return player_id