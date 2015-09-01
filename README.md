# Tournament-Results
Swiss pairing for tournament with even numbered player implemented using python and postgreSQL.

## Motivation
Cloned the code skeleton from github as provided by Udacity's Full Stack Nanodegree program and developed the code on virtual environment. I used VirtualBox to run the VM and configured it using Vagrant

## Installation
Requires Python and PsotgreSQL to be installed

## Usage
Execute the tournament_test.py file

## Tests
tournament_test.py contains a list of  unit tests to test functions that registers players, deletes table contents, counts number of registered players,
displays sorted winners scoreboard andgenerates pairs based on swiss pairing technique.

The list of unit tests for this project are-

if __name__ == '__main__':
    testDeleteMatches()
    testDelete()
    testCount()
    testRegister()
    testRegisterCountDelete()
    testStandingsBeforeMatches()
    testReportMatches()
    testPairings()
    print "Success!  All tests pass!"

## Credits
Udacity's Full Stack Nanodegree provided the code skeleton to implement this project

