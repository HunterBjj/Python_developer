
num = int(input("Введите целое число "))
if(num%2!=0):
    print('Плохо')
elif(num>=2 and num<=5 and num%2==0):
    print("Неплохо")
elif(num>=6 and num <=20 and num%2 ==0):
    print("Так себе")
elif(num>20 and num %2==0):
    print("Отлично")
