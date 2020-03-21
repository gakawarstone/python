my_input = [int(i) for i in input().split(' ')]
output = []
i = 0
cnt = 0
n = int(input())

for number in my_input:
    if my_input[i] == n:
        output.append(i)
        cnt += 1
    i += 1


if cnt != 0:
    print(*output)
else:
    print('Отсутвует')
