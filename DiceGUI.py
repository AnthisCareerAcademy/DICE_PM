import pygame
import sys
from Dice import Dice
class DiceGUI:
    """ Overall class to manage game assets and behavior """

    def __init__(self):
        """ Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Dice GUI")

    def run(self):
        """Start the main loop for the game"""
        self.sequence()
        self._check_events()
        self._update_screen()
        self.clock.tick(60)
        pass
    def sequence(self):
        pass
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            # get a list of all sprites that are under the mouse cursor
            clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
            # do something with the clicked sprites...
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill('white')

        pygame.display.flip()


if __name__ == '__main__':
    main_game = DiceGUI()
    main_game.run()
