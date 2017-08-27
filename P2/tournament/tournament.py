#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn=connect()
    c=conn.cursor()
    c.execute('delete from matches')
    c.execute('UPDATE players SET wins = 0;')          # Made error here
    c.execute('UPDATE players SET matches = 0;')      # Made error here
    conn.commit()
    conn.close()

def deletePlayers():
    """Remove all the player records from the database."""
    conn=connect()
    c=conn.cursor()
    c.execute('delete from players')
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn=connect()
    c=conn.cursor()
    c.execute('select count(player_id) as num from players')
    c=(c.fetchone())[0]
    conn.close()
    return c


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:               

      name: the player's full name (need not be unique).
    """
    conn=connect()
    c=conn.cursor()
    c.execute('Insert into players (name) values (%s)', (name,))  
    conn.commit()
    conn.close()
    return c



def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn=connect()
    c=conn.cursor()
    c.execute('select * from players order by wins DESC')
    results=c.fetchall()
    conn.close()
    return results


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn=connect()
    c=conn.cursor()
    add_match_query = 'INSERT INTO matches (winner_id, loser_id) VALUES ({0}, {1});'.format(winner, loser)               # Important 
    add_winner_query = 'UPDATE players SET matches=matches+1, wins=wins+1 WHERE player_id = {0};'.format(winner)         
    add_loser_query = 'UPDATE players SET matches=matches+1 WHERE player_id = {0};'.format(loser)
    c.execute(add_match_query)
    c.execute(add_winner_query)
    c.execute(add_loser_query)
    conn.commit()
    conn.close()


 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    pairings = []
    players = playerStandings()
    if len(players) < 2:
        raise KeyError("Not enough players.")
    for i in range(0, len(players), 2):
        pairings.append((players[i][0], players[i][1], players[i+1][0], players[i+1][1]))
    return pairings
