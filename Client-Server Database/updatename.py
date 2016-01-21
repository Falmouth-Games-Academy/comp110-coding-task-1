#!/usr/bin/python

"""Update the name of a given player.

The code in this file updates the name of a given
player stored in the table of players in the highscores
database.
"""

import cgi
import cgitb
import json

import pymysql

import processing


def change_player_name(username, player_id):
    """Change the name of a given player.

    This function changes the name of the player
    corresponding to the given player id to the
    given name.
    """

    connection, cursor = processing.connect_to_database()
    # Change the appropriate username
    cursor.execute("UPDATE players SET player_name='" + username + "' "
                   "WHERE player_id='" + player_id + "'")
    connection.commit()


if __name__ == '__main__':
    # Turn on debug mode
    cgitb.enable()
    # Print necessary headers
    print("Content-Type: text/html; charset=utf-8\n\n")

    form = cgi.FieldStorage()
    current_name = processing.get_player_name(form)
    new_name = processing.get_new_name(form)

    if current_name is not None and new_name is not None:
        player_id = processing.get_player_id(current_name)

        if player_id is not None and processing.username_is_unique(new_name):
            change_player_name(new_name, player_id)
            print(json.dumps(new_name))
        else:
            # If player doesn't exist in database or new name isn't unique
            print(json.dumps(None))

    else:
        # If original name/new name not provided or new name already taken
        print(json.dumps(None))

