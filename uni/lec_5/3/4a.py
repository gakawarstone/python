from math import sqrt


def simple(x):
    k = int(sqrt(x))
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(k):
        if x % (i + 2) == 0:
            return False
    return True


(a, b) = (int(input()) for i in range(2))

for i in range(a, b + 1):
    if simple(i):
        print(i)
