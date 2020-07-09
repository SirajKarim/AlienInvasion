import pygame

class Ship():
    def __init__(self,ai_settings,screen):    #new
        self.screen = screen
        self.ai_settings = ai_settings   #new
        self.image = pygame.image.load('images/ship.bmp')  
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx) #new
        #movement flag
        self.move_right = False
        self.move_left = False

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor  #new
        elif self.move_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor #new

        self.rect.centerx = self.center