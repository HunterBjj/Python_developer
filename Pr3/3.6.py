
from turtle import left


txt = input("Введите текст ")
x = txt.split()
i = 0
while  i < len(x): # ,цикл бесконечен, пока не дойдём до конца списка
    if(x[i]=='right'):
        x[i]='left'
    elif(x[i]=='bright'):
        x[i]='bleft'
    elif(x[i]=='aright'):
        x[i]='aleft'
    i+=1    
print(x)
 
 