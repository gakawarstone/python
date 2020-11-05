word = input()
a = word.split('h')
print(*list(map(lambda x: x[:: -1], a[1: -1])), sep='h')
