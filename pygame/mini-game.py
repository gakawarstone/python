import pygame
import config as c
import color as cl
import game_h as game
pygame.init()
pygame.display.set_caption('GK')


def cubes_init(x_list):
    cubes = {}
    for x in x_list:
        cubes[x] = Cube(x)
    return cubes


def cubes_draw(cubes, player):
    for cube in cubes:
        cubes[cube].move()
        cubes[cube].draw()
        touch = game.check_touch(player, cubes[cube])
        if touch:
            pygame.quit()
            quit()


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

    def __init__(self, x):
        self.x = x
        self.y = 0
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
    cubes = cubes_init([100, 200, 300, 400])
    run = True
    while run:
        pygame.time.delay(10)
        c.win.fill(cl.black)
        game.if_close()

        cubes_draw(cubes, player)
        player.move()
        player.draw()

        pygame.display.update()


main()

pygame.quit()
