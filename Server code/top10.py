#!/usr/bin/python
# Turn on debug mode.

import cgitb
import pymysql
import json
import connect_to_database
cgitb.enable()

"""top10.py retrieves the top 10 highest scores from the scores table and prints them in descending order"""

# Print necessary headers.
print("Content-Type: text/html; charset=utf-8\n\n")


def print_results(cursor):
    # Print the top 10 scores in the database.
    cursor.execute("SELECT players.name, levels.name, scores.score FROM scores "
                   "INNER JOIN players ON scores.player_ID = players.ID "
                   "INNER JOIN levels ON scores.level_ID = levels.ID "
                   "ORDER BY score DESC LIMIT 10")
    results = [(r[0], r[1], r[2]) for r in cursor.fetchall()]
    scores = str(results)
    scores = scores.replace('[', ' ')
    scores = scores.replace("'", " ")
    scores = scores.replace(']', ' ')
    print("Top 10 Scores")
    print(json.dumps(scores))


def main():
    conn = connect_to_database.connect()
    cursor = conn.cursor()
    print_results(cursor)

if __name__ == "__main__":
    main()