import pygame
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


def main():
    player = Player(10, 10)
    run = True
    while run:
        pygame.time.delay(10)

        game.if_close()

        player.move()
        print(player.x, player.y)

        pygame.display.update()


main()

pygame.quit()
