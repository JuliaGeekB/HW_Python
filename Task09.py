"""
Задача 9.
По данному целому неотрицательному n вычислите значение n!. N!=1*2*3*...N
0!=1. 
"""

number = int(input('Введите число: '))

fact=1
i=1
    
while i <= number:
    fact *=i
    i += 1
    
print(fact)


"""
for i in range(1, number+1):
    fact*=i
"""