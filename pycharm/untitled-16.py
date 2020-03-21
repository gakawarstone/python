import copy
matrix = [[]]
matrix_out = [[]]
cnt = 0
i = 0
c = 0
matrix[0] = [int(i) for i in input().split(' ')]

while str != 'end':
    my_input = input()
    if my_input != 'end':
        my_input = [int(x) for x in my_input.split(' ')]
        matrix.append(my_input)
    else:
        break

matrix_out = copy.deepcopy(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if 0 <= i < len(matrix) and 0 <= j - 1 < len(matrix[i]):
            cnt += matrix[i][j - 1]
        else:
            cnt += matrix[i][-1]

        if 0 <= i < len(matrix) and 0 <= j + 1 < len(matrix[i]):
            cnt += matrix[i][j + 1]
        else:
            cnt += matrix[i][0]

        if 0 <= i - 1 < len(matrix) and 0 <= j < len(matrix[i]):
            cnt += matrix[i - 1][j]
        else:
            cnt += matrix[-1][j]

        if 0 <= i + 1 < len(matrix) and 0 <= j < len(matrix[i]):
            cnt += matrix[i + 1][j]
        else:
            cnt += matrix[0][j]

        matrix_out[i][j] = cnt
        cnt = 0

for i in range(len(matrix_out)):
    print(*matrix_out[i])
