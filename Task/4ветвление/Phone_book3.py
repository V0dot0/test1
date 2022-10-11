phone_book = {}
a = 0
key = str
value = 0

def menuSelect(a):
    a = int(input(" 1 Добавить контакт \n 2 Удалить контакт \n 3 Изменить контакт \n 4 просмотреть контакты \n "))
    return a
def name_input(key):
    key = input(" Введите контакт: ")
    key = key.lower()
    key = key.title()
    return key

def num_stand(value):
    value = input(" Введите номер телефона: ")
    value = value.replace("+7", "8")
    value = value.replace(" ", "").replace("-", "")

def num_input(value):
    value = num_stand(value)
    if value.isdigit() != 1:
        print ("again")
    return value

def deletionOf():
    key = "a"
    print(" Введите контакт, который хотите удалить: ")
    key = name_input(key)
    del phone_book[key]

def num_stand(value):
    value = input(" Введите номер телефона: ")
    value = value.replace("+7", "8")
    value = value.replace(" ", "").replace("-", "")




a = menuSelect(a)
while a != 0:
    if a == 1:
        key = name_input(key)
        value = num_input(value)
        phone_book[key] = value

    if a == 2:
        deletionOf()

    if a == 3:
        print(" Введите контакт для изменения: ")
        key = name_input(key)
        del phone_book[key]
        print(" Введите новый номер: ")
        value = num_input(value)
        phone_book[key] = value
    if a == 4:
        print(phone_book)

    a = menuSelect(a)
