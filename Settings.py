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

    @abstractmethod
    def run(self):
        pass
