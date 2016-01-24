CREATE DATABASE high_scores
USE high_scores

CREATE TABLE players
(
ID int NOT NULL AUTO_INCREMENT
name VARCHAR(3)
PRIMARY KEY (ID)
);

CREATE TABLE levels
(
ID int NOT NULL AUTO_INCREMENT
name VARCHAR(5)
PRIMARY KEY (ID)
);

CREATE TABLE scores
(
player_ID int(11)
level_ID int (11)
score int(11)
PRIMARY KEY (player_ID, level_ID)
);

SELECT players.name, scores.player_ID
FROM scores
INNER JOIN players
ON scores.player_ID = players.ID;

SELECT levels.name, scores.level_ID
FROM scores
INNER JOIN levels
ON scores.level_ID = levels.ID;