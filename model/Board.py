class Board:
    start = 1
    end = None
    positionKey = 'p'
    snakeKey = 's'
    ladderKey = 'l'

    def __init__(self, size):
        self.pBoard = {}
        self.end = size - self.start + 1
        for i in range(self.start, self.end + 1):
            self.pBoard[i] = {self.positionKey: i}
