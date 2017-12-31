from Domain.enums import Ships
from Domain.square import Square
from Domain.ship import Ship
from Domain.enums import Result
from Domain.enums import names


class UI:

    def __init__(self, controller, humanPlayer, computerPlayer):
        self._controller = controller
        self._humanPlayer = humanPlayer
        self._computerPlayer = computerPlayer

    @staticmethod
    def displayInitialMessage():
        print("You have to place a battleship, a cruiser and a destroyer on the board")
        print("You will be asked to provide direction (H for horizontally and V for vertically) "
              "and coordinates for each ship in the format LC "
              "where L is the line (1-8) and C is the column (A-H)")

    def displayBattleShipMessage(self):
        orientation = input("Enter direction for the battleship (H/V): ")
        while orientation not in ["H", "V", "h", "v"]:
            print("Orientation must be 'H' / 'h' for horizontal or 'V' / 'v' for vertical!")
            orientation = input("Enter direction for the battleship (H/V): ")

        line, column = -1, -1

        while (line in range(8)) == False or (column in range(8)) == False:
            coords = input("Enter coordinates: ")
            if len(coords) < 2:
                continue
            line = ord(coords[0]) - 49
            column = ord(coords[1].upper()) - 65

        ship = Ship(Ships.BATTLESHIP.value)
        if self._controller.placeShip(ship, self._controller.getShipsBoard(), orientation, Square(line, column)) == True:
            print("Battleship placed successfully")
        else:
            print("Could not place battleship")
            self.displayBattleShipMessage()

    def displayCruiserMessage(self):
        orientation = input("Enter direction for the cruiser (H/V): ")
        while orientation not in ["H", "V", "h", "v"]:
            print("Orientation must be 'H' / 'h' for horizontal or 'V' / 'v' for vertical!")
            orientation = input("Enter direction for the cruiser (H/V): ")

        line, column = -1, -1

        while (line in range(8)) == False or (column in range(8)) == False:
            coords = input("Enter coordinates: ")
            if len(coords) < 2:
                continue
            line = ord(coords[0]) - 49
            column = ord(coords[1].upper()) - 65


        ship = Ship(Ships.CRUISER.value)
        if self._controller.placeShip(ship, self._controller.getShipsBoard(), orientation, Square(line, column)) == True:
            print("Cruiser placed successfully")
        else:
            print("Could not place cruiser")
            self.displayCruiserMessage()

    def displayDestroyerMessage(self):
        orientation = input("Enter direction for the destroyer (H/V): ")
        while orientation not in ["H", "V", "h", "v"]:
            print("Orientation must be 'H' / 'h' for horizontal or 'V' / 'v' for vertical!")
            orientation = input("Enter direction for the destroyer (H/V): ")

        line, column = -1, -1

        while (line in range(8)) == False or (column in range(8)) == False:
            coords = input("Enter coordinates: ")
            if len(coords) < 2:
                continue
            line = ord(coords[0]) - 49
            column = ord(coords[1].upper()) - 65

        ship = Ship(Ships.DESTROYER.value)
        if self._controller.placeShip(ship, self._controller.getShipsBoard(), orientation, Square(line, column)) == True:
            print("Destroyer placed successfully")
        else:
            print("Could not place destroyer")
            self.displayDestroyerMessage()

    def askCoordinates(self):
        line, column = -1, -1

        while (line in range(8)) == False or (column in range(8)) == False:
            coords = input("Shoot at: ")
            if len(coords) < 2:
                continue
            line = ord(coords[0]) - 49
            column = ord(coords[1].upper()) - 65

        return self._controller.fireAt(Square(line, column), self._controller.getHitBoard())

    def displayShipsBoard(self):
        print("Your ships: ")
        print(self._controller.getShipsBoard())

    def displayHitBoard(self):
        print("Your shots: ")
        print(self._controller.getHitBoard())

    def printMessage(self, res, player):
        if res[0] == Result.NOT_HIT:
            print("Miss")
        elif res[0] == Result.HIT:
            print("Hit")
        elif res[0] == Result.DESTROYED:
            print("{} {} has been sunk".format(names[player], Ships(res[1].getSize()).name))


    def start(self):


        self.displayInitialMessage()
        self.displayBattleShipMessage()
        self.displayShipsBoard()
        self.displayCruiserMessage()
        self.displayShipsBoard()
        self.displayDestroyerMessage()
        self.displayShipsBoard()
        self._controller.placeAIShips()


        gameWon = False

        while not gameWon:

            res = self.askCoordinates()

            while res[0] == Result.ALREADY_HIT:
                print("Position already hit. Enter another one")
                res = self.askCoordinates()

            self.printMessage(res, 2)

            res = res[0]

            if res == Result.DESTROYED:
                self._humanPlayer.incrementShipsSank()
                if self._humanPlayer.getShipsSank() == 3:
                    gameWon = True
                    self.displayHitBoard()
                    print("Congratulations! You won the game!")
                    continue

            self.displayHitBoard()

            res = self._controller.aiFire()

            while res[0] == Result.ALREADY_HIT:
                res = self._controller.aiFire()

            self.printMessage(res, 1)

            res = res[0]

            if res == Result.DESTROYED:
                self._computerPlayer.incrementShipsSank()
                if self._computerPlayer.getShipsSank() == 3:
                    gameWon = True
                    self.displayShipsBoard()
                    print("Defeat! Computer won!")
                    continue

            self.displayShipsBoard()
