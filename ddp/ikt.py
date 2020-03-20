def F(n):
    if n > 1:
        print(n)
        F(n - 1)
        F(n - 2)
        F(n - 3)


def main():
    F(5)


main()
