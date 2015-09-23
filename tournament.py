#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        return(psycopg2.connect("dbname={}".format(database_name)))
    except:
        print("Error connecting to database. Try again!")



def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    query = "DELETE FROM matches"
    c.execute(query)
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    query = "DELETE FROM players"
    c.execute(query)
    DB.commit()
    DB.close()

def deleteScoreboard():
    """Remove all the scoreboard records from the database"""
    DB = connect()
    c= DB.cursor()
    query = "DELETE FROM scoreboard"
    c.execute(query)
    DB.commit()
    DB.close()

def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    query = "SELECT COUNT (*) FROM players"
    c.execute(query)
    return c.fetchone()[0]
    DB.close()


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    player = "INSERT INTO players (name) VALUES (%s) RETURNING id"
    scoreboard = "INSERT INTO scoreboard (player,score,matches) VALUES (%s,%s,%s)"
    c.execute(player, (name,))
    playerid = c.fetchone()[0]
    c.execute(scoreboard, (playerid,0,0))
    DB.commit()
    DB.close()


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
    DB = connect()
    c = DB.cursor()
	c.execute ()
    sql = """SELECT s.player, p.name, (SELECT COUNT(winner) AS numOfWins FROM matches WHERE winner = s.player), s.matches
	             FROM scoreboard AS s
                 INNER JOIN players AS p on p.id = s.player
                 ORDER BY numOfWins DESC"""
    c.execute(sql)
    playerRanks = []
    for row in c.fetchall():
        playerRanks.append(row)
    DB.close()
    return playerRanks


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    winningPoints = 2
    losingPoints = 0
    DB = connect()
    c = DB.cursor()
    sql = "INSERT INTO matches (winner, loser) VALUES (%s,%s)"
    winning = "UPDATE scoreboard SET score = score+%s, matches = matches+1 WHERE player = %s"
    losing = "UPDATE scoreboard SET score = score+%s, matches = matches+1 WHERE player = %s"
    c.execute(sql, (winner, loser))
    c.execute(winning, (winningPoints, winner))
    c.execute(losing, (losingPoints, loser))
    DB.commit()
    DB.close()

def isPairValid(p1, p2):
    """Checks if two players played against each other already
    Args:
        p1: the id of player to check
        p2: the id of potentially paired player
     Return true if pair is valid, else return false
    """
    DB = connect()
    c = DB.cursor()
    sql = """SELECT winner, loser
             FROM matches
             WHERE ((winner = %s AND loser = %s)
                    OR (winner = %s AND loser = %s))"""             
    c.execute(sql, (p1, p2, p2, p1))
    numOfMatches = c.rowcount
    DB.close()
    if numOfMatches > 0:
        return False
    return True

def validPairId(id1, id2, pStanding):
    """Checks if 2 players played against each other already
    If they did, find a valid match
    Args:
        id1: player needing match
        id2: potentially matched player
        pStanding: current ranking of players from swissPairings()
    Returns id of matched player. If none found, returns potential match as the best match
    """
    if id2 >= len(pStanding):
        return id1 + 1
    elif isPairValid(pStanding[id1][0], pStanding[id2][0]):
        return id2
    else:
        return validPairId(id1, (id2 + 1), pStanding)
 
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
    pStanding = playerStandings()
    pairsMatched = []

    numOfPlayers = countPlayers()
    if numOfPlayers%2 == 0:
    #checking for even & odd number of players
	#code for handling odd number of players not in place yet. So, just an error msg displayed for now
        while len(pStanding) > 1:
            rightMatch = validPairId(0, 1, pStanding)
            player1 = pStanding.pop(0)
            player2 = pStanding.pop(rightMatch - 1)
            pairsMatched.append((player1[0],player1[1],player2[0],player2[1]))
        return pairsMatched
    else:
        return "Number of players is odd"

