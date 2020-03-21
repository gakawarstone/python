sum = 0
sqrt_sum = 0
numbers = []
out = False

while True:
    numbers.append(int(input()))
    for number in numbers:
        sum += number
        sqrt_sum += number ** 2
        if sum == 0:
            out = True
            break
    if out:
        break
    sum = 0
    sqrt_sum = 0

print(sqrt_sum)
