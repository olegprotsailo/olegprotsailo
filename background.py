import pygame
class Background():
    def __init__(self,screen):
        self.screen=screen
        self.bg_img=pygame.image.load("images/parallax2.jpg").convert()
        self.bg_img=pygame.transform.scale(self.bg_img,(1700, 800))
        self.rect_img=self.bg_img.get_rect()
        self.bg_speed=0.2
        self.bg_y1=0
        self.bg_y2=-self.rect_img.height
    def update(self):
        self.bg_y1+=self.bg_speed
        self.bg_y2+=self.bg_speed
        if self.bg_y1>=self.rect_img.height:
            self.bg_y1=-self.rect_img.height
        if self.bg_y2>=self.rect_img.height:
            self.bg_y2=-self.rect_img.height
        self.screen.blit(self.bg_img,(0,self.bg_y1))
        self.screen.blit(self.bg_img,(0,self.bg_y2))