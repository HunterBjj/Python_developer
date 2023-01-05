"""
2. Перестановки.
Дано: x, y, z, n.
Задание: нужно получить список всех возможных перестановок чисел x, y, z, где x + y + z != n.
"""
num = input("Введите три числа через пробел").split()
result =  set(["[" + num[i] + ", " + num[j] + ", " + num[k] + "]" for i in range(0,3,1) for j in range(0,3,1) for k in range(0,3,1) ])

print(result)



