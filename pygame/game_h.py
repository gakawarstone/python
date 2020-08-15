import pygame
from splash import splash
import config as c
import color as cl
import img
import time
x = 23
y = 78
width = 70
height = 30
speed = 1
speed_x = 1
speed_y = 1


def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


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


def draw_img(x, y, img, a=0):
    if a != 0:
        img = pygame.Surface((x, y), pygame.SRCALPHA)
        img.set_colorkey(cl.black)
        img.set_alpha(a)
    c.win.blit(img, (x, y))


def gm_print(str, size, pos, color=cl.black):
    f = pygame.font.SysFont('arial', size)
    words = [word.split(' ') for word in str.splitlines()]
    space = f.size(' ')[0]  # The width of a space.
    max_width = c.win_width - 10
    x, y = pos
    for line in words:
        for word in line:
            word_surface = f.render(word, 1, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            c.win.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height


def start():
    run = True
    while run:
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            splash()
        if keys[pygame.K_SPACE]:
            run = False

        c.win.fill(cl.dark_white)
        draw_img(0, 0, img.start_bg)
        gm_print('Welcome', 50, (150, 150), cl.dark_rose)
        gm_print('Press space to continue...', 30, (85, 400), cl.dark_rose)
        pygame.display.update()
    time.sleep(1)


def screen(chapter_name, img_, text, sprt='', bg=img.bg_2):
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
        draw_img(0, 0, bg)
        gm_print('Chapter: ' + chapter_name, 30, (10, 10))
        gm_print(text, 15, (12, 332))
        draw_img(10, 50, img_)
        if sprt:
            draw_img(200, 50, sprt)
        pygame.draw.rect(c.win, cl.black, (10, 330, 480, 100), 1)

        pygame.draw.rect(c.win, cl.black, (10, 440, 170, 50), 1)
        gm_print('PREVIOS', 30, (27, 450))
        pygame.draw.rect(c.win, cl.black, (190, 440, 120, 50), 1)
        gm_print('SAVE', 30, (210, 450))
        pygame.draw.rect(c.win, cl.black, (320, 440, 170, 50), 1)
        gm_print('NEXT', 30, (370, 450))
        pygame.display.update()
    time.sleep(1)


def screen_new(chapter_name, img_, text, sprt='', sprt_x=100):
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

        draw_img(0, 0, img_)
        if sprt:
            draw_img(sprt_x, 0, sprt)

        greay_rect = pygame.Surface((500, 100), pygame.SRCALPHA)
        pygame.draw.rect(greay_rect, cl.greay, greay_rect.get_rect())
        c.win.blit(greay_rect, (0, 400))
        gm_print(text, 15, (5, 402), cl.green)

        pygame.display.update()
    time.sleep(1)
