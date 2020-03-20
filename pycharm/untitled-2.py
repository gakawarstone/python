a = int(input())
b = int(input())
find = False
d = 1

while find != True:
    if d % a == 0 and d % b == 0:
        find = True
        break
    d += 1

print(d)