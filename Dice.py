from random import randint
from pygame.sprite import Sprite
import pygame


class Dice(Sprite):
    """ Dice class"""

    def __init__(self, main_game):
        """Initiate our dice"""
        self.mysprites = {
            0: 'sprites/dice-six-faces-none.bmp',
            1: 'sprites/dice-six-faces-one.bmp',
            2: 'sprites/dice-six-faces-two.bmp',
            3: 'sprites/dice-six-faces-three.bmp',
            4: 'sprites/dice-six-faces-four.bmp',
            5: 'sprites/dice-six-faces-five.bmp',
            6: 'sprites/dice-six-faces-six.bmp',
            'mixing': 'sprites/rolling-dice-cup.bmp',
            'throwing': 'sprites/cubes.bmp',
        }
        super().__init__()
        self.sides = 6
        self.is_held = False
        self.screen = main_game.screen
        self.screen_rect = main_game.screen.get_rect()

        # Load the dice image and get its rect.
        self.image = pygame.image.load(self.mysprites[0])
        self.rect = self.image.get_rect(center=self.screen.get_rect().center)
        self.rect.midleft = self.screen_rect.midleft

    def roll(self) -> int:
        """ Roll the dice and return its value """
        if not self.is_held:
            holder = randint(1, self.sides)
            self.image = pygame.image.load(self.mysprites[holder])
            self.image = pygame.transform.scale(self.image, (200, 200))
            return holder
        else:
            return False

    def hold(self):
        """ Hold the dice so it cannot be rolled"""
        self.is_held = not self.is_held

    def draw_die(self, givenx):
        """ Draw the dice at its current location """
        self.screen.blit(self.image, self.rect.move(givenx, 125))
