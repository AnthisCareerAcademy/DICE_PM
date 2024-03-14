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

        self.die = pygame.sprite.Group()
        self.intro_font = pygame.font.SysFont(None, 48)
        self.intro_text = self.intro_font.render("Press SPACE to Start", True, (0, 0, 0))
        self.second_intro_font = pygame.font.SysFont(None, 36)
        self.second_intro_text = self.second_intro_font.render("Welcome to the Yahtzee Game!", True, (0, 0, 0))
        self.second_intro_complete = False

    def run(self):
        """Start the main loop for the game"""
        self._show_introduction_screen()
        while True:
            self._check_events()
            if self.second_intro_complete:
                self._update_screen()
            self.clock.tick(60)

    def _show_introduction_screen(self):
        """Display the introduction screen"""
        while not self.second_intro_complete:
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.second_intro_text,
                             (self.screen.get_width() // 2 - self.second_intro_text.get_width() // 2,
                              self.screen.get_height() // 2 - self.second_intro_text.get_height() // 2))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.second_intro_complete = True

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self._update_die(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._next_die()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        pass

    def _update_die(self, event):
        # Only one dice can be clicked at a time. We need to check what dice is clicked each click.
        pos = event.pos

        # get a list of all sprites that are under the mouse cursor
        clicked_sprites = [dice.hold() for dice in self.die if dice.rect.collidepoint(pos)]
        clicked_sprites.clear()
        # do something with the clicked sprites...pos = pygame.mouse.get_pos()
        #
        #       # get a list of all sprites that are under the mouse cursor
        #       clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
        #       # do something with the clicked sprites...

        # print("Clicked!", pos)

        # get a list of all sprites that are under the mouse cursor
        # Find out what die is under the mouse cursor when clicked. Change held to 'true'
        # clicked_sprites = [s for s in self.die if s.rect.collidepoint(pos)]
        # print(clicked_sprites)

    def _next_die(self):
        """ Add new dice to die list. Sprite group """
        if len(self.die) < 6:
            new_die = Dice(self, len(self.die))
            new_die.roll()
            self.die.add(new_die)

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
