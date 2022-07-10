from model.Board import Board

class BoardService:

    def __init__(self, boardSize, snakes, ladders):
        self.board = Board(boardSize)
        self.pBoard = self.board.pBoard
        self.snakeKey = self.board.snakeKey
        self.ladderKey = self.board.ladderKey
        self.startPosition = self.board.start
        self.endPosition = self.board.end
        self.snakes = snakes
        self.ladders = ladders

    def setBoard(self):
        self.setSnakes()
        self.setLadders()

    def setSnakes(self):
        for snake in self.snakes:
            head = snake.head
            tail = snake.tail
            self.pBoard[head][self.snakeKey] = tail

    def isSnakePresent(self, position):
        return self.snakeKey in self.pBoard[position]

    def getSnakeTail(self, position):
        if self.isSnakePresent(position):
            return self.pBoard[position][self.snakeKey]
        else:
            raise Exception('Snake not present at position ' + str(position))

    def setLadders(self):
        for ladder in self.ladders:
            start = ladder.start
            end = ladder.end
            self.pBoard[start][self.ladderKey] = end

    def isLadderPresent(self, position):
        return self.ladderKey in self.pBoard[position]

    def getLadderEnd(self, position):
        if self.isLadderPresent(position):
            return self.pBoard[position][self.ladderKey]
        else:
            raise Exception('Ladder not present at position ' + str(position))

    def isOutsideBoard(self, position):
        return position > self.endPosition

    def isAtTheEnd(self, position):
        return position == self.endPosition

    def getEndPositoin(self):
        return self.endPosition
