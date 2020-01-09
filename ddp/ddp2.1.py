def massive(n, mass):
    for i in range(n):
        mass[i] = i + 1
    return


def post(x, y):
    mass = {}
    check = [[y][]]
    massive(x, mass)
    for row in check:
        check[row]
