"""
Задача 28. 
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
"""

def sum_of_numbers(num1,num2):
    if num2 == 0:
        return 0
    else:
        return num1+1+sum_of_numbers(0,num2-1) 
        
num1=int(input("Введите число: "))
num2=int(input("Введите число: ")) 
print(sum_of_numbers(num1,num2))