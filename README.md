# COMP110 Coding Task 1
I designed the database and the high score processing algorithms to interact with my Kivy game project.  
The primary key for levels is not auto-incremented, as level names are added corresponding to the level number, and the level number is used as the primary key.  
If any of the requests are unable to retrieve or add the requested data, they print None. This is to make it easier to for my Kivy game to know the result of its request. 
Any functions that are used by more than one of the algorithms are located in processing.py.

Note: Commits have only happened in the last couple of weeks because I was leaving this project until last, as it is much smaller than the others. This project being much smaller than the others is also the reason for significantly less commits.

##Locations of Algorithms Required for Assignment

|Algorithm|File|
|---|---|
|retrieve the top 10 high scores from a database server|getscores.py|
|retrieve the highest score of a given user|getbest.py|
|insert new users |adduser.py|
|update user names |updatename.py|
|insert new high scores into the database server|submitscore.py|
|update high scores in the database|updatescore.py|
|SQL file|highscores.sql|

##Entity Relationship Diagram for Database
One player can have zero to many scores. One level can have zero to many scores. A score can have one and only one player. A score can have one and only one level.

![Entity Relationship Diagram](https://github.com/NecroReindeer/comp110-coding-task-1/blob/master/Client-Server%20Database/Entity%20Relationship%20Diagram.png)
