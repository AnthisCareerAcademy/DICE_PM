from random import randint
from pygame.sprite import Sprite
import pygame


class Dice(Sprite):
    """ Dice class"""

    def __init__(self, main_game, id):
        """Initiate our dice"""
        self.mysprites = {
            0: 'sprites/dice0.bmp',
            1: 'sprites/dice1.bmp',
            2: 'sprites/dice2.bmp',
            3: 'sprites/dice3.bmp',
            4: 'sprites/dice4.bmp',
            5: 'sprites/dice5.bmp',
            6: 'sprites/dice6.bmp',
            'mixing': 'sprites/rolling-dice-cup.bmp',
            'throwing': 'sprites/cubes.bmp',
        }
        super().__init__()
        self.sides = 6
        self.id = id
        self.is_held = False
        self.screen = main_game.screen
        self.screen_rect = main_game.screen.get_rect()

        # Load the dice image and get its rect.
        self.image = pygame.image.load(self.mysprites[0])
        self.rect = self.image.get_rect(center=self.screen.get_rect().center)
        self.rect.midleft = self.screen_rect.midleft
        self.x = self.rect.x
        self.y = self.rect.y
        self.width = self.rect.width
        self.height = self.rect.height

    def roll(self):
        """ Roll the dice and return its value """
        if not self.is_held:
            holder = randint(1, self.sides)
            self.image = pygame.image.load(self.mysprites[holder])

    def hold(self):
        """ Hold the dice so it cannot be rolled"""
        self.is_held = not self.is_held

    def draw_die(self):
        """ Draw the dice at its current location """
        self.x = self.id * 300 + 50
        self.y = 125

        amt = 20
        # Highlight dice that are held (FEATURE)
        if self.is_held:
            pygame.draw.rect(self.screen, (151, 74, 181), (self.x - amt/2, self.y - amt/2, self.width + amt, self.height + amt), 10)
        self.screen.blit(self.image, (self.x, self.y))
