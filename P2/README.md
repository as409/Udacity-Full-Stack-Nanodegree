# Udacity: Intro to Relational Databases

## Final Project: Tournament Planner



### Project Overview

In this project, you’ll be writing a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it.

### Installing dependencies

- ```sudo apt-get install virtualbox```
- ```sudo apt-get install vagrant```








### Using the Vagrant Virtual Machine

- The Vagrant VM has PostgreSQL installed and configured, as well as the psql command line interface (CLI), so that you don't have to install or configure them on your local machine.
- To use the Vagrant virtual machine, navigate to the full-stack-nanodegree-vm/tournament directory in the terminal, then use the command vagrant up (powers on the virtual machine) followed by ```vagrant ssh``` (logs into the virtual machine).
- Remember, once you have executed the vagrant ssh command, you will want to ```cd /vagrant``` to change directory to the synced folders in order to work on your project, once your ```cd /vagrant```, if you type ```ls``` on the command line, you'll see your tournament folder.
- The Vagrant VM provided in the the top repo already has PostgreSQL server installed, as well as the psql command line interface (CLI), so you'll need to have your VM on and be logged into it to run your database configuration file (tournament.sql), and test your Python file with tournament_test.py.

### Using the psql command line interface

- The very first time we start working on this project, no database will exist - so first, we'll need to create the SQL database for our tournament project. From psql, we can do this on the command line directly using a create statement or by - - importing tournament.sql (which then executes whatever commands are in the .sql script).
tournament.sql is where we'll create our database schema and views; we also have the option of creating the database and tables in this file.
- With psql, you can run any SQL query on the tables of the currently connected database.
- When using psql, remember to end SQL statements with a semicolon, which is not always required from Python.
- To build and access the database we run ```psql``` followed by ```\i tournament.sql```
### Run

Once you have your .sql and .py files set up, it’s a good idea to test them out against the testing file provided to you (tournament_test.py). To run the series of tests defined in this test suite, run the program from the command line ```python tournament_test.py```

You should be able to see the following output once all your tests have passed:


vagrant@vagrant:/vagrant/tournament$ python tournament_test.py
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!

