"""
Дана последовательность чисел длинной  N
Найти первое (левое вхождение положительного числа  Х
в неё или вывести -1, если число Х не встречалось
"""


def findx(seq, x):
    ans = -1
    for i in range(len(seq)):
        if ans == -1 and seq[i] == x:
            ans = i
    return ans


