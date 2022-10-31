

n1 = int(input("Введите целое число "))
n2 = 0 # revers


while n1 > 0:
   
        
    
    digit = n1 %10
    n1 = n1 // 10 # убираем последнее число
    n2 = n2*10 # увеличели разрядность
    n2 += digit #добавляем число


if n1 > 2147483647:
    
        print(f"{n1}->0")
    
    
elif n1 & n2 >= 0:
    print(f"+{n2}")
else:
    print(f"-{n2}")

