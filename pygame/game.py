import pygame
from splash import splash
import config
pygame.init()
pygame.display.set_caption('GK')

x = 23
y = 78
width = 70
height = 30
speed = 1
speed_x = 1
speed_y = 1


def moving():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y > 0:
        y -= speed
    if keys[pygame.K_s] and y < 500 - width:
        y += speed
    if keys[pygame.K_a] and x > 0:
        x -= speed
    if keys[pygame.K_d] and x < 500 - height:
        x += speed


def main_screen():
    return


splash()


pygame.quit()
