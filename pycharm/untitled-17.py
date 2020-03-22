n = int(input())
output = [[0 for i in range(n)] for i in range(n)]
cnt = 1
i = 0

while cnt < n ** 2:
    for j in range(n - i):
        output[i][j] = cnt
        cnt += 1
    for c in range(n - i - 2):
        output[c + 1][-i - 1] = cnt
        cnt += 1
    for k in range(n - 1 - i, i, -1):
        output[-1 - i][k] = cnt
        cnt += 1
    for l in range(n - i, i + 1, -1):
        output[l][i] = cnt
        cnt += 1
    i += 1


for i in range(len(output)):
    print(*output[i])
