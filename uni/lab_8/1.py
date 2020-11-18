word = list(map(lambda x: x[:: -1], input().split('h')[1: -1]))
word.reverse()
print(*word, sep='h')
