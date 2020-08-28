# import files
import pygame
import chapter_dio as dio
from chapter_sprite import grant

# pygame init function and set window title
pygame.init()
pygame.display.set_caption('GK')

# functions call
dio.dio()
dio.dio_new()
grant()

# close window
pygame.quit()
