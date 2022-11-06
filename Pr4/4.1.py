num =  list(map(int,input('Введите целые числа ').split()))
sum = 0
for i in range(0,len(num),2):
    sum += num[i]
    if num[i]==num[-1]:
        sum*=num[i]
        break
    elif num[i+1] == num[-1]: # проверка на последний элемент ,если перепрыгнули в пустоту
        sum*=num[-1]
        break



print(sum)    

