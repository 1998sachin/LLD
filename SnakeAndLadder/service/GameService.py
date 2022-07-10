class GameService:

    def __init__(self, players, boardService, diceService):
        self.players = players
        self.boardService = boardService
        self.diceService = diceService
        self.gameEnded = False
        self.playerTurnIndex = 0
        self.playersFinished = 0

    def getNextPlayer(self):
        if self.gameEnded:
            raise Exception('Game has Ended. No next player')

        while True:
            self.playerTurnIndex += 1
            self.playerTurnIndex %= len(self.players)
            if self.players[self.playerTurnIndex].hasWon:
                continue
            else:
                return self.players[self.playerTurnIndex]

        raise Exception('No next player found. Gamed Ended')

    def setPlayerStateForWin(self, player):
        if self.boardService.isAtTheEnd(player.currentPosition):
            player.hasWon = True
            self.playersFinished += 1
            print(player.name, 'has reached the end and won')

    def move(self, moveCount, player):
        curPos = player.currentPosition
        newPos = curPos + moveCount
        if self.boardService.isOutsideBoard(newPos):
            print(player.name, 'will move outside board hence move rejected')
        elif self.boardService.isSnakePresent(newPos):
            player.currentPosition = self.boardService.getSnakeTail(curPos + moveCount)
            print(player.name, 'got bitten by snake at', newPos, 'Moving back')
        elif self.boardService.isLadderPresent(newPos):
            player.currentPosition = self.boardService.getLadderEnd(newPos)
            print(player.name, 'found a ladder at', newPos, 'moving up')
        else:
            player.currentPosition = newPos

        print(player.name, 'moved from', curPos, 'to', player.currentPosition)

    def getMoves(self):
        return self.diceService.rollDice()

    def play(self):
        while not self.gameEnded:
            p = self.getNextPlayer()
            print('')
            print(p.name, 'rolling --------------->')
            moves = self.getMoves()
            self.move(moves, p)
            self.setPlayerStateForWin(p)
            if self.playersFinished == len(self.players):
                self.gameEnded = True

        print('\n\nGame Ended')
