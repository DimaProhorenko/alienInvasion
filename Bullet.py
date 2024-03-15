import pygame
from pygame.sprite import Sprite
from Settings import Settings


class Bullet(Sprite):

    def __init__(self, screen, ship_postion):
        super().__init__()
        self.screen = screen
        self.ship_position = ship_postion
        self.rect = pygame.Rect(0, 0, Settings.bullet_width, Settings.bullet_height)
        self.rect.midtop = ship_postion
        self.y = float(self.rect.y)

    def update(self):
        self.y -= Settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, Settings.bullet_color, self.rect)

    def is_bullet_off_screen(self):
        return self.rect.y < 0
