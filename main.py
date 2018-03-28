
import pygame,sys
import game_function as g_f
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from background import Background
from gamestats import Stats
from alien import Alien
def init_game():
    pygame.init()
    game_settings=Settings()
    screen=pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    ship=Ship(screen)
    bullets=Group()
    background=Background(screen)
    aliens=Group()
    stats = Stats(game_settings)
    g_f.create_fleet(game_settings, screen, aliens, ship)
    pygame.display.set_caption("Our first game")
    while True:
        g_f.check_events(game_settings,screen,ship,bullets)
        g_f.update_screen(background,ship,bullets,aliens,screen)
        ship.update()
        bullets.update()
        g_f.update_aliens(game_settings,aliens,stats,screen,ship,bullets)
        g_f.update_bullets(bullets, aliens)
init_game()