numbs = [int(input()) for i in range(3)]
_cnt = 0
cnt = 0

for i in numbs:
    for j in numbs:
        if i == j:
            _cnt += 1

    if _cnt > cnt:
        cnt = _cnt

    _cnt = 0

if cnt > 1:
    print('similar:', cnt)
else:
    print('no similar')
