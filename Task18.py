"""
Задача 18. 
Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
"""

import random
import math

n=int(input("Введите количество элементов в списке: "))
if n<=0: 
    print('Ошибка ввода')
else:
    list_input=[random.randint(1,10) for i in range(n)]
    print(list_input)

    x=int(input("Введите число X: "))
    near=list_input[0]
    for i in range(1, len(list_input)):
        if abs(x-list_input[i])<abs(x-near):
            near=list_input[i]
       
    print(near)

