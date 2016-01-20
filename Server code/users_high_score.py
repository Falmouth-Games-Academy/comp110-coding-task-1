#!/usr/bin/python
# Turn on debug mode.

import cgitb
import cgi
import pymysql
import json

cgitb.enable()


# Print necessary headers.
print("Content-Type: text/html; charset=utf-8\n\n")


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


def print_results(c, playerID,  playername):
    # Print the user's top scores in the database.
    c.execute("SELECT * FROM scores WHERE "+ playerID +" = scores.player_ID")
    print (playername + "'s high scores")
    scores = [(r[0], r[1], r[2]) for r in c.fetchall()]
    print(json.dumps(scores))


def get_id(c, playername):
    c.execute("SELECT * FROM players WHERE players.name ='" + playername + "' LIMIT 1")
    fetch_ID =([(r[0]) for r in c.fetchall()])
    player_ID =str(fetch_ID[0])
    return player_ID
    # Needs to be able to deal with player not existing

def main():
    conn = connect_to_database()
    c = conn.cursor()
    form = cgi.FieldStorage()

    if "playername" not in form:
        print("Error")
    else:
        playername = str(form.getvalue('playername'))
        player_ID = get_id(c, playername)
        print_results(c, player_ID, playername)

if __name__ == "__main__":
    main()