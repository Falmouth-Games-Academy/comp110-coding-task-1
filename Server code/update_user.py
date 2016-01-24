#!/usr/bin/python
# Turn on debug mode.

import cgitb
import cgi
import pymysql
import json
import connect_to_database

cgitb.enable()

""" update_user.py allows a player to change their name in the players table"""

# Print necessary headers.
print("Content-Type: text/html; charset=utf-8\n\n")


def update_user(cursor, conn, new_name, playername):
    # Insert new user
    cursor.execute("UPDATE players SET name = '"+ new_name +"' WHERE  name = '" + playername + "'")
    conn.commit()


def print_results(cursor):
    cursor.execute("SELECT * FROM players")
    players = [(r[0], r[1]) for r in cursor.fetchall()]
    print(json.dumps(players))


def main():
    conn = connect_to_database.connect()
    cursor = conn.cursor()

    form = cgi.FieldStorage()

    if "playername" not in form or "new_name" not in form:
            print("Error: Missing data.")
    else:
        playername = str(form.getvalue('playername'))
        new_name = str(form.getvalue('new_name'))
        update_user(cursor, conn, new_name, playername)
        print_results(cursor)


if __name__ == "__main__":
    main()
