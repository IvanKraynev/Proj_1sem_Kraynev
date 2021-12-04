# Дан список размера N и целые числа K и L (1 < K ≤ L ≤ N).
# Найти среднее арифметическое всех элементов списка, кроме элементов с номерами от K до L включительно.

import random

N = int(input('Введите размер списка: '))
K = int(input('Введите целое число: '))                             # K больше 1, но меньше или равно L.
L = int(input('Введите целое число: '))                             # L больше или равно K, но меньше или равно N.

a = []
s = 0
counter = 0
for i in range(N):
    a.append(random.randint(1, 10))
print(a)
for i in range (len(a)):
    if (i >= K - 1) and (i <= L - 1):               # Проверяются числа на отсутствие в радиусе от K до L включительно.
        continue
    else:
        s += a[i]
        counter += 1
print(s)
print(counter)
print(s/counter)



