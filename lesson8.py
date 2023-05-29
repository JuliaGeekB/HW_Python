"""
Задача 49. 
Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Открывать файл
2. Сохранять файл
3. Показать все контакты
4. Добавить контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выход
"""

path = "phone.txt"

# 1. Открывать файл
def open_file_read(path):
    with open(path,'r') as file:
        main_list=(file.readlines())
        main_list_str=[x.rstrip().split(':') for x in main_list]
    return main_list_str
print(open_file_read('phone.txt'))

# 2. Сохранять файл
# 3-8.Показать, добавлять, искать, изменять, удалять контакты, выход

def main_menu():
    print("\nMain MENU")
    print("1. Показать все контакты")
    print("2. Добавить контакт")
    print("3. Найти контакт")
    print("4. Изменить контакт")
    print("5. Удалить контакт")
    print("6. Выход")
    choice=input("Выберите действие: ")
    if choice=="1":
        main_list=open(path, "r+")
        filecontents=main_list.read()
        if len(filecontents)==0:
            print("Нет контактов")
        else:
            print(filecontents)
            main_list.close
            main_menu()
    elif choice=="2":
        newcontact()
        main_menu()
    elif choice=="3":
        searchcontact()
        main_menu()
    elif choice=="4":
        editcontact()
        main_menu()
    elif choice=="5":
        deletecontact()
        main_menu()
    elif choice=="6":
        print("До новой встречи!")

        
def newcontact():
    firstname=input("Введите имя: ")
    lastname=input("Введите фамилию: ")
    phoneNum=input("Введите номер телефона: ")
    contactDetails=(lastname+':'+firstname+':'+phoneNum)
    main_list=open(path, 'a')
    main_list.write("\n")
    main_list.write(contactDetails)
    print("Контакт\n" +contactDetails + "\nдобавлен")

def searchcontact():
    searchname=input("Введите имя: ")
    main_list=open(path,'r+')
    filecontents=main_list.readlines()
    found=False
    for line in filecontents:
        if searchname in line:
            print("Найден контакт: ", end=' ')
            print(line)
            found=True
            break
    if found==False:
        print("Контакт не найден")

def editcontact():
    contact_list=read_file_to_list(path)
    contact_to_edit=search_to_modify(contact_list)
    contact_list.remove(contact_to_edit)
    print("Введите номер поля, которое надо изменить: ")
    choice=input("1-Фамилия\n2-Имя\n3-Номер телефона")
    if choice=="1":
        contact_to_edit[0]=input("Введите фамилию: ")
    elif choice=="2":
        contact_to_edit[1]=input("Введите имя: ")
    elif choice=="3":
        contact_to_edit[2]=input("Введите номер телефона: ")
    contact_list.append(contact_to_edit)
    with open(path, 'w', encoding='utf-8') as file:
        for x in contact_list:
            line=' '.join(x)+'\n'
            file.write(line)
    
            
def deletecontact():
    contact_list=read_file_to_list(path)
    contact_to_delete=search_to_modify(contact_list)
    contact_list.remove(contact_to_delete)
    with open(path, 'w') as file:
        for x in contact_list:
            line=' '.join(x)+'\n'
            file.write(line)

def search_to_modify(main_list: list):
    search_field, search_value=search_parameters()
    search_result=[]
    for x in main_list:
        if x[int(search_field)-1]==search_value:
            search_result.append(x)
    if len(search_result)==1:
        return search_result[0]
    elif len(search_result)>1:
        print("Найдено несколько контактов")
    else:
        print("Контакт не найден")
    print()

def search_parameters():
    print("По какому полю выполнить поиск: ")
    search_field=input("1-по фамилии\n2-по имени\n3-по номеру телефона")
    print()
    search_value = None
    if search_field =="1":
        search_value=input("Введите фамилию для поиска: ")
        print()
    if search_field =="2":
        search_value=input("Введите имя для поиска: ")
        print()    
    if search_field =="3":
        search_value=input("Введите номер телефона для поиска: ")
        print()
    return search_field, search_value

def read_file_to_list(path):
    with open(path, 'r', encoding='utf-8') as file:
        contact_list=[]
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list


main_menu()
