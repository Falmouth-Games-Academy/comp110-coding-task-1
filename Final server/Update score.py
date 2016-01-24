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
The main gets request from form then displays appropriate text or error.
'''
def main():

    if 'request' not in form:
        print("Missing request")
    else:
        request = str(form.getvalue('request'))
        if request == 'update_score':
            update_score()

if __name__ == "__main__":
    main()
