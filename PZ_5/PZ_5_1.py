# Найти сумму чисел ряда 1,2,3,...,60 c использованием функции нахождения суммы.
# Использовать локальные переменные.

def summa():
    res = 0                                             # Переменная для хранения суммы чисел.
    sum1 = 0                                            # счетчик цикла
    while sum1 < 60:
        sum1 += 1
        res += sum1
    print(res)
summa()
