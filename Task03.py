"""
Задача 3. 
В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
Выведите наименьшее число парт, которое нужно приобрести для них.
"""

a=int(input('Введите количество учеников в 1 классе: '))
b=int(input('Введите количество учеников во 2 классе: '))
c=int(input('Введите количество учеников в 3 классе: '))

x1=int((a+1)//2)
x2=int((b+1)//2)
x3=int((c+1)//2)

print(x1+x2+x3)