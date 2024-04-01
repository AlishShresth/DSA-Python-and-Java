matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
primaryDiagonalSum = 0
secondaryDiagonalSum = 0
j = len(matrix) - 1
for i in range(len(matrix)):
    for k in range(len(matrix[0])):
        print(matrix[i][k], end=" ")
    print()
for i in range(len(matrix)):
    primaryDiagonalSum += matrix[i][i]
    if i != j:
        continue
    secondaryDiagonalSum += matrix[i][j]
    j -= 1
print('Primary diagonal Sum = ', primaryDiagonalSum)
print('Secondary diagonal sum = ', secondaryDiagonalSum)
print('Sum of both diagonals = ', primaryDiagonalSum+secondaryDiagonalSum)
