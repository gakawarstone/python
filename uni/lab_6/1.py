(n, b2, b5) = (int(input()) for i in range(3))
g = (b5 / b2) ** (1 / 3)
b1 = b2 / g
s = (b1 * (g ** n - 1)) / (g - 1)
print(s)
