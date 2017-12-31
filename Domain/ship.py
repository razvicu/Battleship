'''
Contains ship class
'''
from Domain.enums import Result

class Ship:
    '''
    Provides ship characteristics
    '''

    def __init__(self, size):
        '''
        Class constructor which initializes health of ship (initially equal to its size) and sets its sunk state to False
        :param size: the size of ship
        '''
        self._size = size
        self._health = size
        self._sunk = False

    def getHealth(self):
        '''
        Returns ship's health
        :return: health
        '''
        return self._health

    def getSize(self):
        '''
        Returns ship's size
        :return: size
        '''
        return self._size

    def getStatus(self):
        '''
        Returns ship's status
        :return: Result describing ship's state
        '''
        if self._sunk is True:
            return Result.DESTROYED
        elif self._health < self._size:
            return Result.HIT
        else:
            return Result.NOT_HIT

    def hit(self):
        '''
        A hit on ship means its health is decremented by one
        :return: None
        '''
        self._health -= 1
        if self._health == 0:
            self._sunk = True
