import pynovell as game
import img
import text
chapter_name = '2021'


def naruto():
    game.start()
    game.frame(img.room_night, text.naruto_1, img.down_3)
    game.frame(img.room_night, text.naruto_2, img.down_2)
    game.frame(img.room_night, text.naruto_3, img.down_2)
    game.frame(img.room_night, text.naruto_4, img.down_3)
    game.frame(img.room_night, text.naruto_5, img.down_2)
    game.frame(img.room_night, text.naruto_6, img.down_3)
