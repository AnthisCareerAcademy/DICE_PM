from random import randint


class Dice:
    """ Dice class"""

    def __init__(self, sides: int = 6):
        """Initiate our dice"""
        self.sides = sides
        self.is_held = False

    def roll(self) -> int:
        """ Roll the dice and return its value """
        if not self.is_held:
            return randint(1, self.sides + 1)
        else:
            return False

    def hold(self):
        """ Hold the dice so it cannot be rolled"""
        self.is_held = not self.is_held
