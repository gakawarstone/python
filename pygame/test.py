import pygame
import gkt
import game_h as game
pygame.init()
pygame.display.set_caption('GK')

first = game.Frame()
second = game.Frame()
print(first.uid, second.uid)
print(game.Frame.id_list)
Frame = game.Frame
print(Frame.get_from_id(0))

pygame.quit()
