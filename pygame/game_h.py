import pygame
from splash import splash
import config as c
import color as cl
import img
import time
from buttons import Button


def menu():
    run = True
    while run:
        pygame.time.delay(10)
        c.win.fill(cl.white)

        if_close()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            splash()

        pygame.display.update()
    time.sleep(1)


def hover_zone(pos, size):
    zone = Button(pos, size)
    zone.hover(cl.greay)


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
    return y


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


class File_with_save:
    def __init__(self, file_name):
        self.link = file_name

    def write(self, str):
        with open(self.link, 'a') as the_file:
            the_file.write(str + '\n')

    def read(self, str_number):
        pass
