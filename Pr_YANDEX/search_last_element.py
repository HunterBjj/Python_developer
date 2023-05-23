"""

Дана последовательность чисел длинной N
Найти последнее (правое) вхождение числа X
в неё или вывести -1, если число Х не встречалось
"""

def last_element(seq, num):
    arg = -1
    for i in range(len(seq)):
        if num == seq[i]:
            arg = i
    return i
