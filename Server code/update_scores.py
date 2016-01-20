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
    # This function creates a connection to the high_scores database
    conn = pymysql.connect(
        db='high_scores',
        user='root',
        passwd='ImprobableDreams',
        host='localhost')
    return conn


def get_id(c, playername):
    c.execute("SELECT * FROM players WHERE players.name ='" + playername + "' LIMIT 1")
    fetch_ID = ([(r[0]) for r in c.fetchall()])
    player_ID = str(fetch_ID[0])
    return player_ID
    # Needs to be able to deal with player not existing


def update_score(c, conn, playerID, level, score):
    # Insert playerID, level and score in scores table
    c.execute("UPDATE scores SET score = " + score +" WHERE player_ID = " +playerID + " AND level_ID = "+ level +" ")
    conn.commit()
    #Needs to find duplicate enteries


def print_scores(c):
    # Print the contents of the scores table
    c.execute("SELECT * FROM scores")
    scores = [(r[0], r[1], r[2]) for r in c.fetchall()]
    print(json.dumps(scores))


def main():
    conn = connect_to_database()
    c = conn.cursor()
    form = cgi.FieldStorage()

    if "playername" not in form or "level" not in form or "score" not in form:
        print("Error: Missing data.")
    else:
        playername = str(form.getvalue('playername'))
        level = str(form.getvalue('level'))
        score = str(form.getvalue('score'))
        player_ID = get_id(c, playername)
        update_score(c, conn, player_ID, level, score)
        print_scores(c)

if __name__ == "__main__":
    main()
