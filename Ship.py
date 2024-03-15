import pygame.image

from Settings import Settings
from Bullet import Bullet


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
        self.bullets = pygame.sprite.Group()

    def update(self):
        if self.is_moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
        if self.is_moving_left and self.rect.left > 0:
            self.rect.x -= self.speed
        for bullet in self.bullets:
            if bullet.is_bullet_off_screen():
                self.bullets.remove(bullet)
            else:
                bullet.update()

    def draw(self):
        self.screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw_bullet()

    def fire(self):
        self.bullets.add(Bullet(self.screen, self.rect.midtop))
