"""
Задача 19. 
Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
"""

my_list=[i for i in range(10)]
k = int(input('Введите число k: '))
print(my_list)

for _ in range(k):
    my_list.insert(0, my_list.pop())

"""ВАРИАНТ 2.
n=len(my_list)
new_my_list=my_list[-k:]+my_list[:-k]
print(new_my_list)
"""

print(my_list)
