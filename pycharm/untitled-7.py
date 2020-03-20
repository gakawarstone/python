genom = input()
number = 0
i = 0
cnt = 0

for c in genom:
    if i == len(genom) - 1:
        break
    if genom[i] == genom[i + 1]:
        number += 1
    else:
        print(genom[i], number + 1, sep='', end='')
        number = 0
    i += 1

print(genom[i], number + 1, sep='', end='\n')
