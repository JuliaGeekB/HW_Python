"""
Задача 11.
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1. 
Input:     5 
Output:  61
"""

number=int(input('Введите число: '))
first=0
second=1
index=1
while second<number:
    first, second=second, first+second
    index+=1
print(index if second==number else-1)