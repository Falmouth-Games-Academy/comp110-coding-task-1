#!/usr/bin/python

"""Add a new player to the table of players"""

import cgi
import cgitb
import json

import pymysql

import processing


def username_is_unique(username):
    """Check if a username does not already exist.

    This function checks if a username does not already
    exist in the highscores database. If the user doesn't
    already exist, it returns True. Otherwise, it returns False
    """

    connection, cursor = processing.connect_to_database()
    # Get list of all existing users
    cursor.execute("SELECT players_test.name FROM players_test")
    existing_users = [(row[0]) for row in cursor.fetchall()]

    # Only one of each name will be allowed
    if username not in existing_users:
        return True
    else:
        return False


def add_user_to_database(username):
    """Add a username to the database.

    This function will add a player with the given username
    to the players table of the highscores database.
    """

    connection, cursor = processing.connect_to_database()

    cursor.execute("INSERT INTO players_test VALUES(null, '" + username + "')")
    connection.commit()


if __name__ == '__main__':
    # Turn on debug mode
    cgitb.enable()
    # Print necessary headers
    print("Content-Type: text/html; charset=utf-8\n\n")

    form = cgi.FieldStorage()
    username = processing.get_player_name(form)

    if username is not None and username_is_unique(username):
        add_user_to_database(username)
        print(json.dumps(username))
    else:
        # If username already taken or not provided
        print(json.dumps(None))

