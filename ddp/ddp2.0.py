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
    check = np.zeros(y, int)
    n = 0
    k = 0
    r = 0
    c = 0
    i = 0
    full_row = False
    for i in range(x):
        c = y - 1
        check[c] = mass[i]
        k = check[c]
        if i == x - 1:
            check[c - 1] += 1
            # post(x, y)
        if check[c - 1] == x:
            c -= 1
        if check[c] < x - 1 and c != y - 1:
            c += 1
        print(check[0], check[1], check[2])
    return r


def main():
    print(post(8, 3))


main()
