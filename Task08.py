"""
Задача 8. 
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
"""

length=int(input('Введите длину шоколадки: '))
width=int(input('Введите ширину шоколадки: '))
units=int(input('Введите количество отломленных долек: '))

if units==length*width or units>length*width:
    print("Ошибка ввода")
else:
    if units%width ==0 or units%length ==0:
        print("Yes")
    else:
        print("No")