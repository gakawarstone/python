def f(x):
    return x ** 2


def update_dictionary(d, key):
    if key not in d:
        d[key] = 0
        d[key] = f(key)


def dict_f(d):
    n = int(input())
    my_input = [int(input()) for j in range(n)]
    for i in my_input:
        update_dictionary(d, i)
    for key in my_input:
        print(d[key])


def main():
    d = {}
    d = dict_f(d)


main()
