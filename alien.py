import pygame
from pygame.sprite import Sprite
class Alien(Sprite):

    def __init__(self,game_config,screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.game_config = game_config 