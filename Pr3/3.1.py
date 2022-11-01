
num = int(input("Введите целое число "))
if ( num%3 == 0 and num%5 == 0 ):
    print("Fizz Buzz")

elif(num%3==0):
    print('Fizz')
elif(num%5==0):
    print("Buzz")
else:
    print('Число не делится на 3 и 5')