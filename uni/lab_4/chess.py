pos_1 = [int(input()) for i in range(2)]
pos_2 = [int(input()) for i in range(2)]
s = ((pos_2[0] - pos_1[0]) ** 2 + (pos_2[0] - pos_1[0]) ** 2) ** 0.5
if s < 2:
    print("YES")
else:
    print("NO")
