import pygame
import game_h as game
import config as c
import color as cl


class Mouse():
    width = 1
    height = 1

    def get_pos(self):
        self.x, self.y = pygame.mouse.get_pos()
        return self.x, self.y


class Button():
    def __init__(self, pos, size):
        self.x, self.y = pos
        self.width, self.height = size

    def hover(self, color=cl.dark_hover):
        mouse = Mouse()
        mouse.get_pos()
        if game.check_touch(self, mouse):
            rect = (self.x, self.y, self.width, self.height)
            pygame.draw.rect(c.win, color, rect)

    def click(self):
        mouse = Mouse()
        mouse.get_pos()
        if game.check_touch(self, mouse):
            if pygame.mouse.get_pressed()[0]:
                return True
        return False

    def draw(self, color=cl.black):
        rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(c.win, color, rect, 1)
