# Средствами языка Python сформировать два текстовых файла (.txt),
# содержащих по одной последовательности из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Содержимое первого файла:
# Четные элементы:
# Количество четных элементов:
# Среднее арифметическое:
# Содержимое второго файла:
# Нечетные элементы:
# Количество нечетных элементов:
# Сумма положительных элементов:

list1 = ['-18 14 32 -3 50 -7 11 77']
f1 = open('data_1.txt','w')
f1.writelines(list1)
f1.close()

list2 = ['22 -4 99 -42 -1 2 17 60']
f2 = open('data_2.txt','w')
f2.writelines(list2)
f2.close()

f1 = open('data_1.txt')
row1 = f1.read()
arr1 = row1.split()
for i in range(len(arr1)):
    arr1[i] = int(arr1[i])
f1.close()

f2 = open('data_2.txt')
row2 = f2.read()
arr2 = row2.split()
for i in range(len(arr2)):
    arr2[i] = int(arr2[i])
f2.close()

f1 = open('data_1.txt')
sum, count = 0, 0
chet_list = []
for i in arr1:
    sum += i
    count += 1
    if i % 2 == 0:
        chet_list.append(i)
f1.close()

f2 = open('data_2.txt')
plus_sum = 0
nechet_list = []
for i in arr2:
    if i > 0:
        plus_sum += i
    if i % 2 != 0:
        nechet_list.append(i)
f2.close()

f3 = open('data_3.txt','w',encoding='UTF-8')
f3.write('Содержимое первого файла:  ')
f3.writelines(list1)
f3.write('\n')
f3.write('Четные элементы:  ')
f3.writelines((str(chet_list)))
f3.write('\n')
f3.write('Количество четных элементов:  ')
f3.writelines(str(len(chet_list)))
f3.write('\n')
f3.write('Среднее арифметическое:  ')
f3.writelines(str(sum/count))
f3.write('\n')
f3.write('Содержимое второго файла:  ')
f3.writelines(list2)
f3.write('\n')
f3.write('Нечетные элементы:  ')
f3.writelines((str(nechet_list)))
f3.write('\n')
f3.write('Количество нечетных элементов:  ')
f3.writelines(str(len(nechet_list)))
f3.write('\n')
f3.write('Сумма положительных элементов:  ')
f3.writelines(str(plus_sum))
f3.close()



