# import files
import pygame
from splash import splash
import config as c
import color as cl
import game_h as game
import img
import chapter_dio as dio
from chapter_sprite import grant

# pygame init function and set window title
pygame.init()
pygame.display.set_caption('GK')

# functions call
dio.dio_new()
grant()

# close window
pygame.quit()
