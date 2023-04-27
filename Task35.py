"""
Задача 35. 
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым. 
Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число) 
Input: 5 Output: yes
"""

def is_simple(num:int) -> bool:
    if num in [1,2]:
        return True
    elif num%2==0:
        return False
    else:
        for i in range (3,num//2+1,2):
            if num%i==0:
                return False
    return True
        
num=int(input("Введите число: "))    
print (f"Число {num}"+(" простое" if is_simple(num) else " составное") )