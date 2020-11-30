n = int(input())
fib = [0, 1, 1]
if n < 0:
    print('ERROR')
    quit()

for i in range(n):
    for k in range(len(str(i ** 2))):
        if int(str(i ** 2)[k:]) == i:
            print(i ** 2)
    if i ** 2 > n:
        break
