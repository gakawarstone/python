import math


def chance(x):
    r = 0
    while x > 1:
        x = x / 2
        r += 1
    return r


def chance_with_lie(x):
    var = chance(x)
    r = var + chance(var)
    return r


def main():
    print(chance_with_lie(int(input())))


main()
