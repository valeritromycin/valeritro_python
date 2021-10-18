matrix_1 = [
    [1, 2, 3],
    [11, 22, 33]
]

matrix_2 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

matrix = [[0 for row in range(len(matrix_1))] for col in range(len(matrix_2[0]))]
for i in range(len(matrix_1)):
    for j in range(len(matrix_2[0])):
        for k in range(len(matrix_2)):
            matrix[i][j] += matrix_1[i][k]*matrix_2[k][j]

print(matrix)