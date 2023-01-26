"""
5. Ленивая функция.
Дано: цело число n
Задание: написать функцию-генератор, которая будет "лениво" возвращать значения от 0 до n,
определенные следующими правилами.
Если
x == 0 -> -10
x % 3 -> 45
x % 5 -> (x / 5) + 93
Иначе
-> x / 2
"""
def foo(arg):
    if arg == 0:
        return -10
    elif arg % 3 == 0 and arg % 5 == 0:
        return 45, (num / 5) + 93
    elif arg % 3 == 0:
        return 45
    elif arg % 5 == 0:
        return (arg / 5) + 93
    else:
        return arg / 2


num = int(input("Введите число "))
stop = num + 1
result = [foo(i) for i in range(stop)]
print(result)
