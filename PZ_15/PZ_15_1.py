# В матрице найти минимальный элемент в предпоследнем столбце.

import random

rows = int(input('Введите количество строк: '))
columns = int(input('Введите количество столбцов: '))
matrix = [[random.randint(1, 10) for y in range(rows)] for x in range(columns)]
for i in matrix:
    print(i)

n = rows-2
for i in range(len(matrix)):
    matrix[i][n]
arr = [matrix[i][n] for i in range(len(matrix))]
print('Минимальный элемент в предпоследнем столбце', min(arr))