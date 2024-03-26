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

        self.die = []
        while len(self.die) < 5:
            new_dice = Dice(self, len(self.die))
            new_dice.roll()
            self.die.append(new_dice)

    def run(self):
        """Start the main loop for the game"""
        self._show_introduction_screen()

        # intro screen here.
        while True:
            self._check_events()
            # if self.second_intro_complete:
            self._update_screen()
            self.clock.tick(60)

    def _show_introduction_screen(self):
        """Display the introduction screen"""
        intro_font = pygame.font.SysFont(None, 48)
        intro_text = intro_font.render("Press SPACE to Start", True, (0, 0, 0))
        second_intro_font = pygame.font.SysFont(None, 36)
        second_intro_text = second_intro_font.render("Welcome to the Yahtzee Game!", True, (0, 0, 0))
        second_intro_complete = False
        while not second_intro_complete:
            self.screen.fill((255, 255, 255))
            self.screen.blit(second_intro_text,
                             (self.screen.get_width() // 2 - second_intro_text.get_width() // 2,
                              self.screen.get_height() // 2 - second_intro_text.get_height() // 2))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        second_intro_complete = True

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
                # if mouse click is left mouse button
                if event.button == 1:
                    self._update_die(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            for die in self.die:
                if not die.is_held:
                    die.roll()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        pass

    def _update_die(self, event):
        # check mouse position
        pos = pygame.mouse.get_pos()
        for die in self.die:
            if die.x < event.pos[0] < die.x + die.width and die.y < event.pos[1] < die.y + die.height:
                die.hold()

        # Only one dice can be clicked at a time. We need to check what dice is clicked each click.
        # pos = event.pos

    #
    # # get a list of all sprites that are under the mouse cursor
    # clicked_sprites = [dice.hold() for dice in self.die if dice.rect.collidepoint(pos)]
    # clicked_sprites.clear()
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

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill('#FFFDD0')
        for dice in self.die:
            dice.draw_die()

        pygame.display.flip()


if __name__ == '__main__':
    main_game = DiceGUI()
    main_game.run()
