import pygame
from pygame.sprite import Sprite
class Alien(Sprite):

    def __init__(self,game_config,screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.game_config = game_config
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = screen.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
    
    def blit_me(self):
        self.screen.blit(self.image, self.rect)
