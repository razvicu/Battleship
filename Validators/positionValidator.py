'''
Contains validators for application
'''
from Domain.shipField import ShipField

def isPositionValid(self, board, shipSize, xDiff, yDiff, square):
    '''
    Function which checks if position is valid for a ship of shipSize to be placed at position square in orientation
    provided by xDiff and yDiff
    :param self: explicit self object
    :param board: Board object
    :param shipSize: the size of ship
    :param xDiff: 1 if ship is placed horizontally, 0 otherwise
    :param yDiff: 1 if ship is placed vertically, 0 otherwise
    :param square: Square object where we want to place ship
    :return: True if we can place the ship of shipSize at position square, False otherwise
    '''
    if (xDiff == 0 and yDiff == 0) or (xDiff == 1 and yDiff == 1):
        return False

    self._squareValidator.validate(square)

    if (isInside(square.getX(), square.getY() + shipSize - 1) == False and xDiff == 1 ) \
            or (isInside(square.getX() + shipSize - 1, square.getY()) == False and yDiff == 1 ):
        return False

    for i in range(shipSize):
        if isinstance(board[square.getX() + i * yDiff, square.getY() + i * xDiff], ShipField):
            return False

    return True

def isInside(x, y):
    '''
    Function which checks if coordinates are inside the board
    :param x: the line
    :param y: the column
    :return: True if coordinates are inside, False otherwise
    '''
    if x < 0 or x > 7 or y < 0 or y > 7:
        return False
    return True