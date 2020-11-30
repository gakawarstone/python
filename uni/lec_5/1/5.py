import random
a = [random.randint(-10, 10) for i in range(10)]
print(*a)
i = 0
while i in range(0, len(a) - 1):
    if a[i] % 2 == 1:
        a[i] = 0
    i += 1
print(*a)
