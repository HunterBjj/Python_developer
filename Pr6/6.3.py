"""
Дано: n.

Задание: нужно получить список "удвоенных" нечетных чисел от 0 до n.

Пример:

 n = 5, результат: [2, 6]

"""
num = input("Введите число ")
int_num = int(num[0])
result = [i*2 for i in range(1,int_num,2)]

print(result)