#!/usr/bin/python
# Turn on debug mode.

import cgitb
import cgi
import pymysql
import json

cgitb.enable()


# Print necessary headers.
print("Content-Type: text/html; charset=utf-8\n\n")


# Connect to the database.
def connect_to_database():
    """
    This function creates a connection to the high_scores database
    :return: connection
    """
    conn = pymysql.connect(
        db='high_scores',
        user='root',
        passwd='ImprobableDreams',
        host='localhost')
    return conn


def insert_player(c, conn, playername):
    # Insert new user into the players database
    c.execute("INSERT INTO players VALUES (NULL,'" + playername + "')")
    conn.commit()


def print_results(c):
    # Print the contents of the players table
    c.execute("SELECT * FROM players")
    players = [(r[0], r[1]) for r in c.fetchall()]
    print(json.dumps(players))


def main():
    conn = connect_to_database()
    c = conn.cursor()

    form = cgi.FieldStorage()

    if "playername" not in form:
            print("Error: No username entered")
    else:
            playername = str(form.getvalue('playername'))
            insert_player(c, conn, playername)
            print_results(c)

if __name__ == "__main__":
    main()
