'''
Contains WaterField class
'''

from Domain.enums import Result

class WaterField:
    '''
    Provides WaterField characteristics
    '''
    def __init__(self, isHit):
        '''
        Constructor initializes a waterfield
        :param isHit: True if field was hit, False otherwise
        '''
        self._hit = isHit

    def getIcon(self):
        '''
        Returns icon to be displayed in console according to field's state
        :return: character corresponding to field's state
        '''
        if self._hit == True:
            return ' * '
        return ' - '

    def getShip(self):
        '''
        Function to be overriden in subclass
        :return:
        '''
        pass

    def getHit(self):
        '''
        Returns state of field
        :return: True if current field was hit, False otherwise
        '''
        return self._hit

    def shootAt(self):
        '''
        Hits current field
        :return: Result corresponding to field's state
        '''
        if self._hit == True:
            return Result.ALREADY_HIT
        self._hit = True
        return Result.NOT_HIT

