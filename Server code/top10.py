#!/usr/bin/python
# Turn on debug mode.

import cgitb
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


def print_results(c):
    # Print the top 10 scores in the database.
    c.execute("SELECT * FROM scores ORDER BY score DESC")
    print ("Top 10 scores")
    scores = [(r[0], r[1], r[2]) for r in c.fetchall()]
    print(json.dumps(scores))


def main():
    conn = connect_to_database()
    c = conn.cursor()
    print_results(c)

if __name__ == "__main__":
    main()

