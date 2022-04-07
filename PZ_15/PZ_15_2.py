# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.

import random
def func1(list):
    flag = 0
    sum = 0
    for i in list:
        flag += 1
        sum += i
    res = sum/flag
    return res
rows = int(input('Введите количество строк: '))
columns = int(input('Введите количество столбцов: '))
matrix = [[random.randint(1, 10) for y in range(rows)] for x in range(columns)]
for i in matrix:
    print(i)


arr = []
for i in range(len(matrix)):
        if i % 2 != 0:
            arr.append(matrix[i])
print(arr, "\n")
for i in arr:
    print(func1(i))