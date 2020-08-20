import pygame
import time
import config as c
import color as cl
import game_h as game
import img
pygame.init()
pygame.display.set_caption('GK')


def cubes_init(list_obj):
    cubes = {}
    for i in range(len(list_obj)):
        x, y = list_obj[i]
        cubes[i] = Cube(x, y)
    return cubes


def cubes_draw(cubes, player):
    for cube in cubes:
        cubes[cube].move()
        cubes[cube].draw()
        touch = game.check_touch(player, cubes[cube])
        if touch:
            main()


class Player:
    x = 20
    y = 20

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def move(self):
        self.x, self.y = game.moving(self, self.x, self.y)

    def draw(self):
        #   rect = (self.x, self.y, self.width, self.height)
        #   pygame.draw.rect(c.win, cl.blue, rect)
        game.draw_img(self.x, self.y, img.fire)


class Cube:
    @classmethod
    def death(cls):
        print(cls.width)

    def __init__(self, x, y=0):
        self.x = x
        self.y = y
        self.speed = 2
        self.width = 20
        self.height = 20

    def move(self):
        self.y += self.speed
        """if self.y >= c.win_height - self.height - 1:
            self.speed = -self.speed
        if self.y <= 1:
            self.speed = -self.speed"""
        if self.y >= c.win_height:
            self.y = 0

    def draw(self):
        #        rect = (self.x, self.y, self.width, self.height)
        #        pygame.draw.rect(c.win, cl.red, rect)
        game.draw_img(self.x, self.y, img.barrel)


def lever(cubes, n):
    player = Player(20, 20)
    run = True
    while run:
        pygame.time.delay(10)
        c.win.fill(cl.black)
        game.draw_img(0, 0, img.mg_bg)
        game.if_close()

        cubes_draw(cubes, player)
        game.gm_print("LEVEL " + str(n), 30, (5, 460), cl.red)
        player.move()
        player.draw()

        if player.x + player.width >= c.win_width:
            run = False

        pygame.display.update()
    return


def lever_1():
    cubes = cubes_init([(250, 50)])
    lever(cubes, 1)


def lever_2():
    cubes = cubes_init([(100, 100), (400, 100)])
    lever(cubes, 2)


def lever_3():
    cubes = cubes_init([(250, 0),
                        (150, 50), (350, 50),
                        (250, 100)])
    lever(cubes, 3)


def lever_4():
    cubes = cubes_init([(150, 100), (250, 100), (350, 100),
                        (100, 150), (200, 150), (300, 150), (400, 150),
                        (150, 200), (250, 200), (350, 200)])
    lever(cubes, 4)


def lever_5():
    cubes = cubes_init([(250, 0),
                        (150, 50), (350, 50),
                        (100, 100), (200, 100), (300, 100),
                        (150, 150), (350, 150),
                        (250, 200)])
    lever(cubes, 5)


def lever_6():
    cubes = cubes_init([(150, 100), (250, 100), (350, 100),
                        (100, 150), (200, 150), (300, 150), (400, 150),
                        (150, 200), (250, 200), (350, 200),
                        (100, 250), (200, 250), (300, 250), (400, 250),
                        (150, 300), (250, 300), (350, 300)])
    lever(cubes, 6)


def main():
    if not c.game_win:
        lever_1()
        lever_2()
        lever_3()
        lever_4()
        lever_5()
        lever_6()
        c.game_win = True
        if c.game_win:
            time.sleep(1)
            game.frame(img.jojo500, "Поздравляю ДИО!")

    return


game.start()
main()

pygame.quit()
