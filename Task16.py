"""
Задача 16. 
Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
"""
import random

n=int(input("Введите количество элементов в списке: "))
if n<=0: 
    print('Ошибка ввода')
else:
    list_input=[random.randint(1,5) for i in range(n)]
    print(list_input)

    x=int(input("Введите число X: "))
    count=0
    for i in range(0, len(list_input)):
        if list_input[i]==x:
            count+=1
       
    print(f"Число {x} содержится {count} раз(а) в списке" if count !=0 else 'Указанное число не содержится в списке')
