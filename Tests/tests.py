import unittest

from Controller.shipController import ShipController
from Controller.exception import InvalidInputError
from Domain.player import Player
from Domain.square import Square
from Domain.ship import Ship
from Domain.enums import Ships, Result
from Domain.square import SquareValidator
from Validators.positionValidator import isInside, isPositionValid
from Domain.shipField import ShipField
from Domain.board import Board


class Test(unittest.TestCase):
    def setUp(self):
        self._player1 = Player()
        self._player2 = Player()
        self._squareValidator = SquareValidator()
        self._controller = ShipController(self._player1.getShipsBoard(), self._player1.getHitBoard(), self._squareValidator)
        self._battleShip = Ship(Ships.BATTLESHIP.value)
        self._cruiser = Ship(Ships.CRUISER.value)
        self._destroyer = Ship(Ships.DESTROYER.value)
        self._square1 = Square(1,3)
        self._square2 = Square(3,5)
        self._square3 = Square(-1, 6)
        self._square4 = Square(7,7)

class TestBoardandPlayer(Test):
    def setUp(self):
        super().setUp()

    def testBoard(self):
        board = Board()
        board._board[2][3] = 3
        self.assertEqual(board[2, 3], 3)
        board[2, 7] = 9
        self.assertEqual(board[2, 7], 9)

    def testPlayer(self):
        self._player1.incrementShipsSank()
        self.assertEqual(self._player1.getShipsSank(), 1)

        self.assertEqual(self._player1.getHitBoard(), self._player1._hitBoard)
        self.assertEqual(self._player1.getShipsBoard(), self._player1._shipsBoard)

class TestShip(Test):
    def setUp(self):
        super().setUp()

    def testHit(self):
        self.assertEqual(self._destroyer.getStatus(), Result.NOT_HIT)

        self._destroyer.hit()

        self.assertEqual(self._destroyer.getHealth(), 1)
        self.assertEqual(self._destroyer.getStatus(), Result.HIT)

        self._destroyer.hit()

        self.assertEqual(self._destroyer.getHealth(), 0)
        self.assertEqual(self._destroyer.getStatus(), Result.DESTROYED)

    def testGetHealth(self):
        self.assertEqual(self._destroyer.getHealth(), 2)
        self._destroyer.hit()
        self.assertEqual(self._destroyer.getHealth(), 1)

        self.assertEqual(self._cruiser.getHealth(), 3)
        self.assertEqual(self._battleShip.getHealth(), 4)

    def testGetStatus(self):
        self._cruiser.hit()
        self.assertEqual(self._cruiser.getStatus(), Result.HIT)
        self._cruiser.hit()
        self._cruiser.hit()
        self._cruiser.hit()
        self.assertEqual(self._cruiser.getStatus(), Result.DESTROYED)
        self.assertEqual(self._cruiser.getHealth(), -1)

    def testGetSize(self):
        self.assertEqual(self._cruiser.getSize(), 3)
        self.assertNotEqual(self._destroyer.getSize(), 10)

class TestShipField(Test):
    def setUp(self):
        super().setUp()


class TestController(Test):
    def setUp(self):
        super().setUp()

    def testPlaceShip(self):
        self.assertTrue(self._controller.placeShip(self._battleShip, self._player1.getShipsBoard(), "h", self._square1))
        self.assertTrue(self._controller.placeShip(self._destroyer, self._player1.getShipsBoard(), "v", self._square2))
        self.assertFalse(self._controller.placeShip(self._cruiser, self._player1.getShipsBoard(), "h", self._square2))
        self.assertFalse(self._controller.placeShip(self._cruiser, self._player1.getShipsBoard(), "s", self._square4))
        with self.assertRaises(InvalidInputError):
            self._controller.placeShip(self._battleShip, self._player1.getShipsBoard(), "h", self._square3)

    def testPlaceAiShips(self):
        for k in range(100):
            self.setUp()
            self._controller.placeAIShips()
            board = self._player1.getHitBoard()
            count = 0
            for i in range(8):
                for j in range(8):
                    if isinstance(board[i, j], ShipField):
                        count += 1
            self.assertEqual(count, 9)

    def testAiFire(self):
        board = self._player1.getShipsBoard()
        count, prev = 0, 0
        for k in range(64):
            count = 0
            res = self._controller.aiFire()

            while res[0] == Result.ALREADY_HIT:
                res = self._controller.aiFire()
            for i in range(8):
                for j in range(8):
                    if board[i, j].getHit():
                        count += 1
            self.assertEqual(count, prev + 1)
            prev = count

    def testGenerateSquare(self):
        square = self._controller.generateSquare()
        square2 = self._controller.generateSquare()
        self.assertFalse(square is square2)
        self._squareValidator.validate(square)
        self.assertTrue(isInside(square.getX(), square.getY()))
        self.assertTrue(isInside(square2.getX(), square2.getY()))

    def testGenerateOrientation(self):
        x1, y1 = self._controller.generateOrientation()
        x2, y2 = self._controller.generateOrientation()
        self.assertEqual(x1 + y1, 1)
        self.assertEqual(x2 + y2, 1)

    def testFireAt(self):
        self._controller.placeShip(self._battleShip, self._player1.getShipsBoard(), "h", self._square1)
        self.assertEqual(self._controller.fireAt(self._square1, self._player1.getShipsBoard()),
                         (Result.HIT, self._battleShip))
        square2 = Square(self._square1.getX(), self._square1.getY() + 1)
        self.assertEqual(self._controller.fireAt(square2, self._player1.getShipsBoard()),
                         (Result.HIT, self._battleShip))
        square3 = Square(square2.getX(), square2.getY() + 1)
        self.assertEqual(self._controller.fireAt(square3, self._player1.getShipsBoard()),
                         (Result.HIT, self._battleShip))
        square4 = Square(square3.getX(), square3.getY() + 1)
        self.assertEqual(self._controller.fireAt(square4, self._player1.getShipsBoard()),
                         (Result.DESTROYED, self._battleShip))

        self.assertEqual(self._controller.fireAt(Square(2,2), self._player1.getShipsBoard()),
                         (Result.NOT_HIT, None))
        self.assertEqual(self._controller.fireAt(Square(2, 2), self._player1.getShipsBoard()),
                         (Result.ALREADY_HIT, None))

    def testGetShipsBoard(self):
        self.assertEqual(self._controller.getShipsBoard(), self._player1.getShipsBoard())

    def testGetHitBoard(self):
        self.assertEqual(self._controller.getHitBoard(), self._player1.getHitBoard())

class TestValidators(Test):

    def setUp(self):
        super().setUp()

    def testIsInside(self):
        self.assertTrue(isInside(2, 3))
        self.assertTrue(isInside(self._square1.getX(), self._square1.getY()))
        self.assertFalse(isInside(-1, -1))
        self.assertFalse(isInside(-1, 2))
        self.assertFalse(isInside(8, 7))
        self.assertFalse(isInside(7, -2))
        self.assertFalse(isInside(self._square3.getX(), self._square3.getY()))

    def testIsPositionValid(self):
        self.assertTrue(isPositionValid(self, self._player1.getHitBoard(), 3, 1, 0, self._square1))
        self.assertFalse(isPositionValid(self, self._player1.getHitBoard(), 3, 1, 1, self._square1))
        self.assertFalse(isPositionValid(self, self._player1.getHitBoard(), 2, 0, 1, self._square4))
        self.assertFalse(isPositionValid(self, self._player1.getHitBoard(), 3, 1, 0, Square(1,7)))
        with self.assertRaises(InvalidInputError):
            isPositionValid(self, self._player1.getHitBoard(), 3, 1, 0, self._square3)

if __name__ == "__main__":
    unittest.main()

