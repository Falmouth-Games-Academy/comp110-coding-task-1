CREATE DATABASE highscores;
USE highscores;
CREATE TABLE levels(level_id INT NOT NULL, level_name VARCHAR(30) NOT NULL, PRIMARY KEY(level_id));
CREATE TABLE players(player_id INT NOT NULL AUTO_INCREMENT, player_name VARCHAR(3) NOT NULL, PRIMARY KEY(player_id));
CREATE TABLE scores(player_id INT NOT NULL, level_id INT NOT NULL, score INT NOT NULL, PRIMARY KEY(player_id, level_id));
