# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3?)
# A = 2; B = 3 -> 8 

num = int(input('Введите число возводимое в степень: '))
exp = int(input('Введите степенное число: '))
def Expo(num, exp):
    res = 0
    if exp == 1:
        return num
    else:
        return num*Expo(num, exp - 1)
print(Expo(num,exp))