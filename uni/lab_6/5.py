numbers = [int(input()) for i in range(6)]
logic = False

for i in range(len(numbers) - 1):
    if numbers[i] + numbers[i-1] == 8:
        logic = True

print(logic)
