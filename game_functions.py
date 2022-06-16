import sys
import pygame
from bullet import Bullet
from alien import Alien

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

def update_screen(game_config,screen,spaceship,bullets,aliens):
    screen.fill(game_config.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    spaceship.blit_me()
    aliens.draw(screen)
    pygame.display.flip()

def erase_old_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_bullets(bullets):
    bullets.update()
    erase_old_bullets(bullets)

def create_fleet(game_config,screen,aliens,spaceship):
    alien = Alien(game_config, screen)
    number_aliens_x = get_number_aliens_x(game_config,alien.rect.width)
    number_rows = get_number_rows(game_config,spaceship.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_config,screen,aliens,alien_number,row_number)

def get_number_aliens_x(game_config, alien_width):
    available_space_x = game_config.screen_Width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(game_config,screen,aliens,alien_number,row_number):
    alien = Alien(game_config, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height *row_number
    aliens.add(alien)

def get_number_rows(game_config,spaceship_height,alien_height):
    available_space_y = (game_config.screen_heigth -(3 * alien_height) - spaceship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def update_aliens(game_config,aliens):
    check_fleet_edges(game_config,aliens)
    aliens.update()


def check_fleet_edges(game_config,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_config, aliens)
            break

def change_fleet_direction(game_config,aliens):
    for alien in aliens.sprites():
        alien.rect.y += game_config.fleet_drop_speed
    game_config.fleet_direction *= -1
