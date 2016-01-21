#!/usr/bin/python

"""Add a new player to the table of players.

The code in this file adds a new player to the
table of players in the database.
"""

import cgi
import cgitb
import json

import pymysql

import processing


def add_user_to_database(username):
    """Add a username to the database.

    This function will add a player with the given username
    to the players table of the highscores database.
    """

    connection, cursor = processing.connect_to_database()
    # Insert the new user
    cursor.execute("INSERT INTO players VALUES(null, '" + username + "')")
    connection.commit()


if __name__ == '__main__':
    # Turn on debug mode
    cgitb.enable()
    # Print necessary headers
    print("Content-Type: text/html; charset=utf-8\n\n")

    form = cgi.FieldStorage()
    username = processing.get_player_name(form)

    if username is not None and processing.username_is_unique(username):
        add_user_to_database(username)
        print(json.dumps(username))
    else:
        # If username already taken or not provided
        print(json.dumps(None))

