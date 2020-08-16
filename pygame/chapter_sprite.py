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
    ch = game.choose_2(img.school500, 'вариант А', 'вариант В')
    if ch == 1:
        game.screen_new(chapter_name, img.school500, 'Ты выбрал вариант А', img.sprite500)
    if ch == 2:
        game.screen_new(chapter_name, img.school500, 'Ты выбрал вариант В', img.sprite500)
