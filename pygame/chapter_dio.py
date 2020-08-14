import pygame
from splash import splash
import config as c
import color as cl
import game_h as game
import img
import time
chapter_name = 'DIO'


def dio():
    game.screen(chapter_name, img.jojo, 'Покажите мне Дио')
    time.sleep(1)
    game.screen(chapter_name, img.dio, '...')
    time.sleep(1)
    game.screen(chapter_name, img.jojo, 'Я сказал настоящего')
    time.sleep(1)
    game.screen(chapter_name, img.real_dio, '...')
    time.sleep(1)
    game.screen(chapter_name, img.jojo, 'Превосходно')
    time.sleep(1)
