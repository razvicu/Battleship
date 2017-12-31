'''
Module contains error class
'''


class InvalidInputError(Exception):
    '''
    Custom error to be raised when it occurs during execution of the program
    '''
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message