import random as rnd
# RGB colors dict
black = (0, 0, 0)
white = (255, 255, 255)
dark_white = (200, 200, 200)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
rose = (220, 100, 255)
dark_rose = (76, 46, 62)
greay = (35, 35, 35, 200)


def random():
    R = rnd.randint(0, 255)
    G = rnd.randint(0, 255)
    B = rnd.randint(0, 255)
    return (R, G, B)
