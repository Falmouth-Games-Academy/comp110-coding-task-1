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
print ("Hello")
print ("<br />")
print ("<br />")

#def greet_player():
    #if "player" not in form:
        #print ("Something Went Wrong")
    #else:
        #print("<b>Hello " + str(form.getvalue("player")) + "</b>")
        #my_first_int = 1
        #my_first_str = str(form.getvalue("user"))


# Connect to the database.
conn = pymysql.connect(
    db='highscores',
    user='root',
    passwd='samwillsfal',
    host='localhost')
c = conn.cursor()

def greet_player():
    if 'first_name' not in form:
        print("Something went wrong")
    else:
        print("<b>Hello " + str(form.getvalue("first_name")) + "</b>")

def get_name_score():
    if 'first_name' and 'last_name' and 'score' not in form:
        print ("Where are first name, last name, score?")
    else:
        first_name = str(form.getvalue('first_name'))
        last_name = str(form.getvalue('last_name'))
        score = str(form.getvalue('score'))

#def get_player_id():
    #first_name = str(form.getvalue('first_name'))
    #score = str(form.getvalue('score'))
    #c.execute("SELECT * FROM players WHERE players.first_name =  " 'first_name')
    #players_id = [(r[0]) for r in c.fetchall()]
    #print (players_id)
    #c.execute("UPDATE scores SET score = ' + score + ' WHERE player_id = " 'players_id')
    #print ("Score updated for ' + first_name + '")

    #conn.commit()

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


#def add_player(first_name, last_name):
# Insert some example data.
    #c.execute("INSERT INTO players VALUES (NULL, '"  + first_name + "', '" + last_name + "')")
    #conn.commit()

#def get_id(first_name):
    #c.execute("SELECT * FROM players WHERE first_name = " ' + first_name + ')
    #player_id = str([(r[0] for r in c.fetchall()])

#required get_id
#def add_score(first_name):
    #c.execute("SELECT id FROM players WHERE first_name = '" + first_name +"')
    #player_id = str(([(r[0]) for r in c.fetchall()]))
    #players_id = (json.dumps(player_id))
    #print = (player_id)
    #c.execute("INSERT INTO scores VALUES ('" + player_id + "', '" + score + "')")
    #conn.commit()

#def update_score(player_id):
    #c.execute("UPDATE scores SET score = ' + score + ' WHERE player_id = ' + player_id + '")
    #print ("Score updated")

def print_players():
    c.execute("SELECT * FROM players")
    players = [(r[0], r[1], r[2]) for r in c.fetchall()]
    print (json.dumps(players))

def print_scores():
# Print the contents of the database.
    c.execute("SELECT players.first_name, players.last_name, scores.score FROM scores INNER JOIN players ON player$
    print ("<b>All scores</b><br/>")
    scores = ([(r[0], r[1], r[2]) for r in c.fetchall()])
    print (json.dumps(scores))

def print_highscores():
    c.execute("SELECT players.first_name, players.last_name, scores.score FROM scores INNER JOIN players ON player$
#c.execute("SELECT * FROM scores")
#c.execute("SELECT * FROM players")
    print ("<b>Top 10 scores</b><br />")
    scores = [(r[0], r[1], r[2]) for r in c.fetchall()]
    print (json.dumps(scores))

def print_highscore():
    c.execute("SELECT players.first_name, players.last_name, scores.score FROM scores INNER JOIN players ON player$
    print ("<b>Top score</b><br />")
    scores = ([(r[0], r[1], r[2]) for r in c.fetchall()])
    print (json.dumps(scores))

def print_break():
    print ("<br/><br/>")

def main():

    #if 'first_name' and 'last_name' and 'score' not in form:
        #print("Missing values")
    #else:
        #first_name = str(form.getvalue('first_name')
        #last_name = str(form.getvalue('last_name')
        #score = str(form.getvalue('score')
        #print ("<b>Hello " %(first_name)s "</b>")

    greet_player()
    get_name_score()
    print_break()
    #get_player_id()

    add_score_player()

    #add_player()
    #get_id()
    #add_score()
    #update_score()
    print_players()
    print_break()
    print_scores()
    print_break()
    print_highscores()
    print_break()
    print_highscore()

if __name__ == "__main__":
    main()

