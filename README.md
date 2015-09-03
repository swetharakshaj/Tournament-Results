# Tournament-Results
Swiss pairing for tournament with even numbered player implemented using python and postgreSQL.

## Motivation
Cloned the code skeleton from github as provided by Udacity's Full Stack Nanodegree program and developed the code on virtual environment. I used VirtualBox to run the VM and configured it using Vagrant

## Installation
Requires Python and PsotgreSQL to be installed

## Usage
To execute the project follow these steps in order.

Clone the repository to a local machine.
In the commandline, navigate to the cloned reporsitory folder. 
To build and access the database we run 'psql' followed by '\i tournament.sql'. 
To run the series of tests defined in test suite, run the tournament_test program from the command line using the command 'python tournament_test.py'.


## Tests
tournament_test.py contains a list of  unit tests to test functions that registers players, deletes table contents, counts number of registered players, displays sorted winners scoreboard and generates pairs based on swiss pairing technique.

## Credits
Udacity's Full Stack Nanodegree provided the code skeleton to implement this project

