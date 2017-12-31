'''
Module which contains constants used in the program in order to make code more readable and easier to debug
'''
from enum import Enum, auto

class Ships(Enum):
    '''
    Contains size of each ship
    '''
    BATTLESHIP = 4
    CRUISER = 3
    DESTROYER = 2

class Result(Enum):
    '''
    Contains values for each ship / water state
    '''
    NOT_HIT = auto()
    ALREADY_HIT = auto()
    HIT = auto()
    DESTROYED = auto()

'''
Dictionary used in displaying information on the screen about whose ships were sank
'''
names = {
    1 : "Your",
    2 : "Enemy"
}

'''
Directions for adjacent squares
'''

dx = [ -1, 0, 1,  0]
dy = [  0, 1, 0, -1]


