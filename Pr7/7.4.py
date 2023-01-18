"""
[Junior-] 4. Пешки.
Дано: координаты расставленных пешек в виде набора строк.
Вам предоставляется набор координат, в которых расставлены белые пешки. Вы должны подсчитать количество защищенных пешек
"""


def protected_pawn(coordinates):
    res = 0

    for i in range(len_coordinates):
        for g in range(len_result):
                if result[g] == coordinates[i]:
                    if coordinates[i] == 'a3' or coordinates[i] == 'a4' or coordinates[i] == 'a5' or coordinates[i] == 'a6' or coordinates[i] == 'a7':
                        otvet.append(result[g + 6])
                    elif coordinates[i] == 'h3' or coordinates[i] == 'h4' or coordinates[i] == 'h5' or coordinates[i] == 'h6' or coordinates[i] == 'h7':
                        otvet.append(result[g - 8])
                    otvet.append(result[g - 8])
                    otvet.append(result[g + 6])
    len_otvet = len(otvet)
    for k in range(1, len_otvet, 2):
            if coordinates.count(otvet[k]) == True or coordinates.count(otvet[k - 1]) == True:
                res += 1
            else:
                continue
    return res


letter_coordints = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
num_coordints = ['2', '3', '4', '5', '6', '7', '8']
result = [i + g for i in letter_coordints for g in num_coordints] # Генерируем последовательность координат
len_result = len(result)
coordinates = input("Введите координаты ").split()
len_coordinates = len(coordinates)
print(result)
otvet = []
resulult_gurd = protected_pawn(coordinates)
print(f"{coordinates}, результат: {resulult_gurd}")











