# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from sys import stdin
from SnakeAndLadder.model.Snake import Snake
from SnakeAndLadder.model.Ladder import Ladder
from SnakeAndLadder.model.Board import Board
from SnakeAndLadder.model.Dice import Dice
from SnakeAndLadder.model.Player import Player

from SnakeAndLadder.service.BoardService import BoardService
from SnakeAndLadder.service.DiceService import DiceService
from SnakeAndLadder.service.GameService import GameService

BOARD_SIZE = 100
DICE_SIZE = 6
if __name__ == '__main__':
    snakesCount = int(stdin.readline().strip())
    snakes = []
    for i in range(snakesCount):
        head, tail = list(map(int, stdin.readline().split()))
        s = Snake(head, tail)
        snakes.append(s)

    laddersCount = int(stdin.readline().strip())
    ladders = []
    for i in range(laddersCount):
        start, end = list(map(int, stdin.readline().split()))
        s = Ladder(start, end)
        ladders.append(s)

    playersCount = int(stdin.readline().strip())
    players = []
    for i in range(playersCount):
        name = stdin.readline().split()
        s = Player(name)
        players.append(s)

    board = Board(BOARD_SIZE)
    boardService = BoardService(board, snakes, ladders)
    boardService.setBoard()

    dice = Dice(DICE_SIZE)
    diceService = DiceService(dice)

    gameService = GameService(players, boardService, diceService)

    gameService.play()


