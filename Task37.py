"""
Задача 37. 
Дано натуральное число N и последовательность из N элементов. 
Требуется вывести эту последовательность в обратном порядке. 
Примечание. В программе запрещается объявлять списки и использовать циклы (даже для ввода и вывода). 
Input:    2 -> 3 4 Output: 4 3
"""

def list_of_numbers(num:int):
    if num == 1:
        return num
    else:
        return f"{num} {list_of_numbers(num-1)}"
        
num=int(input("Введите число: "))    
print(list_of_numbers(num))