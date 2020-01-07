def massive(n, mass):
    for i in range(n):
        mass[i] = i + 1
    return


def post(x):
    mass = {}
    check = {}
    massive(x, mass)
    n = 0
    r = 0
    for i in range(x):
        check[0] = mass[i]
        for i in range(x):
            check[1] = mass[i]
            for i in range(x):
                check[2] = mass[i]
                n = 0
                if check[0] > check[1]:
                    n = 1
                if check[1] > check[2]:
                    n = 1
                if check[0] == check[1]:
                    n = 1
                if check[0] == check[2]:
                    n = 1
                if check[1] == check[2]:
                    n = 1
                if check[0] - check[1] == 1:
                    n = 1
                if check[0] - check[1] == -1:
                    n = 1
                if check[0] - check[2] == 1:
                    n = 1
                if check[0] - check[2] == -1:
                    n = 1
                if check[1] - check[2] == 1:
                    n = 1
                if check[1] - check[2] == -1:
                    n = 1
                if check[0] - check[1] == x-1:
                    n = 1
                if check[0] - check[1] == -(x-1):
                    n = 1
                if check[0] - check[2] == x-1:
                    n = 1
                if check[0] - check[2] == -(x-1):
                    n = 1
                if check[1] - check[2] == x-1:
                    n = 1
                if check[1] - check[2] == -(x-1):
                    n = 1
                elif n == 0:
                    r += 1
                    print(check[0], check[1], check[2])
    return r


def main():
    print(post(int(input())))


main()
