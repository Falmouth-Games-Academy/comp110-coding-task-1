#!/usr/bin/python
# Turn on debug mode.

import cgitb
import cgi
import pymysql
import json
import connect_to_database

cgitb.enable()

"""users_high_score.py retrieves the high scores for a specific user for each level"""

# Print necessary headers.
print("Content-Type: text/html; charset=utf-8\n\n")


def print_results(cursor, playerid,  playername):
    # Print the user's top scores in the database.
    cursor.execute("SELECT players.name, levels.name, scores.score FROM scores "
                   "INNER JOIN players ON scores.player_ID = players.ID "
                   "INNER JOIN levels ON scores.level_ID = levels.ID "
                   "WHERE " + playerid + " = scores.player_ID")
    print (playername + "'s high scores")
    scores = [(r[0], r[1], r[2]) for r in cursor.fetchall()]
    print(json.dumps(scores))


def get_id(cursor, playername):
    cursor.execute("SELECT * FROM players WHERE players.name ='" + playername + "' LIMIT 1")
    fetch_id = ([(r[0]) for r in cursor.fetchall()])
    player_ID = str(fetch_id[0])
    return player_ID


def main():
    conn = connect_to_database.connect()
    cursor = conn.cursor()
    form = cgi.FieldStorage()

    if "playername" not in form:
        print("Error")
    else:
        playername = str(form.getvalue('playername'))
        player_id = get_id(cursor, playername)
        print_results(cursor, player_id, playername)

if __name__ == "__main__":
    main()
