import pygame

class SpaceShip():

    def __init__(self,screen,game_config):
        self.screen = screen
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.game_config = game_config
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.movin_down = False

    def blit_me(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_config.spaceship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.game_config.spaceship_speed_factor
        # if self.moving_right:
        #     self.rect.bottom -= 1
        # if self.movin_down:
        #     self.rect.bottom += 1
        self.rect.centerx = self.center