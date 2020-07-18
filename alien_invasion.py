import sys
import pygame
from settings import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien    #ispe shak ha


def run_game():
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings,screen)
    alien = Alien(ai_settings,screen)   #ispe shak ha
    bullets = Group()
    aliens = Group()
    pygame.display.set_caption("Alien Invasion")
    gf.create_fleet(ai_settings, screen, ship, aliens) #new
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # bullets.update()
        # Get rid of bullets that have disappeared.
        # for bullet in bullets.copy():
        #     if bullet.rect.bottom <= 0:
        #         bullets.remove(bullet)
        # print(len(bullets))
        gf.update_bullets(bullets)                     
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)  #ispe shak tha
        # update_bullets(bullets)

run_game()