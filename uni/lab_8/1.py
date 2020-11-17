word = input().split('h')
print(*list(map(lambda x: x[:: -1], word[1: -1])), sep='h')
