"""
Задача 33. 
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные. 
Input: 5 -> 1 3 3 3 4 
Output: 1 3 3 3 1
"""

import random

n=int(input("Введите количество оценок: "))
list_input=[random.randint(1,5) for i in range(n)]
print(list_input)

max_point=max(list_input)
min_point=min(list_input)

for i in range (n):
    if list_input[i]==max_point:
        list_input[i]=min_point

print(list_input)