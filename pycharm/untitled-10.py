numbers = [int(i) for i in input().split(' ')]
output = []
i = 0
cnt = 0
check = False

for number in sorted(numbers):
#    if sorted(numbers)[i] != sorted(numbers)[i + 1]:
#        i += 1
    if i >= len(numbers) - 1:
        break
#    if i == len(numbers) - 1:
#        if sorted(numbers)[i] == sorted(numbers)[i - 1]:
#            cnt += 1
#            check = True
    if sorted(numbers)[i] == sorted(numbers)[i + 1] and not check:
        cnt += 1
    elif cnt > 1:
        for c in range(cnt):
            output.append(sorted(numbers)[i])
    i += 1

#output.append(sorted(numbers)[i])

print(*output, end='\n')
