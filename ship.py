import pygame
class Ship():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load("images/ashot.jpg")
        self.image=pygame.transform.scale(self.image,(100, 60))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx+=3
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.rect.centerx-=3
        if self.moving_up and self.rect.top>self.screen_rect.top:
            self.rect.centery-=3
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.rect.centery+=3
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        self.center = self.screen_rect.centerx