import pygame
import sys
from Dice import Dice


class DiceGUI:
    """ Overall class to manage game assets and behavior """

    def __init__(self):
        """ Initialize the game and create game resources. """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Dice GUI")
        self.font = pygame.font.SysFont(None, 36)
        self.rolls_left = 0

        self.rules = "These are suppost to be the rules. "

        self.die = []
        while len(self.die) < 5:
            new_dice = Dice(self, len(self.die))
            new_dice.roll()
            self.die.append(new_dice)

    def run(self):
        """ Start the main loop for the game """

        self._show_introduction_screen()
        self._show_rules_screen()

        while True:
            self._check_events()
            # if self.second_intro_complete:
            self._update_screen()
            self.clock.tick(60)

    def _check_quit(self, given_event):
        """ Check if event type is quitting. """
        if given_event.type == pygame.QUIT or given_event.type == pygame.KEYDOWN and given_event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

    def _show_introduction_screen(self):
        """ Display the introduction screen """
        # intro_font = pygame.font.SysFont(None, 48)
        # intro_text = intro_font.render("Press SPACE to Start", True, (0, 0, 0))
        second_intro_text = self.font.render("Welcome to the Yahtzee Game!", True, (0, 0, 0))
        space_tapped = False
        while not space_tapped:
            self.screen.fill((255, 255, 255))
            self.screen.blit(second_intro_text,
                             (self.screen.get_width() // 2 - second_intro_text.get_width() // 2,
                              self.screen.get_height() // 2 - second_intro_text.get_height() // 2))
            pygame.display.flip()
            for event in pygame.event.get():
                self._check_quit(event)

                # Replace this break with a button. Will break when button is pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        space_tapped = True

    def _show_rules_screen(self):
        """ Display rules """

        rules_text = self.font.render(self.rules, True, (0, 0, 0))
        space_tapped = False
        while not space_tapped:
            self.screen.fill((255, 255, 255))
            self.screen.blit(rules_text,
                             (self.screen.get_width() // 2 - rules_text.get_width() // 2,
                              self.screen.get_height() // 2 - rules_text.get_height() // 2))
            pygame.display.flip()
            for event in pygame.event.get():
                self._check_quit(event)

                # Replace this break with a button. Will break when button is pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        space_tapped = True
        pass

    def _check_events(self):
        """ Respond to key presses and mouse events. """
        for event in pygame.event.get():
            self._check_quit(event)
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                # if mouse click is left mouse button
                if event.button == 1:
                    self._update_die(event)

    def _check_keydown_events(self, event):
        """ Respond to key presses. """
        if event.key == pygame.K_SPACE:
            for die in self.die:
                if not die.is_held:
                    die.roll()

    def _check_keyup_events(self, event):
        """ Respond to key releases. """
        pass

    def _update_die(self, event):
        # check mouse position
        for die in self.die:
            if die.x < event.pos[0] < die.x + die.width and die.y < event.pos[1] < die.y + die.height:
                die.hold()

    def _render_text(self):
        """ Update screen text """
        self.screen.fill('#FFFDD0')
        rolls_left_text = self.font.render(f"Your rolls left: {self.rolls_left}", True, (0, 0, 0))
        self.screen.blit(rolls_left_text, (self.screen.get_width() - 250, 10))

    def _update_screen(self):
        """ Update images on the screen, and flip to the new screen. """
        self._render_text()

        for dice in self.die:
            dice.draw_die()
        pygame.display.flip()


if __name__ == '__main__':
    main_game = DiceGUI()
    main_game.run()
