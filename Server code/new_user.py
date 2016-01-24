#!/usr/bin/python
# Turn on debug mode.

import cgitb
import cgi
import pymysql
import json
import connect_to_database

cgitb.enable()

"""new_user.py adds a new user to the players table"""

# Print necessary headers.
print("Content-Type: text/html; charset=utf-8\n\n")


def insert_player(cursor, conn, playername):
    # Inserts a new player into the players database
    cursor.execute("INSERT INTO players VALUES (NULL,'" + playername + "')")
    conn.commit()


def print_results(cursor):
    # Prints the contents of the players table
    cursor.execute("SELECT * FROM players")
    players = [(r[0], r[1]) for r in cursor.fetchall()]
    print(json.dumps(players))


def main():
    conn = connect_to_database.connect()
    cursor = conn.cursor()

    form = cgi.FieldStorage()

    if "playername" not in form:
            print("Error: No username entered")
    else:
            playername = str(form.getvalue('playername'))
            insert_player(cursor, conn, playername)
            print_results(cursor)

if __name__ == "__main__":
    main()
