"""
Задача 22. 
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
"""
import random
num1=int(input("Введите количество элементов первого множества: "))
num2=int(input("Введите количество элементов второго множества: "))

list_1=[random.randint(1,10) for i in range(num1)]
list_2=[random.randint(1,10) for i in range(num2)]

list_3=set(list_1+list_2)
print(list_1)
print(list_2)
print(list_3)