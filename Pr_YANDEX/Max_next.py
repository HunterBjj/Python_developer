"""
Дана последовательность чисел длинной N (N > 1)
Найти максимальное число в последовательности и второе по величине число
(такое, которое будет максимальным, если вычеркнуть из последовательности одно максимальное число)
"""


def max_max2(seq):
    max_num = 0
    next_max = 0
    for i in range(len(seq)):
        if seq[i] > max_num:
            next_max = max_num
            max_num = seq[i]
        elif next_max < seq[i]:
            next_max = seq[i]

    return max_num, next_max

