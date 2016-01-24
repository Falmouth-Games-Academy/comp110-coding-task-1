#!/usr/bin/python

# Turn on debug mode.
import cgitb
import pymysql
import json
#import mysql.connector

#cnx = mysql.connector.connect(user='root', database='highscores')
#cursor = cnx.cursor()
cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html; charset=utf-8\n\n")

import cgi
form = cgi.FieldStorage()
print ("Hello")
print ("<br />")
print ("<br />")
