import game_h as game
import img
import text
chapter_name = 'SPRITE'


def grant():
    game.start()
    game.frame(img.school500, text.down_1, img.down_1, -30)
    game.frame(img.school500, text.down_2, img.down_2)
    game.frame(img.school500, text.down_3, img.down_2)
    game.frame(img.school500, text.down_4, img.down_3)
    game.frame(img.school500, text.grant_1, img.down_2)
    game.choose_2(img.school500, text.grant_mi6, text.grant_all,
                  mi6gun, all_)


def all_():
    game.frame(img.school500, text.grant_t, img.down_2)


def mi6gun():
    game.frame(img.school500, text.grant_f, img.sprite500)
