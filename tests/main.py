letters = ('A', 'B', 'C', 'D', 'E', ' B', ' C', ' D', ' E')
outp = []

with open("in.txt") as file:
    for line in file:
        if not line.startswith(letters):
            outp.append(line)


toWrite = []

for line in outp:
    try:
        num = int(line.split('.')[0])
        num -= 25 * 8
        q = ' '
        for el in line.split('.')[1:]:
            q += str(el)
        toWrite.append(str(num) + q)
    except Exception:
        toWrite.append(line)


with open("outp.txt", 'w') as file:
    for line in toWrite:
        file.write(line)
