import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):

    def __init__(self,game_config,screen,spaceship):
        
        super(Bullet, self).__init__()
        self.screen = screen
        self.game_config = game_config
        self.rect = pygame.Rect(0, 0, game_config.bullet_width,game_config.bullet_height)

        self.rect.centerx = spaceship.rect.centerx
        self.rect.top = spaceship.rect.top
        self.y = float(self.rect.y)
        self.color = game_config.bullet_color
        self.speed_factor = game_config.bullet_speed_factor

    def update(self):
        self.y -= self.game_config.bullet_speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
