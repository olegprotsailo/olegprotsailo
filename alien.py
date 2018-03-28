import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,game_settings,screen):
        super().__init__()
        self.screen=screen
        self.game_settings=game_settings
        self.image=pygame.image.load("images/alien.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect=self.image.get_rect()
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.rect.x += self.game_settings.aliens_speed_factor*self.game_settings.fleet_direction
    def check_adges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >=screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True
