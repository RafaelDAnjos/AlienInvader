import pygame
from config import Config
from spaceship import SpaceShip
import game_functions
from pygame.sprite import Group

def run_game():
    pygame.init()
    game_config = Config()
    screen = pygame.display.set_mode((game_config.screen_Width,game_config.screen_heigth))
    spaceship = SpaceShip(screen,game_config)
    pygame.display.set_caption("Alien Invaders!")
    bullets = Group()
    while True:
        game_functions.check_events(game_config,screen,spaceship,bullets)
        spaceship.update()
        game_functions.update_bullets(bullets)
        game_functions.update_screen(game_config,screen,spaceship,bullets)


run_game()