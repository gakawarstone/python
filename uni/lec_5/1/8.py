import random
a = [random.randint(-100, 100) for i in range(10)]
b = []
i = 0
while i in range(0, len(a) - 1):
    if a[i] < 0:
        b.append(a[i])
    i += 1

if b:
    print(sum(b))
else:
    print('no elements')
