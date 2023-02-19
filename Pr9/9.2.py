"""
2. Ленивое объединение
Дано: 2 списка произвольной длины.
Задание: написать функцию, которая возвращает результат объединения этих списков. Используйте функцию itertools.chain.
Пример:
list(f([1, 2], [3, 4])), результат: [1, 2, 3, 4]
"""
from itertools import chain


def union_num(num1, num2):
    result = list(chain(num1, num2)) #Создаёт итератор представляющий единой цепочкой элементы указанных объектов.
    return result


num1 = input("Enter number1 ").split()
int_num1 = list(map(int, num1))
num2 = input("Enter number2 ").split()
int_num2 = list(map(int, num2))
res = union_num(int_num1, int_num2)

print(res)