import sys
import pygame
from Settings import Settings
from Ship import Ship


class AlienInvasion:

    def __init__(self):
        # Pygame init
        pygame.init()

        # Screen init
        self.screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))
        self.clock = pygame.time.Clock()
        fav_icon = pygame.image.load(Settings.fav_icon_path)
        pygame.display.set_caption(Settings.caption)
        pygame.display.set_icon(fav_icon)

        #   Ship init
        self.ship = Ship(self)
        self.ship_moving_right = False

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.is_moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.is_moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.is_moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.is_moving_left = False

    def _update_screen(self):
        self.screen.fill(Settings.bg_color)
        self.ship.update()
        self.ship.draw()

        pygame.display.flip()
