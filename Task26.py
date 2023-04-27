"""
Задача 26. 
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
"""

def degree_of_number(num, degree):
    if degree == 0:
        return 1
    else:
        return num*degree_of_number(num,degree-1) 
        
num=int(input("Введите число: "))
degree=int(input("Введите число: ")) 
print(degree_of_number(num, degree))