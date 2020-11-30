import random
a = [random.randint(-100, 100) for i in range(10)]
a.sort()
a.reverse()
print(*a)
