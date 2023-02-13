# Задача 26: 
# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def deg(A, B):


    if B == 1:
        return A
    return A * deg(A, B - 1)

number1 = int(input('Введите число A: '))
number2 = int(input('Введите число B: '))
print(deg(number1, number2))