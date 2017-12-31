'''
Module contains controller for the application
'''

from Domain.shipField import ShipField
from Domain.square import Square
from Domain.ship import Ship
from Domain.enums import Ships, Result, dx, dy
from Validators.positionValidator import isPositionValid, isInside
import random

class ShipController:

    def __init__(self, shipsBoard, hitBoard, squareValidator):
        '''
        Constructor of controller class
        :param shipsBoard: the board containing human's player ships
        :param hitBoard: the board containing human's player shots
        :param squareValidator: validator for objects of type Square
        '''
        self._shipsBoard = shipsBoard
        self._hitBoard = hitBoard
        self._squareValidator = squareValidator
        self._hitStack = []

    def placeShip(self, ship, board, orientation, square):
        '''
        Function which places a ship on the board
        :param ship: the Ship object to be placed on board
        :param board: the Board object which contains ships
        :param orientation: either horizontal or vertical
        :param square: the Square object where the bow of ship is to be placed
        :return: True if ship was placed successfully, False otherwise
        '''
        xDiff, yDiff = 0, 0
        if orientation in ["H", "h"]:
            xDiff = 1
        elif orientation in ["V", "v"]:
            yDiff = 1
        else:
            return False
        isValid = isPositionValid(self, self._shipsBoard, ship.getSize(), xDiff, yDiff, square)
        if isValid == True:
            for i in range(ship.getSize()):
                board[square.getX() + i * yDiff, square.getY() + i * xDiff] = ShipField(ship)
            return True

        return False

    def placeAIShips(self):
        '''
        Function which places Computer's ship on board
        :return: None
        '''
        xDiff, yDiff = self.generateOrientation()

        ships = [Ship(Ships.BATTLESHIP.value), Ship(Ships.CRUISER.value), Ship(Ships.DESTROYER.value)]

        for ship in ships:

            square = self.generateSquare()

            while isPositionValid(self, self._hitBoard, ship.getSize(), xDiff, yDiff, square) == False:
                square = self.generateSquare()

            for i in range(ship.getSize()):
                self._hitBoard[square.getX() + i * yDiff, square.getY() + i * xDiff] = ShipField(ship, True)

    def generateSquare(self):
        '''
        Function which generates a valid Square object
        :return: Square object generated
        '''
        x, y = -1, -1

        while isInside(x, y) is False:
            x = random.randint(0, 7)
            y = random.randint(0, 7)

        square = Square(x, y)
        return square

    def generateOrientation(self):
        '''
        Function which generates a valid orientation
        :return: tuple consisting of direction for the ship
        '''
        xDiff, yDiff = 0, 0
        xDiff = random.getrandbits(1)
        if xDiff == 0:
            yDiff = 1
        return xDiff, yDiff

    def fireAt(self, square, board, ai = False):
        '''
        Function which shoots at a specific coordinate
        :param square: the Square object to be shot at
        :param board: the Board object where square is
        :param ai: True if AI fires, False otherwise
        :return: tuple containing state (HIT, DESTROYED etc) and the Ship object at square coordinates
        '''
        self._squareValidator.validate(square)
        state = board[square.getX(), square.getY()].shootAt()
        if ai is True:
            if state == Result.HIT:
                for i in range(4):
                    if isInside(square.getX() + dx[i], square.getY() + dy[i]):
                        self._hitStack.append((square.getX() + dx[i], square.getY() + dy[i]))
        return state , board[square.getX(), square.getY()].getShip()

    def aiFire(self):
        '''
        Function which shoots at a random generated coordinate
        :return: call to fireAt() function
        '''
        if not self._hitStack:
            square = self.generateSquare()
        else:
            coords = self._hitStack.pop()
            square = Square(coords[0], coords[1])
        return self.fireAt(square, self._shipsBoard, True)

    def getShipsBoard(self):
        '''
        Function which returns human's player ships
        :return: Board object
        '''
        return self._shipsBoard

    def getHitBoard(self):
        '''
        Function which returns human's player shots
        :return: Board object
        '''
        return self._hitBoard


