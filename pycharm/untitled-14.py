input = int(input())
output = []
n = 1
cnt = 0

while cnt <= input - 1:
    for j in range(n):
        output.append(n)
        cnt += 1
        if cnt >= input:
            break
    n += 1

print(*output)
