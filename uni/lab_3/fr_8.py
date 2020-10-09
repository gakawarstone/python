numbers_oct = [input() for i in range(2)]
numbers = list(map(lambda x: int(x, 8), numbers_oct))
print(sum(numbers))
numbers[-1] = - numbers[-1]
print(sum(numbers))
