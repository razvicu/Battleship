'''
Module contains board class, which is the game interface
'''

from Domain.waterField import WaterField

class Board:
    '''
    Provides game field
    '''

    def __init__(self):
        '''
        Constructor takes no arguments but initializes a 8x8 board, each cell being a WaterField object
        and stores the coordinates string to be displayed alongside the board on the screen
        '''
        self._board = [[ WaterField(False) for i in range(8) ] for j in range(8)]
        self._coords = "     A     B     C     D     E     F     G     H "

    def __str__(self):
        '''
        Overrides str method
        Used to print game interface in console
        :return: empty string
        '''
        print(self._coords)
        for i in range(len(self._board)):
            print(i + 1, end = ' ')
            for j in range(len(self._board)):
                print ("  " + self._board[i][j].getIcon(), end = ' ')
            print('\n')
        return ""

    def __setitem__(self, key, value):
        '''
        Overrides setitem method
        :param key: a tuple consisting of coordinates of game field object
        :param value: the value to be assigned to the game field
        :return: None
        '''
        i, j = key
        self._board[i][j] = value

    def __getitem__(self, item):
        '''
        Overrides getitem method
        :param item: a tuple consisting of coordinates of game field object
        :return: object at coordinates item, either a waterField or a shipField
        '''
        i, j = item
        return self._board[i][j]