n = int(input())
fib = [0, 1, 1]
if n < 0:
    print('ERROR')
    quit()

while 1:
    if fib[-1] + fib[-2] < n:
        fib.append(fib[-1] + fib[-2])
    else:
        break

print(sum(fib))
