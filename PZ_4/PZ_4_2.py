# Дано число A (>1).
# Вывести наибольшее из целых чисел K, для которых сумма 1 + 1/2 + ... + 1/K будет меньше A, и саму эту сумму.

a = input('Введите целое число: ')

while type(a) != int:                          # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите целое число: ")


k = a
flag = 0
num = 'ошибка'                                 # Выводит при неверном вводе числа.
while k > 1:
    if flag == 0:
        sum = 0
        i = k
        while i > 0:
            sum += 1/i
            i -= 1
        if sum < a:
            num = k
            flag = 1
            print('Сумма = ', sum)
            break
        k -= 1
    else:
        break
print('Число k = ', num)

