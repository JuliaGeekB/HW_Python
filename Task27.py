"""
Задача 27.
Пользователь вводит текст. Словом считается последовательность непробельных символов, идущих подряд.
Определить сколько раздельных слов содержится. 
"""

import string

my_string= "Вот моя деревня. Вот мой дом родной. Вот качу я в санках по горе крутой. Вот свернулись санки и я на бок - хлоп.".lower()
for ch in string.punctuation:
    my_string=my_string.replace(ch, ' ')
text=set(my_string.split())
print(len(text))