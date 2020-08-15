import pygame
from splash import splash
import config as c
import color as cl
import game_h as game
import img
chapter_name = 'SPRITE'


def sprite():
    game.start()
    game.screen_new(chapter_name, img.school500, 'Я спрайт', img.sprite500)
