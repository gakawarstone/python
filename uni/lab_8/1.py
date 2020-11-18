a = list(map(lambda x: x[:: -1], input().split('h')[1: -1]))
a.reverse()
print(*a, sep='h')
