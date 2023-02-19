"""
1. Случайности не случайны.
Дано: n - целое число.
Задание: написать функцию-генератор, которая возвращает n дробных чисел из диапазона [0, n].
Используйте функцию random.uniform для генерации случайных чисел.
Пример:
 list(f(3)), результат: [0.460552766096591, 2.6440795402868016, 0.3830553232366699]
"""
import random


def random_num(count_num):
    for i in range(1, count_num + 1, 1):
        yield random.uniform(0, 5)


count_num = int(input("Введите количество сгенерированых чисел "))
result = list(random_num(count_num))
print(result)