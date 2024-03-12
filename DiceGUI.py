import pygame
import sys

from pygame import Color

from Dice import Dice


class DiceGUI:
    """ Overall class to manage game assets and behavior """

    def __init__(self):
        """ Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Dice GUI")

        self.die = pygame.sprite.Group()

    def run(self):
        """Start the main loop for the game"""
        while True:
            # self.sequence()
            self._check_events()
            #self._update_die()
            self._update_screen()
            self.clock.tick(60)

    def sequence(self):
        # rolling dice cup move the cup diagonally side to side (Roll function)
        for dice in self.die:
            print(dice.roll())
            if input("Hold?") == 'y':
                dice.hold()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print("down event")
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                print("up event")
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Mouse up")
                pos = pygame.mouse.get_pos()

                # get a list of all sprites that are under the mouse cursor
                # Find out what die is under the mouse cursur when clicked. Change held to 'true'
                # clicked_sprites = [s for s in self.die if s.rect.collidepoint(pos)]
                # print(clicked_sprites)


    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._next_die()

    def _next_die(self):
        """ Add new dice to die list. Sprite group """
        if len(self.die) < 6:
            new_die = Dice(self)
            new_die.roll()
            self.die.add(new_die)

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        pass


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill('#FFFDD0')
        offby = 0
        for dice in self.die.sprites():
            dice.draw_die(offby)
            offby += 273

        pygame.display.flip()


if __name__ == '__main__':
    main_game = DiceGUI()
    main_game.run()
