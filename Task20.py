"""
Задача 20.  В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; 
D, G – 2 очка; 
B, C, M, P – 3 очка; 
F, H, V, W, Y – 4 очка; 
K – 5 очков; 
J, X – 8 очков; 
Q, Z – 10 очков. 
А русские буквы оцениваются так: 
А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
Д, К, Л, М, П, У – 2 очка; 
Б, Г, Ё, Ь, Я – 3 очка; 
Й, Ы – 4 очка; 
Ж, З, Х, Ц, Ч – 5 очков; 
Ш, Э, Ю – 8 очков; 
Ф, Щ, Ъ – 10 очков. 
Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
"""
n=int(input('Введите количество букв в слове: '))
list_word=list()
for z in range (0, n):
    word=input('Введите слово на русском/английском языке (по буквам): ')
    list_word.append(word)

tuple_1point=('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', "В", "Е", "И", "Н", "О", "Р", "С", "Т")
tuple_2point=('D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У')
tuple_3point=('B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', "Я")
tuple_4point=('F', 'H', 'V', 'W', 'Y', 'Й', 'Ы')
tuple_5point=('K', 'Ж', 'З', 'Х', 'Ц', 'Ч')
tuple_8point=('J', 'X', 'Ш', 'Э', 'Ю')
tuple_10point=('Q','Z','Ф','Щ','Ъ')

count=0
for i in range (0, len(list_word)):
    for j in range (0, len(tuple_1point)):
        if list_word[i]==tuple_1point[j]:
            count+=1
    for j in range (0, len(tuple_2point)):
        if list_word[i]==tuple_2point[j]:
            count+=2
    for j in range (0, len(tuple_3point)):
        if list_word[i]==tuple_3point[j]:
            count+=3
    for j in range (0, len(tuple_4point)):
        if list_word[i]==tuple_4point[j]:
            count+=4
    for j in range (0, len(tuple_5point)):
        if list_word[i]==tuple_5point[j]:
            count+=5
    for j in range (0, len(tuple_8point)):
        if list_word[i]==tuple_8point[j]:
            count+=8
    for j in range (0, len(tuple_10point)):
        if list_word[i]==tuple_10point[j]:
            count+=10

print(count)
