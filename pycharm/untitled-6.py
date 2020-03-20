genome = input()
cnt = 0
for c in genome:
    if c == 'g' or c == 'c':
        cnt += 1
    if c == 'G' or c == 'C':
        cnt += 1

print((cnt / len(genome)) * 100)
