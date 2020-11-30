import random
a = [random.randint(-100, 100) for i in range(3)]
b = ('aaa' for i in range(3))
c = {random.random() for i in range(3)}
d = {}
for i in range(0, 2):
    d[random.randint(-100, 100)] = 'aaa'

print(*a)
print(*b)
print(*c)
print(*d)

print(a + list(c))
print(set(a))
