num =  input('Введите целые числа ').split()
for i in range(len(num)):
    num[i] = int(num[i])
sorter = sorted(num, key=abs)

print(sorter)