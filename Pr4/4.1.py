num =  list(map(int,input('Введите целые числа ').split()))
sum = 0
for i in range(0,len(num),2):
    sum += num[i]

sum *=num[-1]

print(sum)    

