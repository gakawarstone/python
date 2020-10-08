numbers = [int(input()) for i in range(3)]
numbers_bin = list(map(bin, numbers))
numbers_oct = list(map(oct, numbers))
numbers_hex = list(map(hex, numbers))
print(numbers_bin, numbers_oct, numbers_hex, sep='\n')
