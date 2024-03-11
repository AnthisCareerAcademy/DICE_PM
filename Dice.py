from random import randint
import pygame


class Dice():
    """ Dice class"""

    def __init__(self, sides: int, main_game):
        """Initiate our dice"""
        self.mysprites = {
            0: 'sprites/dice-six-faces-none.png',
            1: 'sprites/dice-six-faces-one.png',
            2: 'sprites/dice-six-faces-two.png',
            3: 'sprites/dice-six-faces-three.png',
            4: 'sprites/dice-six-faces-four.png',
            5: 'sprites/dice-six-faces-five.png',
            6: 'sprites/dice-six-faces-six.png',
            'mixing': 'sprites/rolling-dice-cup.png',
            'throwing': 'sprites/cubes.png',
        }
        self.sides = sides
        self.is_held = False
        self.screen = main_game.screen
        self.settings = main_game.settings
        self.screen_rect = main_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load(self.mysprites[0])
        self.rect = self.image.get_rect()


    def roll(self) -> int:
        """ Roll the dice and return its value """
        if not self.is_held:
            holder = randint(1, self.sides)
            self.image = pygame.image.load(self.mysprites[holder])
            return holder
        else:
            return False

    def hold(self):
        """ Hold the dice so it cannot be rolled"""
        self.is_held = not self.is_held
