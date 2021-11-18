# Даны два числа. Вывести большее из них.

a, b = input("Введите первое число: "), input("Введите второе число: ")

while type(a) != int:                           # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число: ")

while type(b) != int:                           # обработка исключений
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите второе число: ")

if a > b:
    print(a)
else:
    print(b)

