#!/usr/bin/python
# Turn on debug mode.

import cgitb
import cgi
import pymysql
import json
import connect_to_database

cgitb.enable()

"""update_score.py updates the players score for a specific level """

# Print necessary headers.
print("Content-Type: text/html; charset=utf-8\n\n")


def get_id(cursor, playername):
    cursor.execute("SELECT * FROM players WHERE players.name ='" + playername + "' LIMIT 1")
    fetch_id = ([(r[0]) for r in cursor.fetchall()])
    player_id = str(fetch_id[0])
    return player_id


def update_score(cursor, conn, playerID, level, score):
    # Inserts playerID, level and score in scores table
    cursor.execute("UPDATE scores SET score = " + score +" WHERE player_ID = " +playerID + " AND level_ID = "+ level +" ")
    conn.commit()


def print_scores(cursor):
    # Print the contents of the scores table
    cursor.execute("SELECT players.name, levels.name, scores.score FROM scores "
                   "INNER JOIN players ON scores.player_ID = players.ID "
                   "INNER JOIN levels ON scores.level_ID = levels.ID "
                   "ORDER BY score DESC LIMIT 10")
    results = [(r[0], r[1], r[2]) for r in cursor.fetchall()]
    scores = str(results)
    scores = scores.replace('[', ' ')
    scores = scores.replace("'", " ")
    scores = scores.replace(']', ' ')
    print(json.dumps(scores))


def main():
    conn = connect_to_database.connect()
    cursor = conn.cursor()
    form = cgi.FieldStorage()

    if "playername" not in form or "level" not in form or "score" not in form:
        print("Error: Missing data.")
    else:
        playername = str(form.getvalue('playername'))
        level = str(form.getvalue('level'))
        score = str(form.getvalue('score'))
        player_ID = get_id(cursor, playername)
        update_score(cursor, conn, player_ID, level, score)
        print_scores(cursor)

if __name__ == "__main__":
    main()
