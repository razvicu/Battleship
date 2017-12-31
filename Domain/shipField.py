'''
Contains ShipField class
'''

from Domain.enums import Result
from Domain.waterField import WaterField

class ShipField(WaterField):
    '''
    Provides ShipField characteristics
    '''

    def __init__(self, ship, hidden = False):
        '''
        Constructor which initializes a shipfield
        :param ship: the Ship object contained in current field
        :param hidden: True if the board is human's, False otherwise
        '''
        self._ship = ship
        self._hidden = hidden
        self._hit = False

    def getIcon(self):
        '''
        Returns icon to be displayed in console according to ship's state
        :return: character corresponding to ship's state
        '''
        status = self._ship.getStatus()
        if status == Result.DESTROYED:
            return ' # '
        elif status == Result.NOT_HIT:
            if self._hidden == True:
                return ' - '
            else:
                return ' X '
        elif status == Result.HIT:
            if self._hit == True:
                return ' O '
            elif self._hidden == True:
                return ' - '
            else:
                return ' X '

    def shootAt(self):
        '''
        Hits current field
        :return: status of ship contained in current field
        '''
        if self._hit == True:
            return Result.ALREADY_HIT
        self._ship.hit()
        self._hit = True
        return self._ship.getStatus()

    def getShip(self):
        '''
        Returns Ship object contained in current field
        :return: Ship object
        '''
        return self._ship

    def getHit(self):
        '''
        Returns state of field
        :return: True if current field was hit, False otherwise
        '''
        return self._hit
