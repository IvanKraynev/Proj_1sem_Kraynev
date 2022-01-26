# Из предложенного текстового файла (text18-22.txt) вывести на экран его содержимое, количество букв в верхнем регистре.
# Сформировать новый файл,
# в который поместить текст в стихотворной форме предварительно заменив символы третей строки их числовыми кодами.
for i in open('text18-22.txt', encoding='UTF-8'):
    print(i, end='')
def count_upper():
    capital_letters = 0
    for i in open('text18-22.txt', encoding='UTF-8'):
        for j in i:
            if j.isupper():
                capital_letters += 1
    print(end='\n')
    print('Количество букву в верхнем регистре:  ', capital_letters)
count_upper()

count = 0
f1 = open('data_4.txt','w',encoding='UTF-8')
for i in open('text18-22.txt', encoding='UTF-8'):
    count += 1
    if count == 3:
        for k in i:
            f1.write(str(ord(k)))
        f1.write('\n')
    else:
        f1.write(i)
f1.close()
