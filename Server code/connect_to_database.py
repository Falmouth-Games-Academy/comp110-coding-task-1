#!/usr/bin/python
# Turn on debug mode.

import cgitb
import pymysql

cgitb.enable()

""" connect_to_database.py contains a function that connects to the high_scores database."""

def connect():
    """
    This function creates a connection to the high_scores database
    :return: connection
    """
    connection = pymysql.connect(
        db='high_scores',
        user='root',
        passwd='ImprobableDreams',
        host='localhost')
    return connection
