from tokenize import Double


a = int(input("Введите чило a:"))
b = int(input("Введите число b:"))
arg1 = a%b
arg2 = a//b # не стал приводить к float, т.к. целочисленное деление
print(f"Остаток от деления = {arg1} \n Целочисленное деление = {arg2}")


