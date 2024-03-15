import pygame.image

from Settings import Settings


class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load(Settings.spaceship_icon_path)
        self.image = pygame.transform.scale(self.image, (56, 56))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.is_moving_right = False
        self.is_moving_left = False
        self.speed = Settings.ship_speed

    def update(self):
        if self.is_moving_right:
            self.rect.x += self.speed
        if self.is_moving_left:
            self.rect.x -= self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)
