-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--players is designed to hold just the players registering and assigning them with unique ID
CREATE TABLE players ( id SERIAL PRIMARY KEY,
                       name TEXT );

--matches is designed to give unique ID to every match played and stores the id of winner and loser
CREATE TABLE matches ( matchid SERIAL PRIMARY KEY,
                       winner INTEGER,
                       loser INTEGER );                      

--scoreboard is designed to store the cumulative score of players along with their id and total number of matches played
CREATE TABLE scoreboard ( player INTEGER,
                          score INTEGER,
                          matches INTEGER );
                        
