from Domain.player import Player
from Domain.square import SquareValidator
from Controller.shipController import ShipController
from UI.ui import UI

humanPlayer = Player()
computerPlayer = Player()
squareValidator = SquareValidator()

controller = ShipController(humanPlayer.getShipsBoard(), humanPlayer.getHitBoard(), squareValidator)

ui = UI(controller, humanPlayer, computerPlayer)
ui.start()