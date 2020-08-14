import pygame
from splash import splash
import config as c
import color as cl
import time
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
    if keys[pygame.K_s] and y < c.win_width - width:
        y += speed
    if keys[pygame.K_a] and x > 0:
        x -= speed
    if keys[pygame.K_d] and x < c.win_height - height:
        x += speed


def draw_img(x, y, img):
    c.win.blit(img, (x, y))


def gm_print(str, size, position):
    f = pygame.font.SysFont('arial', size)
    text = f.render(str, 1, cl.black)
    c.win.blit(text, position)


def screen(chapter_name, img, text):
    run = True
    while run:
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            splash()
        if keys[pygame.K_d]:
            run = False

        c.win.fill(cl.dark_white)
        gm_print('Chapter: ' + chapter_name, 30, (10, 10))
        gm_print(text, 15, (12, 332))
        draw_img(10, 50, img)
        pygame.draw.rect(c.win, cl.black, (10, 330, 480, 100), 1)

        pygame.draw.rect(c.win, cl.black, (10, 440, 170, 50), 1)
        gm_print('PREVIOS', 30, (27, 450))
        pygame.draw.rect(c.win, cl.black, (190, 440, 120, 50), 1)
        gm_print('SAVE', 30, (210, 450))
        pygame.draw.rect(c.win, cl.black, (320, 440, 170, 50), 1)
        gm_print('NEXT', 30, (370, 450))
        pygame.display.update()
    time.sleep(1)
