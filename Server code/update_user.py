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


def update_user(c, conn, new_name, playername):
    # Insert new user
    c.execute("UPDATE players SET name = '"+ new_name +"' WHERE  name = '" + playername + "'")
    conn.commit()


def print_results(c):
    c.execute("SELECT * FROM players")
    print([(r[0], r[1]) for r in c.fetchall()])

def main():
    conn = connect_to_database()
    c = conn.cursor()

    form = cgi.FieldStorage()

    if "playername" not in form or "new_name" not in form:
            print("Error: Missing data.")
    else:
        playername = str(form.getvalue('playername'))
        new_name = str(form.getvalue('new_name'))
        update_user(c, conn, new_name, playername)
        print_results(c)


if __name__ == "__main__":
    main()
