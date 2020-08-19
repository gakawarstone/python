import pygame
import config as c
import color as cl
import game_h as game
import img
pygame.init()
pygame.display.set_caption('GK')


def cubes_init(x_list,
               y_list):
    cubes = {}
    for i in range(len(x_list)):
        cubes[i] = Cube(x_list[i])
        cubes[i].y = y_list[i]
    return cubes


def cubes_draw(cubes, player):
    for cube in cubes:
        cubes[cube].move()
        cubes[cube].draw()
        touch = game.check_touch(player, cubes[cube])
        if touch:
            main()


def win():
    game.frame(img.jojo500, "Поздравляю ДИО!")


class Player:
    x = 20
    y = 20

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def move(self):
        self.x, self.y = game.moving(self, self.x, self.y)

    def draw(self):
        rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(c.win, cl.blue, rect)


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
        if self.y >= c.win_height - self.height - 1:
            self.speed = -self.speed
        if self.y <= 1:
            self.speed = -self.speed

    def draw(self):
        rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(c.win, cl.red, rect)


def main():
    player = Player(20, 20)
    cubes = cubes_init([100, 150, 200, 250, 300, 350, 400],
                       [0, 50, 0, 50, 0, 50, 0])
    run = True
    while run:
        pygame.time.delay(10)
        c.win.fill(cl.black)
        game.if_close()

        if player.x + player.width >= c.win_width:
            win()

        cubes_draw(cubes, player)
        player.move()
        player.draw()

        pygame.display.update()


main()

pygame.quit()
