"""
Задача 10.
На столе лежат n монеток. Некоторые из них лежах вверх решкой, а некоторые - гербом.
Определите минимальное число монеток, которое нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которое нужно перевернуть.
"""
import random

number = int(input('Введите число монеток: '))

i=1
quantity_heads=0
quantity_tails=0

while i <= number:
    element = random.randint(0,1)
    print(element, end=" ")
    if element==0:
        quantity_heads+=1
    else:
        quantity_tails+=1
    i+=1

print()
print(quantity_heads if quantity_tails>=quantity_heads else quantity_tails)

