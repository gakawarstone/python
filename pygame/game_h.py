import pygame
from splash import splash
import config as c
import color as cl
import img
import time


def check_touch(obj_1, obj_2):
    if obj_1.x >= obj_2.x and obj_1.x <= obj_2.x + obj_2.width:
        if obj_1.y >= obj_2.y and obj_1.y <= obj_2.y + obj_2.height:
            return True
    if obj_2.x >= obj_1.x and obj_2.x <= obj_1.x + obj_1.width:
        if obj_2.y >= obj_1.y and obj_2.y <= obj_1.y + obj_1.height:
            return True
    return False


def if_close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


def choose_2(img_, ch_1, ch_2, sprt='', sprt_x=100):
    ch = 0
    while ch == 0:
        pygame.time.delay(10)

        if_close()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            splash()
        if keys[pygame.K_q]:
            ch = 1
        if keys[pygame.K_e]:
            ch = 2

        draw_img(0, 0, img_)
        if sprt:
            draw_img(sprt_x, 0, sprt)

        greay_rect = pygame.Surface((500, 100), pygame.SRCALPHA)
        pygame.draw.rect(greay_rect, cl.greay, greay_rect.get_rect())
        c.win.blit(greay_rect, (0, 400))

        blue_rect = pygame.Surface((250, 100), pygame.SRCALPHA)
        pygame.draw.rect(blue_rect, cl.blue_a, blue_rect.get_rect())
        c.win.blit(blue_rect, (0, 400))

        red_rect = pygame.Surface((250, 100), pygame.SRCALPHA)
        pygame.draw.rect(red_rect, cl.red_a, red_rect.get_rect())
        c.win.blit(red_rect, (250, 400))

        gm_print(ch_1, 15, (5, 402), cl.green)
        gm_print(ch_2, 15, (255, 402), cl.green)
        gm_print('PRESS Q', 10, (5, 485), cl.green)
        gm_print('PRESS E', 10, (450, 485), cl.green, c.win_width)
        pygame.display.update()
    time.sleep(1)
    return ch


def moving(obj, x, y, speed=1):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y > 0:
        y -= speed
    if keys[pygame.K_s] and y < c.win_width - obj.width:
        y += speed
    if keys[pygame.K_a] and x > 0:
        x -= speed
    if keys[pygame.K_d] and x < c.win_height - obj.height:
        x += speed
    return x, y


def draw_img(x, y, img, a=0):
    if a != 0:
        img = pygame.Surface((x, y), pygame.SRCALPHA)
        img.set_colorkey(cl.black)
        img.set_alpha(a)
    c.win.blit(img, (x, y))


def gm_print(str, size, pos, color=cl.black, max_width=c.win_width - 5):
    f = pygame.font.SysFont('arial', size)
    words = [word.split(' ') for word in str.splitlines()]
    space = f.size(' ')[0]  # The width of a space.
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

        if_close()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            splash()
        if keys[pygame.K_SPACE]:
            run = False

        c.win.fill(cl.dark_white)
        draw_img(0, 0, img.start_bg)
        draw_img(105, 215, img.mylogo_rose)
        gm_print('Welcome', 50, (150, 150), cl.dark_rose)
        gm_print('Press space to continue...', 30, (85, 400), cl.dark_rose)
        pygame.display.update()
    time.sleep(1)


def screen(chapter_name, img_, text, sprt='', bg=img.bg_2):
    run = True
    while run:
        pygame.time.delay(10)

        if_close()

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


def frame(img_, text, sprt='', sprt_x=100):
    run = True
    while run:
        pygame.time.delay(10)

        if_close()

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
