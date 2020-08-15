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
