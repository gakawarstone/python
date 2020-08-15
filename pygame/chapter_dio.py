import pygame
from splash import splash
import config as c
import color as cl
import game_h as game
import img
chapter_name = 'DIO'


def dio():
    game.start()
    game.screen(chapter_name, img.jojo, 'Покажите мне Дио')
    game.screen(chapter_name, img.dio, '...')
    game.screen(chapter_name, img.jojo, 'Я сказал настоящего')
    game.screen(chapter_name, img.real_dio, '...')
    game.screen(chapter_name, img.jojo, 'Превосходно')
