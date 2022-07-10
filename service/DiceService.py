from random import randint


class DiceService:
    def __init__(self, dice):
        self.dice = dice

    def rollDice(self):
        face = randint(self.dice.start, self.dice.size)
        print('rolled', face)
        return face


