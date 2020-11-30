import random
a = [random.randint(-100, 100) for i in range(10)]
b = []
i = 0
while i in range(0, len(a) - 1):
    if a[i] < 5:
        b.append(a[i])
    i += 1

print(*a)
print(*b)
