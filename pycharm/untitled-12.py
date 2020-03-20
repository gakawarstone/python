input = [int(i) for i in input().split(' ')]
numbers = sorted(input)
i = 0
cnt = 0
output = []
cnt_add = 0

for number in numbers:
    if i >= len(numbers) - 1:
        break
    if numbers[i] == numbers[i + 1]:
        cnt = numbers.count(numbers[i])
        for j in range(cnt):
            output.append(numbers[i])
        i += cnt - 1
        cnt = 0
    i += 1


print(*output, end='\n')
