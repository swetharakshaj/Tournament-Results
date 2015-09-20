# Tournament-Results
Swiss pairing for tournament with even numbered player implemented using python and postgreSQL.

## Motivation
Cloned the code skeleton from github as provided by Udacity's Full Stack Nanodegree program and developed the code on virtual environment. I used VirtualBox to run the VM and configured it using Vagrant

## Installation
Requires Python and PsotgreSQL to be installed

## Tests
tournament_test.py contains a list of  unit tests to test functions that registers players, deletes table contents, counts number of registered players, displays sorted winners scoreboard and generates pairs based on swiss pairing technique.

## Usage
To execute the project follow these steps in order.

1. Clone the repository to a local machine.
2. In the commandline, navigate to the cloned reporsitory folder. 
3. Setting up the database can be done in 2 ways
Way 1 -Refer to tournament.sql and execute the commands in the file on Git Bash. For example..
      vagrant@trusty32: vagrant => CREATE DATABASE tournament;
      vagrant@trusty32: vagrant => \c tournament;
      vagrant@trusty32: tournament =>
  Once we have created a database, we can add the tables that we will be working with as in the "CREATE TABLE" commans in      tournament.sql file.
Way 2 - Since we have all the commands tournament.sql file already, we could execute by running run
vagrant@trusty32: psql => \i tournament.sql
4. To run the series of tests defined in test suite, run the tournament_test program from the command line using the command 'python tournament_test.py'.

## Credits
Udacity's Full Stack Nanodegree provided the code skeleton to implement this project

