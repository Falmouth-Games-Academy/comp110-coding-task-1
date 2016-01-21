# COMP110 Coding Task 1
I designed the database and high scores processing algorithms to interact with my Kivy game project.  
The primary key for levels is not auto-incremented, as level names are added corresponding to the level number, and the level number is used as the primary key.  
If any of the requests fail to retrieve or add the requested data, they print None. This is to make it easier to for my Kivy game to know the results of its request. 

##Locations of Algorithms Required for Assignment

|Algorithm|File|
|---|---|
|retrieve the top 10 high scores from a database server|getscores.py|
|retrieve the highest score of a given user|getbest.py|
|insert new users |adduser.py|
|update user names ||
|insert new high scores into the database server|submitscore.py|
|update high scores in the database|updatescore.py|
