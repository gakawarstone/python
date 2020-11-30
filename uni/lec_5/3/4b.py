a = 15
b = 17
c = 21
cnt = 0

for i in range(185 // 15 + 1):
    for j in range(185 // 17 + 1):
        for k in range(185 // 21 + 1):
            if i * a + j * b + k * c == 185:
                cnt += 1

print(cnt)
