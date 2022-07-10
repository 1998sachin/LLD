from random import randint
from model.Dice import Dice

class DiceService:
    def __init__(self, size):
        self.dice = Dice(size)

    def rollDice(self):
        face = randint(self.dice.start, self.dice.size)
        print('rolled', face)
        return face


