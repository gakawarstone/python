import pynovell as game
import img
chapter_name = 'DIO'


def dio():
    game.start()
    game.screen(chapter_name, img.jojo, 'Покажите мне Дио')
    game.screen(chapter_name, img.dio, '...')
    game.screen(chapter_name, img.jojo, 'Я сказал настоящего')
    game.screen(chapter_name, img.real_dio, '...')
    game.screen(chapter_name, img.jojo, 'Превосходно')


def dio_new():
    game.start()
    game.frame(img.jojo500, 'Покажите мне Дио')
    game.frame(img.dio500, '...')
    game.frame(img.jojo500, 'Я сказал настоящего')
    game.frame(img.real_dio500, '...')
    game.frame(img.jojo500, 'Превосходно')
