x_start  = int(input())
x_end = int(input())
y_start = int(input())
y_end = int(input())

print(end=' ')
print(end='\t')
for i in range(x_start, x_end + 1):
    print(i, end='\t')
print('\t')
for i in range(y_start, y_end + 1):
    print(i, end='\t')
    for j in range(x_start, x_end + 1):
        print(j * i, end='\t')
    print('\t')