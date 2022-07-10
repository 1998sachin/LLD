import random


class Dice:
    start = 1
    againFace = 6

    def __init__(self, size):
        if size < 1 or size < self.againFace:
            raise Exception('Dice size should be greater than', max(self.size, self.againFace))
        self.size = size
