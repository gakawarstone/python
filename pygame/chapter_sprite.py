import pygame
from splash import splash
import config as c
import color as cl
import game_h as game
import img
import text
chapter_name = 'SPRITE'


def sprite():
    game.start()
    game.screen_new(chapter_name, img.school500, 'Я спрайт', img.sprite500)
    game.screen_new(chapter_name, img.school500, text.down_1, img.down_1, -30)
    game.screen_new(chapter_name, img.school500, text.down_2, img.down_2)
    game.screen_new(chapter_name, img.school500, text.down_3, img.down_2)
    game.screen_new(chapter_name, img.school500, text.down_4, img.down_3)
    game.screen_new(chapter_name, img.school500, text.grant_1, img.down_2)
    ch = game.choose_2(img.school500, text.grant_all, text.grant_mi6)
    if ch == 1:
        all_()
    if ch == 2:
        mi6gun()


def all_():
    game.screen_new(chapter_name, img.school500, text.grant_t, img.down_2)


def mi6gun():
    game.screen_new(chapter_name, img.school500, text.grant_f, img.down_3)
