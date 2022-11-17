num = input('Введите целые числа ').split()

for i in range(len(num)):
    num[i] = int(num[i])
sorter = sorted(num)
lenf = len(num)

if(lenf % 2 != 0):
    print(sorter[int((lenf / 2) + 0.5) - 1])
else:
    result = (sorter[int(((lenf) / 2) - 1)] + sorter[int((lenf) / 2)]) / 2
    print(result)

