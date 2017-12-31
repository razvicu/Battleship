'''
Contains player class
'''

from Domain.board import Board

class Player:
    '''
    Provides player characteristics
    '''

    def __init__(self):
        '''
        Class constructor which initializes two boards (one for player's ships and other for player's hits) as well as
        the number of ships sank by player
        '''
        self._shipsBoard = Board()
        self._hitBoard = Board()
        self._shipsSank = 0

    def incrementShipsSank(self):
        '''
        Function which increases number of ships sank by player
        :return: None
        '''
        self._shipsSank += 1

    def getShipsBoard(self):
        '''
        Function which returns ships board
        :return: Board object
        '''
        return self._shipsBoard

    def getHitBoard(self):
        '''
        Function which returns hit board
        :return: Board object
        '''
        return self._hitBoard

    def getShipsSank(self):
        '''
        Function which returns number of ships sank
        :return: number of ships sank
        '''
        return self._shipsSank
