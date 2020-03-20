input = [int(i) for i in input().split(' ')]
numbers = sorted(input)
i = 0
cnt = 0
output = []
cnt_add = 0

for number in numbers:
    if i >= len(numbers) - 1:
        break
    if numbers[i] != numbers[i + 1] and cnt > 0:
        for j in range(cnt + 1):
            output.append(numbers[i])
            print('cnt')
        cnt = 0
    elif numbers[-1] == numbers[-2]:
        cnt_add = 2
    elif numbers[-1] == numbers[-3]:
        cnt_add = 1
    if numbers[i] == numbers[i + 1]:
        cnt = numbers.count(numbers[i])
    i += 1

for c in range(cnt_add):
    output.append(numbers[-1])
    print('add')

print(*output, end='\n')
