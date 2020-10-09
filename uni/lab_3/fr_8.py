numbers_oct = [input() for i in range(2)]
numbers = list(map(lambda x: int(x, 8), numbers_oct))
print(sum(numbers))
numbers_plus = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
numbers_minus = [-numbers[i] for i in range(len(numbers)) if i % 2 == 1]
print(sum(numbers_plus) + sum(numbers_minus))
