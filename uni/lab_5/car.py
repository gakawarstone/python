(n, m) = (int(input()) for i in range(2))
if m % n == 0:
    print(m // n)
else:
    print(m // n + 1)
