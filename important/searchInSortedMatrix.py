matrix = [[-1, 3]]
key = 3
j = len(matrix[0]) - 1
i = 0
while (i < len(matrix) and j >= 0):
    print('i = ', i)
    print('j = ', j)
    print(matrix[i][j])
    if matrix[i][j] == key:
        print('found at index', i, j)
        break
    elif matrix[i][j] > key:
        j -= 1
    else:
        i += 1
