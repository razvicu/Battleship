'''
Contains Square class and SquareValidator class
'''

from Controller.exception import InvalidInputError
from Validators.positionValidator import isInside

class Square:
    '''
    Provides square characteristics
    '''

    def __init__(self, x, y):
        '''
        Constructor initalizes object with coordinates x and y
        :param x: the position on oX
        :param y: the position on oY
        '''
        self._x = x
        self._y = y

    def get(self):
        '''
        :return: Square object
        '''
        return self

    def getX(self):
        '''
        :return: x coordinate of current object
        '''
        return self._x

    def getY(self):
        '''
        :return: y coordinate of current object
        '''
        return self._y

    def setX(self, x):
        '''
        Sets x coordinate
        :param x: the x coordinate
        :return: None
        '''
        self._x = x

    def setY(self, y):
        '''
        Sets y coordinate
        :param y: the y coordinate
        :return: None
        '''
        self._y = y

class SquareValidator:
    '''
    Provides validator for Square object
    '''

    def validate(self, object):
        '''
        Checks if a Square object is valid
        :param object: the Square object to be checked
        :return: True if object is a valid Square object, False otherwise
        '''
        error = ""

        if isinstance(object, Square) == False:
            raise InvalidInputError("Not of type Square")

        if isInside(object.getX(), object.getY()) is False:
            error += "Indices out of range\n"

        if len(error) > 0:
            raise InvalidInputError(error)


