from abc import ABC, abstractmethod


class Settings(ABC):
    caption = 'Alien Invasion'
    screen_width = 800
    screen_height = 600
    bg_color = (176, 196, 222)
    ship_speed = 4

    # Icons
    fav_icon_path = './assets/fav_icon.png'
    spaceship_icon_path = './assets/spaceship.png'

    # Bullet
    bullet_width = 3
    bullet_height = 20
    bullet_speed = 5.5
    bullet_color = (220, 20, 60)

    @abstractmethod
    def run(self):
        pass
