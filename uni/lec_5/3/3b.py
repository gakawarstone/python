for i in range(100, 999):
    _str = str(i)
    if int(_str[0]) ** 3 + int(_str[1]) ** 3 + int(_str[2]) ** 3 == i:
        print(i)
