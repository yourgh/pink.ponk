from pygame import*
back = (255, 0, 0)
wind_width = 500
wind_height = 500
window = display.set_mode((wind_width, wind_height))
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = image.load(loadimage)
        self.speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y
        