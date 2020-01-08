import numpy as np


def massive(n, mass):
    for i in range(n):
        mass[i] = i + 1
    return


def number(x, mass):
    for i in range(x):
        return mass[i]



def check(mass):
    len = len(mass)



def post(x, y):
    mass = {}
    check = {}
    massive(x, mass)
    n = 0
    k = 0
    r = 0
    c = 0
    for c in range(y):
        for i in range(x):
            check[c] = mass[i]
            k = check[c]
            if k == x:
                c -= 1
            if c < y:
                c += 1
            print(k)
    return r


def main():
    print(post(8, 3))


main()
