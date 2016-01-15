#!/usr/bin/python

"""Add a new player to the table of players"""

import cgi
import cgitb
import json

import pymysql

import processing

# Turn on debug mode
cgitb.enable()

# Print necessary headers
print("Content-Type: text/html; charset=utf-8\n\n")


def add_user_to_database(username):
    """Add a username to the database.

    This function will add a player with the given username
    to the players table of the highscores database.
    """
    # Connect to the database
    conn = pymysql.connect(
            db='highscores',
            user='root',
            passwd='falser110',
            host='localhost')
    cursor = conn.cursor()

    # Get list of all existing users
    cursor.execute("SELECT players_test.name FROM players_test")
    existing_users = [(row[0]) for row in cursor.fetchall()]

    if username not in existing_users:
        cursor.execute("INSERT INTO players_test VALUES(null, '" + username + "')")
        conn.commit()

        cursor.execute("SELECT players_test.name FROM players_test WHERE players_test.name = '" + username + "'")
        print ([(row[0]) for row in cursor.fetchall()])
        print(json.dumps("Success!"))
    else:
        print("User '" + username + "' already exists.")

def get_username():
    """Retrive a username from the form and return it as a string after formatting.

    This method retrieves the player name provided in the
    request, and formats it so that it is suitable for a
    username in the high score table. It then returns the
    username as a string.
    """
    form = cgi.FieldStorage()
    if "player" not in form:
            print("Player name ('player') was not provided.")
    else:
            # Ensure that the name is upper case
            player_name = str(form.getvalue("player")).upper()
            # Ensure that name is only three characters
            username = processing.chop_name(player_name, 3)
            return username

if __name__ == '__main__':
    username = get_username()
    if username != None:
        add_user_to_database(username)

