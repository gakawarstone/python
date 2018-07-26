def square(x: int) -> int:
    """squre a number"""
    return x ** 2


for N in range(1, 4):
    print(N, 'squared is', square(N))
