def conNS(x, si1, si2):
    b = ''
    b += str(x % si2)
    while x >= si2:  # Пока не закончится остаток
        x = x//si2
        b += str(x % si2)
    return b[::-1]
print(conNS(10, 10, 8))
