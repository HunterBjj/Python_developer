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


def square(int_num):  # К сожалению, не обошлось без большой вложенности в данной функции
    int_num.append(0)
    result_n = []
    len_num = len(int_num)
    for i in range(len_num):
        size = 1
        for g in range(i + 1, len_num, 1):
            if int_num[i] <= int_num[g]:
                size += 1
            else:
                if int_num[i] < int_num[i - 1]:
                    size += 1
                result_next = int_num[i] * size
                result_n.append(result_next)
                break
    max_sq = max(result_n)
    return max_sq


num = input("Введите высоту гистограммы ").split()
int_num = list(map(int, num))
max_square = square(int_num)
print(f' {num} max square: {max_square} ')
