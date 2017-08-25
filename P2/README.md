# Udacity: Intro to Relational Databases

# Final Project: Tournament Planner

## Table of Contents

- Project Overview
- Install
- Code
- Project Instruction
- Run

### Project Overview

In this project, you’ll be writing a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it.

Install

This project requires Python 2.7 and the following Python libraries installed:

Psycopg2
You will complete this project within the Vagrant virtual machine we've provided and configured for you. If you would like to review that before moving on refer to the course materials for help with installing Vagrant and Virtual Box, and previously recorded office hours where we'll show you how to use Vagrant.

Code

Code Templates

The templates for this project are in the tournament subdirectory of your VM’s /vagrant directory. You’ll find three files there: tournament.sql, tournament.py, and tournament_test.py.

tournament.sql - this file is used to set up your database schema (the table representation of your data structure).
tournament.py - this file is used to provide access to your database via a library of functions which can add, delete or query data in your database to another python program (a client program). Remember that when you define a function, it does not execute, it simply means the function is defined to run a specific set of instructions when called.
tournament_test.py - this is a client program which will use your functions written in the tournament.py module. We've written this client program to test your implementation of functions in tournament.py.
Project Instruction

Creating Your Database

Before you can run your code or create your tables, you'll need to use the create database command in psql to create the database. Use the name tournament for your database.

Then you can connect psql to your new database and create your tables from the statements you've written in tournament.sql. You can do this in either of two ways:

Paste each statement in to psql.
Use the command \i tournament.sql to import the whole file into psql at once. Remember, if you get your database into a bad state you can always drop tables or the whole database to clear it out.
Design Notes

Rely on the unit tests as you write your code. If you implement the functions in the order they appear in the file, the test suite can give you incremental progress information.

The goal of the Swiss pairings system is to pair each player with an opponent who has won the same number of matches, or as close as possible.

You can assume that the number of players in a tournament is an even number. This means that no player will be left out of a round.

Your code and database only needs to support a single tournament at a time. All players who are in the database will participate in the tournament, and when you want to run a new tournament, all the game records from the previous tournament will need to be deleted. In one of the extra-credit options for this project, you can extend this program to support multiple tournaments.

Functions in tournament.py

registerPlayer(name) Adds a player to the tournament by putting an entry in the database. The database should assign an ID number to the player. Different players may have the same names but will receive different ID numbers.

countPlayers() Returns the number of currently registered players. This function should not use the Python len() function; it should have the database count the players.

deletePlayers() Clear out all the player records from the database.

reportMatch(winner, loser) Stores the outcome of a single match between two players in the database.

deleteMatches() Clear out all the match records from the database.

playerStandings() Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.

swissPairings() Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system. Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the paired players. For instance, if there are eight registered players, this function should return four pairings. This function should use playerStandings to find the ranking of players.

Using the Vagrant Virtual Machine

The Vagrant VM has PostgreSQL installed and configured, as well as the psql command line interface (CLI), so that you don't have to install or configure them on your local machine.
To use the Vagrant virtual machine, navigate to the full-stack-nanodegree-vm/tournament directory in the terminal, then use the command vagrant up (powers on the virtual machine) followed by vagrant ssh (logs into the virtual machine).
Remember, once you have executed the vagrant ssh command, you will want to cd /vagrant to change directory to the synced folders in order to work on your project, once your cd /vagrant, if you type ls on the command line, you'll see your tournament folder.
The Vagrant VM provided in the the top repo already has PostgreSQL server installed, as well as the psql command line interface (CLI), so you'll need to have your VM on and be logged into it to run your database configuration file (tournament.sql), and test your Python file with tournament_test.py.
Using the psql command line interface

The very first time we start working on this project, no database will exist - so first, we'll need to create the SQL database for our tournament project. From psql, we can do this on the command line directly using a create statement or by importing tournament.sql (which then executes whatever commands are in the .sql script).
tournament.sql is where we'll create our database schema and views; we also have the option of creating the database and tables in this file.
With psql, you can run any SQL query on the tables of the currently connected database.
When using psql, remember to end SQL statements with a semicolon, which is not always required from Python.
To build and access the database we run psql followed by \i tournament.sql.
Run

Once you have your .sql and .py files set up, it’s a good idea to test them out against the testing file provided to you (tournament_test.py). To run the series of tests defined in this test suite, run the program from the command line $ python tournament_test.py.

You should be able to see the following output once all your tests have passed:


vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$
