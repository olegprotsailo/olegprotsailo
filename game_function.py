import pygame,sys
from alien import Alien
from bullet import Bullet
from random import randint
from time import sleep
num=randint(0,10)
def check_events(game_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,game_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            chek_keyup_events(event,ship)
def update_screen(background,ship,bullets,aliens,screen):
    #screen.fill(game_settings.bg_color)
    background.update()
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()
def check_keydown_events(event,game_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        if len(bullets) < game_settings.bullets_allowed:
            new_bullet = Bullet(game_settings,screen,ship)
            bullets.add(new_bullet)
def chek_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    if event.key == pygame.K_SPACE:
        new_bullet = False
def update_bullets(bullets, aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    colisitions=pygame.sprite.groupcollide(bullets,aliens,True,True)
#def create_fleet(game_settings, screen, aliens):
#     alien = Alien(game_settings, screen)
#      alien_width = alien.rect.width

#     available_space_x = game_settings.screen_width - alien_width * 2
#     number_aliens_x = int(available_space_x/(alien_width*2))
#     print(number_aliens_x)
#     for alien_number in range(number_aliens_x):
#         alien = Alien(game_settings, screen)
#         alien.rect.x = alien_width * 2 * alien_number
#         aliens.add(alien)

def get_number_aliens_x(game_settings, alien_width):
    available_space_x = game_settings.screen_width - alien_width * 2
    number_aliens_x = int(available_space_x / (alien_width * 2))
    return number_aliens_x

def get_number_aliens_rows(game_settings, ship, alien_height):
    available_space_y = game_settings.screen_height - ship.rect.height
    number_aliens_y = int(available_space_y / (alien_height * 2))
    return number_aliens_y

def create_alien(game_settings, screen, alien_number, aliens, row_number):
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.rect.x = alien_width * 2 * alien_number
    alien.rect.y = alien.rect.height * 2 * row_number
    aliens.add(alien)

def create_fleet(game_settings, screen, aliens, ship):
    alien = Alien(game_settings, screen)
    numbers_aliens = get_number_aliens_x(game_settings, alien.rect.width)
    numbers_rows = get_number_aliens_rows(game_settings, ship, alien.rect.height)
    print(numbers_rows, numbers_aliens)
    for row_number in range(randint(0,10)):
        for alien_number in range(numbers_aliens):
            create_alien(game_settings, screen, alien_number, aliens, row_number)
def update_aliens(game_settings,aliens,stats,screen,ship,bullets):
    aliens.update()
    check_fleet_adges(game_settings,aliens)
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(stats,screen,bullets,ship,game_settings,aliens)
def check_fleet_adges (game_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_adges():
            change_fleet_direction(game_settings,aliens)
            break
def change_fleet_direction (game_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction*=-1
def ship_hit(stats,screen,bullets,ship,game_settings,aliens):
    stats.ships_left =-1
    aliens.empty()
    bullets.empty()
    create_fleet(game_settings, screen, aliens, ship)
    ship.center_ship()
    sleep = 0.5

