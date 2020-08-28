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


def btn():
    run = True
    while run:
        pygame.time.delay(10)

        if_close()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            splash()
        if keys[pygame.K_d]:
            run = False

        c.win.fill(cl.white)
        star = Button((0, 0), (100, 100))
        star.hover()
        if star.click():
            run = False

        pygame.display.update()
    time.sleep(0.5)


def dream(img_, text, sprt='', sprt_x=100):
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

        greay_rect = pygame.Surface((500, 500), pygame.SRCALPHA)
        pygame.draw.rect(greay_rect, cl.greay, greay_rect.get_rect())
        c.win.blit(greay_rect, (0, 0))
        y = 2
        for line in text:
            y = gm_print('~ ' + line, 15, (5, y), cl.green)

        pygame.display.update()
    time.sleep(1)


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

        blue_button = Button((0, 400), (250, 100))
        if blue_button.click():
            ch = 1

        red_button = Button((250, 400), (250, 100))
        if red_button.click():
            ch = 2

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


def frame(img_, text, sprt_=None, sprt_x=None):
    gf = Frame()
    gf.background = img_
    gf.text = text
    if sprt_:
        gf.sprite = Frame.Sprite(sprt_)
        if sprt_x:
            gf.sprite.x = sprt_x
    gf.show()


def screen(chapter_name, img_, text, sprt_=None, bg=img.bg_2, sprt_x=100):
    gf = Screen()
    gf.background = bg
    gf.text = text
    gf.chapter_name = chapter_name
    gf.img = img_
    if sprt_:
        gf.sprite = Screen.Sprite(sprt_)
        if sprt_x:
            gf.sprite.x = sprt_
    gf.show()


class Frame:
    id = 0
    id_list = []

    @classmethod
    def get_from_id(self, uid):
        try:
            return Frame.id_list[uid]
        except Exception:
            return False

    class Sprite:
        def __init__(self, img_):
            self.img = img_
            self.x = 100
            self.y = 0

        def show(self):
            draw_img(self.x, self.y, self.img)

    def __init__(self):
        self.background = None
        self.text = None
        self.sprite = None

        self.uid = Frame.id
        Frame.id_list.append(self)
        Frame.id += 1

    def show(self):
        run = True
        while run:
            pygame.time.delay(10)

            if_close()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_c]:
                splash()
            if keys[pygame.K_d]:
                run = False
            if keys[pygame.K_a] and self.uid != 0:
                time.sleep(1)
                Frame.get_from_id(self.uid - 1).show()

            next = Button((0, 0), (c.win_width, c.win_height))
            if next.click():
                run = False

            draw_img(0, 0, self.background)
            if self.sprite:
                self.sprite.show()

            greay_rect = pygame.Surface((500, 100), pygame.SRCALPHA)
            pygame.draw.rect(greay_rect, cl.greay, greay_rect.get_rect())
            c.win.blit(greay_rect, (0, 400))
            gm_print(self.text, 15, (5, 402), cl.green)

            pygame.display.update()
        time.sleep(1)


class Screen(Frame):
    def __init__(self):
        self.background = None
        self.img = None
        self.text = None
        self.sprite = None
        self.chapter_name = None

        self.uid = Screen.id
        Screen.id_list.append(self)
        Screen.id += 1

    def show(self):
        run = True
        previos = Button((10, 440), (170, 50))
        next = Button((320, 440), (170, 50))
        while run:
            pygame.time.delay(10)

            if_close()

            keys = pygame.key.get_pressed()
            next_pressed = next.click()
            if keys[pygame.K_c]:
                splash()
            if keys[pygame.K_d]:
                run = False
            if keys[pygame.K_a] and self.uid != 0:
                time.sleep(1)
                Screen.get_from_id(self.uid - 1).show()
            if previos.click() and self.uid != 0:
                time.sleep(1)
                Screen.get_from_id(self.uid - 1).show()
            if next_pressed:
                run = False

            c.win.fill(cl.dark_white)
            draw_img(0, 0, self.background)
            gm_print('Chapter: ' + self.chapter_name, 30, (10, 10))
            gm_print(self.text, 15, (12, 332))
            draw_img(10, 50, self.img)
            if self.sprite:
                self.sprite.show()
            pygame.draw.rect(c.win, cl.black, (10, 330, 480, 100), 1)

            previos.hover()
            pygame.draw.rect(c.win, cl.black, (10, 440, 170, 50), 1)
            gm_print('PREVIOS', 30, (27, 450))

            pygame.draw.rect(c.win, cl.black, (190, 440, 120, 50), 1)
            gm_print('SAVE', 30, (210, 450))

            next.hover()
            pygame.draw.rect(c.win, cl.black, (320, 440, 170, 50), 1)
            gm_print('NEXT', 30, (370, 450))

            pygame.display.update()
        time.sleep(1)
