import pygame
import gkt
import game_h as game
import chapter_dio as dio
from chapter_sprite import grant
pygame.init()
pygame.display.set_caption('GK')

dio.dio_new()
grant()
fr = game.Frame.get_from_id(0)
fr.show()

pygame.quit()
