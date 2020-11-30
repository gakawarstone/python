n = int(input())

for i in range(n + 1):
    _cnt = 0
    for k in range(len(str(i))):
        if int(str(i)[k]) != 0:
            if i % int(str(i)[k]) == 0:
                _cnt += 1
    if _cnt == len(str(i)):
        print(i)
