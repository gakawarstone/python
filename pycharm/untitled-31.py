x = 101

while True:
    L = x - 30
    M = x + 30
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if L == 10:
        break
    x += 1
print(x)
