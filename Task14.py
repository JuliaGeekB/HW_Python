"""
Задача 14. 
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

number=int(input('Введите число N: '))

i=0
element=1

while 2**i <= number:
    element = 2**i
    print(element, end=" ")
    i+=1

