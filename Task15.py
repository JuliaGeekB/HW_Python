"""
Задача 15. 
Пользователь вводит одно число N – количество арбузов. 
Вторая строка содержит N чисел, записанных на новой строчке каждое. 
Здесь каждое число – это масса соответствующего арбуза 
Input:5 -> 5 1 6 5 9 
Output:1 9 (минимальное и максимальное)
"""

import random

number=int(input('Введите количество арбузов: '))
min_weight=20
max_weight=1
for i in range (number):
    massa=random.randint(1,20)
    print (massa, end=" ")
    if massa>max_weight:
        max_weight=massa
    elif massa<min_weight:
        min_weight=massa
print(f'\nМаксимальный вес арбуза - {max_weight} и минимальный вес арбуза - {min_weight}')
