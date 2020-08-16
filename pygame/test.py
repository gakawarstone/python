import pygame
from splash import splash
import config as c
import color as cl
import game_h as game
import img
import chapter_dio as dio
from chapter_sprite import sprite
import random as rnd
pygame.init()
pygame.display.set_caption('GK')

game.choose_2(img.school500, 's', 'v')
R = rnd.randint(0, 255)
G = rnd.randint(0, 255)
B = rnd.randint(0, 255)
print(R, G, B)

pygame.quit()
