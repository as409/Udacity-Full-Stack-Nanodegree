-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


Create database tournament;
\c tournament;

CREATE table players(
	player_id serial primary key,
	name text,                                        -- VARCHAR(30) NOT NULL,
	wins integer default 0,
	matches integer default 0
);

CREATE Table matches(
	match_id serial primary key,
	winner_id serial references players(player_id),
	loser_id  serial references players(player_id)
);
