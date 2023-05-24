"""
Дана последовательность чисел N (N > 0)
Найти максимальное число в последовательности
"""

def findmax(seq):
    num = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > num:
            num = seq[i]
    return num