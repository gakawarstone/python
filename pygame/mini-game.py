import pygame
import random
from splash import splash
import config as c
import color as cl
import game_h as game
import img
import chapter_dio as dio
from chapter_sprite import sprite
pygame.init()
pygame.display.set_caption('GK')


class Player:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 20
        self.y = 20

    def move(self):
        self.x, self.y = game.moving(self.x, self.y)

    def draw(self):
        rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(c.win, cl.random(), rect)


class Cube:
    def __init__(self, x):
        self.width = 20
        self.height = 20
        self.x = x
        self.y = 0
        self.speed = 2

    def move(self):
        self.y += self.speed
        if self.speed == 0:
            self.speed = 1
        if self.speed >= 2:
            self.speed == 2
        if self.speed <= -2:
            self.speed == -2
        if self.y >= c.win_height - self.height - 1:
            self.speed = -self.speed
            self.speed += random.randint(-1, 1)
        if self.y <= 1:
            self.speed = -self.speed
            self.speed += random.randint(-1, 1)

    def draw(self):
        rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(c.win, cl.random(), rect)


def main():
    player = Player(20, 20)
    cube_1 = Cube(100)
    cube_2 = Cube(200)
    cube_3 = Cube(300)
    cube_4 = Cube(400)
    run = True
    while run:
        pygame.time.delay(10)

        game.if_close()

        player.move()
        cube_1.move()
        cube_2.move()
        cube_3.move()
        cube_4.move()
        print(player.x, player.y)

        c.win.fill(cl.black)
        player.draw()
        cube_1.draw()
        cube_2.draw()
        cube_3.draw()
        cube_4.draw()
        pygame.display.update()


main()

pygame.quit()
