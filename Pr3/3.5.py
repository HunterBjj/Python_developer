
j=0
txt = input("Введите текст ")
x = txt.split()
for i in range(3):
    if x[i].isdigit() == False: # isdigit() -> если все числа ,то возвращает TRUE
     j+=1

if(j==3):
 print(' результат: True')
else:
    print(' результат: False')
 
 