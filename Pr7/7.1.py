"""
Дано: натуральное число N.

Задание: написать функцию, которая возвращает список всех цифр этого числа в обратном порядке.

Пример:

 123, результат: [3, 2, 1]

"""
def revers_num(num):
    
    return num[::-1]

num = input("Введите число ")
print(revers_num(num))
