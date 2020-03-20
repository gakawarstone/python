a = int(input())
b = int(input())
numbers_sum = 0
numbers_quantity = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        numbers_sum += i
        numbers_quantity += 1

print(numbers_sum / numbers_quantity)