import random as rnd
# RGB colors dict
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


def random():
    R = rnd.randint(0, 255)
    G = rnd.randint(0, 255)
    B = rnd.randint(0, 255)
    return (R, G, B)
