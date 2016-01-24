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

'''
Greet the player using the first_name from form.
'''
def greet_player():
    if 'first_name' not in form:
        print("Something went wrong")
    else:
        print("<b>Hello " + str(form.getvalue("first_name")) + "</b>")

'''
Get the string values from the form.
'''
def get_name_score():
    if 'first_name' and 'last_name' and 'score' not in form:
        print ("Where are first name, last name, score?")
    else:
        first_name = str(form.getvalue('first_name'))
        last_name = str(form.getvalue('last_name'))
        score = str(form.getvalue('score'))

'''
Using the form strings insert new values into the database.
'''
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
Update the player name using the new first and last name from the form.
'''
def update_player():
    first_name = str(form.getvalue('first_name'))
    new_first_name = str(form.getvalue('new_first_name'))
    last_name = str(form.getvalue('last_name'))
    new_last_name = str(form.getvalue('new_last_name'))
    score = str(form.getvalue('score'))
    print("Hello " + first_name + " You want to change your name to " + new_first_name)

    update_player = c.execute("UPDATE players "
    "SET first_name=%s, last_name=%s WHERE first_name=%s",
    (new_first_name, new_last_name, first_name))

    conn.commit()
    print ("Name updated")

'''
Update the score using the first name from form.
'''
def update_score():
    first_name = str(form.getvalue('first_name'))
    last_name = str(form.getvalue('last_name'))
    score = str(form.getvalue('score'))

    get_id = c.execute("SELECT id FROM players "
    "WHERE first_name=%s",
    (first_name))

    get_number = ([(r[0]) for r in c.fetchall()])
    id = get_number[0]
    player_id = str(json.dumps(id))

    update_score = c.execute("UPDATE scores "
    "SET score=%s WHERE player_id=%s",
    (score, player_id))

    conn.commit()
    print("Score updated")

'''
Print all the players in the database.
'''
def print_players():
    c.execute("SELECT * FROM players")
    players = [(r[0], r[1], r[2]) for r in c.fetchall()]
    print (json.dumps(players))

'''
Print all the scores with player names.
'''
def print_scores():
# Print the contents of the database.
    c.execute("SELECT players.first_name, players.last_name, scores.score FROM scores INNER JOIN players ON player_id = players.id")
    print ("<b>All scores</b><br/>")
    scores = ([(r[0], r[1], r[2]) for r in c.fetchall()])
    print (json.dumps(scores))

'''
Print the top 10 scores in the database with player names.
'''
def print_highscores():
    c.execute("SELECT players.first_name, players.last_name, scores.score FROM scores INNER JOIN players ON player_id = players.id ORDER BY score DESC LIMIT 10")
    print ("<b>Top 10 scores</b><br />")
    scores = [(r[0], r[1], r[2]) for r in c.fetchall()]
    print (json.dumps(scores))

'''
Print the top score with player name.
'''
def print_highscore():
    c.execute("SELECT players.first_name, players.last_name, scores.score FROM scores INNER JOIN players ON player_id = players.id ORDER BY score DESC LIMIT 1")
    print ("<b>Top score</b><br />")
    scores = ([(r[0], r[1], r[2]) for r in c.fetchall()])
    print (json.dumps(scores))

'''
A break in between text.
'''
def print_break():
    print ("<br/><br/>")

'''
The main gets request from form then displays appropriate text or error.
'''
def main():

    if 'request' not in form:
        print("Missing request")
    else:
        request = str(form.getvalue('request'))
        if request == 'all':
            print_players()
            print_break()
            print_scores()
            print_break()
            print_highscores()
            print_break()
            print_highscore()
        elif request == 'top_score':
            print_highscore()
        elif request == 'top_scores':
            print_highscores()
        elif request == 'add_players_score':
            add_score_player()
        elif request == 'update_player':
            update_player()
        elif request == 'update_score':
            update_score()
        elif request == 'greet':
            greet_player()

if __name__ == "__main__":
    main()
