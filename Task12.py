"""
Задача 12.
Загаданы два натуральных числа X и Y (X,Y<=1000). Дана сумма этих чисел S и их произведение P. 
Вывести числа.
"""
import math

s=int(input("Введите сумму чисел X и Y:  "))
p=int(input("Введите произведение чисел X и Y:  "))

if p>1000000 or p<=0:
    print("Ошибка ввода")
else:
    d=int(s*s-4*p)

    x=int((s+math.sqrt(d))/2)
    y=int((s-math.sqrt(d))/2)

    if x+y==s and x*y==p:
        print(x,  y)
    else:
        print("Ошибка ввода")



