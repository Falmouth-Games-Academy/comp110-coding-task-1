#!/usr/bin/python

# Turn on debug mode.
import cgitb
import pymysql
import json

cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html; charset=utf-8\n\n")

import cgi
form = cgi.FieldStorage()

# Connect to the database.
conn = pymysql.connect(
    db='highscores',
    user='root',
    passwd='samwillsfal',
    host='localhost')
c = conn.cursor()

def add_score_player():
    first_name = str(form.getvalue('first_name'))
    last_name = str(form.getvalue('last_name'))
    score = str(form.getvalue('score'))

    add_new_player = ("INSERT INTO players "
    "(first_name, last_name) "
    "VALUES (%s, %s)")

    add_player_score = ("INSERT INTO scores "
    "(player_id, score) "
    "VALUES (%(player_id)s, %(score)s)")

    new_player = (first_name, last_name)
    c.execute(add_new_player, new_player)
    player_id = c.lastrowid

    new_score = {
        'player_id': player_id,
        'score': score,
    }

    c.execute(add_player_score, new_score)

    conn.commit()
    
'''
The main gets request from form then displays appropriate text or error.
'''
def main():

    if 'request' not in form:
        print("Missing request")
    else:
        request = str(form.getvalue('request'))
        if request == 'add_players_score':
            add_score_player()

if __name__ == "__main__":
    main()
