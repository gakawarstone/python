import pygame
import game_h as game
from game_h import gm_print, if_close, Button, draw_img, splash
import color as cl
import config as c
import time
import img
start = game.start


def choose_2(img_, ch_1, ch_2, f_1, f_2, sprt_=None, sprt_x=100):
    gf = Choose_2()
    gf.background = img_
    gf.ch_1 = ch_1
    gf.ch_2 = ch_2
    gf.f_1 = f_1
    gf.f_2 = f_2
    if sprt_:
        gf.sprite = Frame.Sprite(sprt_)
        if sprt_x:
            gf.sprite.x = sprt_x
    gf.show()


def dream(img_, text):
    run = True
    while run:
        pygame.time.delay(10)

        if_close()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            game.splash()
        if keys[pygame.K_d]:
            run = False

        draw_img(0, 0, img_)

        greay_rect = pygame.Surface((500, 500), pygame.SRCALPHA)
        pygame.draw.rect(greay_rect, cl.greay, greay_rect.get_rect())
        c.win.blit(greay_rect, (0, 0))
        y = 2
        for line in text:
            y = gm_print('~ ' + line, 15, (5, y), cl.green)

        pygame.display.update()
    time.sleep(1)


def frame(img_, text, sprt_=None, sprt_x=None):
    gf = Frame()
    gf.background = img_
    gf.text = text
    gf.autoclose = False
    if sprt_:
        gf.sprite = Frame.Sprite(sprt_)
        if sprt_x:
            gf.sprite.x = sprt_x
    gf.show()


def first_frame(img_, text, sprt_=None, sprt_x=None):
    gf = Frame()
    gf.background = img_
    gf.text = text
    gf.autoclose = True
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
    save_id = 0
    id_list = []

    @classmethod
    def get_from_id(self, uid):
        try:
            return Frame.id_list[uid]
        except Exception:
            return False

    @classmethod
    def save(self, uid):
        sv = game.File_with_save('save.txt')
        sv.write(str(uid))
        Frame.save_id += 1

    @classmethod
    def load_save(self, save_id):
        pass

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
        self.outoclose = False

        self.uid = Frame.id
        Frame.id_list.append(self)
        Frame.id += 1

    def show(self):
        run = True
        next = Button((0, 0), (c.win_width, c.win_height))
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
                Frame.get_from_id(self.uid - 1).show()
                if self.autoclose:
                    break
            if next_pressed:
                run = False

            draw_img(0, 0, self.background)
            if self.sprite:
                self.sprite.show()

            if game.hover_zone((0, 0), (500, 50)):
                return

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

        self.uid = Frame.id
        Frame.id_list.append(self)
        Frame.id += 1

    def show(self):
        run = True
        previos = Button((10, 440), (170, 50))
        save = Button((190, 440), (120, 50))
        next = Button((320, 440), (170, 50))
        while run:
            pygame.time.delay(10)

            if_close()

            keys = pygame.key.get_pressed()
            previos_pressed = previos.click() and self.uid != 0
            save_pressed = save.click()
            next_pressed = next.click()
            if keys[pygame.K_c]:
                splash()
            if keys[pygame.K_d]:
                run = False
            if keys[pygame.K_a] and self.uid != 0:
                time.sleep(1)
                Frame.get_from_id(self.uid - 1).show()
            if previos_pressed:
                time.sleep(1)
                Frame.get_from_id(self.uid - 1).show()
            if next_pressed:
                run = False
            if save_pressed:
                Frame.save(self.uid)

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

            save.hover()
            pygame.draw.rect(c.win, cl.black, (190, 440, 120, 50), 1)
            gm_print('SAVE', 30, (210, 450))

            next.hover()
            pygame.draw.rect(c.win, cl.black, (320, 440, 170, 50), 1)
            gm_print('NEXT', 30, (370, 450))

            pygame.display.update()
        time.sleep(1)


class Choose_2(Frame):
    def __init__(self):
        self.background = None
        self.ch_1 = None
        self.ch_2 = None
        self.f_1 = None
        self.f_2 = None
        self.sprite = None

        self.uid = Frame.id
        Frame.id_list.append(self)
        Frame.id += 1

    def show(self):
        while len(Frame.id_list) - 1 > self.uid:
            Frame.id_list.pop()
        Frame.id = self.uid + 1
        ch = None
        while ch is None:
            pygame.time.delay(10)

            if_close()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_c]:
                splash()
            if keys[pygame.K_a] and self.uid != 0:
                time.sleep(1)
                Frame.get_from_id(self.uid - 1).show()
            if keys[pygame.K_q]:
                ch = self.f_1
            if keys[pygame.K_e]:
                ch = self.f_2

            draw_img(0, 0, self.background)
            if self.sprite:
                self.sprite.show()

            blue_button = Button((0, 400), (250, 100))
            if blue_button.click():
                ch = self.f_1

            red_button = Button((250, 400), (250, 100))
            if red_button.click():
                ch = self.f_2

            greay_rect = pygame.Surface((500, 100), pygame.SRCALPHA)
            pygame.draw.rect(greay_rect, cl.greay, greay_rect.get_rect())
            c.win.blit(greay_rect, (0, 400))

            blue_rect = pygame.Surface((250, 100), pygame.SRCALPHA)
            pygame.draw.rect(blue_rect, cl.blue_a, blue_rect.get_rect())
            c.win.blit(blue_rect, (0, 400))

            red_rect = pygame.Surface((250, 100), pygame.SRCALPHA)
            pygame.draw.rect(red_rect, cl.red_a, red_rect.get_rect())
            c.win.blit(red_rect, (250, 400))

            gm_print(self.ch_1, 15, (5, 402), cl.green)
            gm_print(self.ch_2, 15, (255, 402), cl.green)
            gm_print('PRESS Q', 10, (5, 485), cl.green)
            gm_print('PRESS E', 10, (450, 485), cl.green, c.win_width)
            pygame.display.update()
        time.sleep(1)
        ch()
