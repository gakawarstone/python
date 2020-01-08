from math import sqrt


def siple(x):
    k = int(sqrt(x))
    for i in range(k):
        if x % (i + 2) == 0:
            return 0
    return 1


def main():
    print(siple(int(input())))


main()
