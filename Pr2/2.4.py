 
n1 = int(input("Введите целое число "))
n2 = 0 # revers
n3 = n1
while n1 > 0:
    digit = n1 %10 # end element
    n1 = n1 // 10 # убираем последнее число
    n2 = n2*10 # увеличели разрядность
    n2 += digit #добавляем число

print(n3,n2)
