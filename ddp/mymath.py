import math


def chance(x):
    r = 0
    while x > 1:
        x = x / 2
        r += 1
    return r


def main():
    print(chance(int(input())))


main()
