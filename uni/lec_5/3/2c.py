n = input()
outp = False

for i in range(len(n)):
    for k in range(i):
        if n[i] == n[k]:
            outp = True

print(outp)
