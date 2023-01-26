"""
6. Самый большой прямоугольник.
Дано: список высот всех столбцов в гистограмме (список целых чисел)
Задание: У вас есть гистограмма. Попробуйте найти размер самого большого прямоугольника, который можно построить из столбцов гистограммы. Пример.
Примеры:
    largest_histogram([5]) == 5
    largest_histogram([5, 3]) == 6
    largest_histogram([1, 1, 4, 1]) == 4
    largest_histogram([1, 1, 3, 1]) == 4
    largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8
"""
num = input("Введите высоту гистограммы ").split()
len_num = len(num)
height = []
size = 0
minnum = 1
for i in range(1, len_num, 1):
    if int(num[i - 1]) <= int(num[i]):
        size += 1
        minnum = int(num[i - 1])
    else:
        result = int(num[i - 1]) * size
        #result = minnum * size
        height.append(result)
        size = 1

print(height)