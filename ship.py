import pygame
from pygame.sprite import Sprite


class Ship():

    def __init__(self,screen,ai_settings):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # self.ai_settings = ai_settings  

        self.moving_right = False
        self.moving_left = False

        # self.center = float(self.rect.centerx)


    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right: 
             self.rect.centerx += 1
            #  self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left:
             self.rect.centerx -= 1
            # self.rect.centerx -= self.ai_settings.ship_speed_factor

        # self.rect.centerx = self.center