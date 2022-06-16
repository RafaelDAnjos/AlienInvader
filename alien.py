import pygame
from pygame.sprite import Sprite
class Alien(Sprite):

    def __init__(self,game_config,screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.game_config = game_config
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
    
    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.game_config.alien_speed_factor*self.game_config.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
