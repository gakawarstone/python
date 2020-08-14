import pygame
from splash import splash
import config as c
import color as cl
pygame.init()
pygame.display.set_caption('GK')

jojo = pygame.image.load('jojo')


def draw_img(x, y):
    c.win.blit(jojo, (x, y))


def main_screen():
    run = True
    while run:
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            splash()

        c.win.fill(cl.white)
        draw_img(100, 100)
        pygame.display.update()


main_screen()


pygame.quit()
