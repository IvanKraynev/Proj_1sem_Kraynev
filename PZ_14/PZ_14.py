# Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые маски» перенести в первый файл строки с
# нулевым четвертым октетом, а во второй – все остальные. Посчитать количество полученных строк в каждом файле.

import re

f = open('ip_address.txt', 'r', encoding='UTF-8')
file = f.read()

f1 = open('text1.txt', 'w', encoding='UTF-8')
p = re.compile(r"\d{3}\.\d{3}\.\d{3}\.0")
if p.findall(file):
    mask1 = p.findall(file)
    len_mask1 = len(mask1)
    print('Cтроки с нулевым четвертым октетом: ', len_mask1)
    print(mask1)
for i in mask1:
    f1.write(i)
    f1.write('\n')
f1.close()

f2 = open('text2.txt', 'w', encoding='UTF-8')
p = re.compile(r"\d{3}\.\d{3}\.\d{3}\.\d{3}")
if p.findall(file):
    mask2 = p.findall(file)
    del(mask2[-1])
    len_mask2 = len(mask2)
    print('Cтроки не с нулевым четвертым октетом: ', len_mask2)
    print(mask2)
for i in mask2:
    f2.write(i)
    f2.write('\n')
f2.close()
f.close()
