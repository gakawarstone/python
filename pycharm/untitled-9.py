numbers = [int(i) for i in input().split(' ')]
output = []
i = 0


for number in numbers:
    if len(numbers) == 1:
        output.append(numbers[i])
        break
    if i >= len(numbers) - 1:
        break
    output.append(numbers[i - 1] + numbers[i + 1])
    i += 1


if len(numbers) != 1:
    output.append(numbers[0] + numbers[i - 1])


print(*output, end='\n')
