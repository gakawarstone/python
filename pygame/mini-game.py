import pygame
import config as c
import color as cl
import game_h as game
pygame.init()
pygame.display.set_caption('GK')


def cubes():

    return


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
    cube_1 = Cube(100)
    cube_2 = Cube(200)
    cube_3 = Cube(300)
    cube_4 = Cube(400)
    run = True
    while run:
        pygame.time.delay(10)
        c.win.fill(cl.black)
        game.if_close()

        player.move()
        cube_1.move()
        cube_2.move()
        cube_3.move()
        cube_4.move()

        cube_1.draw()
        cube_2.draw()
        cube_3.draw()
        cube_4.draw()
        player.draw()

        touch_1 = game.check_touch(player, cube_1)
        touch_2 = game.check_touch(player, cube_2)
        touch_3 = game.check_touch(player, cube_3)
        touch_4 = game.check_touch(player, cube_4)
        if touch_1 or touch_2 or touch_3 or touch_4:
            pygame.quit()
            quit()
        pygame.display.update()


main()

pygame.quit()
