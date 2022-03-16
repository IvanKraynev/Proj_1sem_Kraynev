# Даны текущие оценки студента по дисциплине «Основы программирования» за месяц.
# Необходимо найти количество «2», «3», «4» и «5», полученных студентом, и определить итоговую оценку за месяц.

from functools import reduce

marks = [4, 2, 4, 5, 2, 3, 4, 5, 4]
sum = reduce(lambda x,y: y+x, marks)
print('Итоговая оценка за месяц: ', sum//len(marks))
kolvo_marks = {}
for i in marks:
 if i not in kolvo_marks:
     kolvo_marks[i] = 1
 else:
    kolvo_marks[i] += 1
print ('Количество «2», «3», «4» и «5»: ', kolvo_marks)
