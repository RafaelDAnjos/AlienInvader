import sys
import pygame
from bullet import Bullet

def check_key_down_events(event,game_config,spaceship,screen,bullets):
    if event.key == pygame.K_RIGHT:
        spaceship.moving_right = True
    if event.key == pygame.K_LEFT:
        spaceship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(game_config,screen,bullets,spaceship)
    # if event.key == pygame.K_UP:
    #     spaceship.moving_up = True
    # if event.key == pygame.K_DOWN:
    #     spaceship.moving_down = True
def fire_bullet(game_config,screen,bullets,spaceship):
    if(len(bullets) < game_config.bullets_alowed):
        new_bullet = Bullet(game_config,screen,spaceship)
        bullets.add(new_bullet)

def check_key_up_events(event,spaceship):
    if event.key == pygame.K_RIGHT:
        spaceship.moving_right = False
    if event.key == pygame.K_LEFT:
        spaceship.moving_left = False
    # if event.key == pygame.K_UP:
    #     spaceship.moving_up = False
    # if event.key == pygame.K_DOWN:
    #     spaceship.moving_down = False
def check_events(game_config,screen,spaceship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event,game_config,spaceship,screen,bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event,spaceship)

def update_screen(game_config,screen,spaceship,bullets):
    screen.fill(game_config.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    spaceship.blit_me()
    pygame.display.flip()
def erase_old_bullets(bullets):

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
def update_bullets(bullets):
    bullets.update()
    erase_old_bullets(bullets)