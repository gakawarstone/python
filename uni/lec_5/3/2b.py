n = input()
outp = False
i = 0

while i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        outp = True
    i += 1

print(outp)
