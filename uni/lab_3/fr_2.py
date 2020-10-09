numbers_bin = [input() for i in range(3)]
numbers = list(map(lambda x: int(x, 2), numbers_bin))
numbers_oct = list(map(oct, numbers))
numbers_hex = list(map(hex, numbers))
print(numbers_oct, numbers, numbers_hex, sep='\n')
