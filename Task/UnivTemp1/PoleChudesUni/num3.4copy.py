def get_words():
    lst = open('Words.txt')
    word_list = lst.read().splitlines()
    word_list = [i.upper() for i in word_list]
    print(word_list)
    return lst

def record(thisrecord):
    #a = int(input())
    #b = 3 #prev record
    new_text = open("Record.txt", mode='r+')
    #if thisrecord > b:
    #    b = thisrecord
    new_text.seek(0)
    print(new_text.read())
    new_text.seek(0)
    #new_text.write(str(b))
    #return b


import random

print("Слова взяты из файла Words.txt\n")
thisrecord = 0
lst = []
get_words()

doReset = 0

lst = ["книга","месяц","ручка","шарик","олень","носок"]

print("Выберите уровень сложности")
live = int(input("3-легко (7 жизней), 2 - средне (5 жизней), 1 - сложно (1 жизнь). Любое другое число даст такое же количество жизней. Ваш ввод: "))
if live == 1:
    live = 7
elif live == 2:
    live = 5
elif live == 3:
    live = 3
while len(lst) != 0:
    print("\nОсталось слов \n", len(lst))
    lstHid = []
    thisrecord = []
    for i in range(0, len(lst)):
        thisrecord.append(i)
    c = int(random.choice(thisrecord))
    lstWord = list(lst[c])
    for i in lstWord:
        lstHid.append('\u25A0')
    print("DEBUG !!!!", lstWord, "DEBUG !!!!")
    life = live
    while life > 0:
        print(lstHid, "life = ", life)
        inpud = input("Назовите букву или все слово: ")
        k = 0
        for i in lstWord:
            if inpud == i:
                lstHid[k] = str(inpud)
                life += 1
            k += 1
        life -= 1
        if str(inpud) == str(lst[c]):
            print("ПОБЕДА все слово")
            print(record())
            lst.pop(c)
            break
        if '\u25A0' not in lstHid:
            print("ПОБЕДА не осталось неизвестных")
            lst.pop(c)
            break
    g = input("Напишите что угодно для продолжения, или напишите 'нет' для остановки ")
    if g == "нет":
        lst = []
print("\n КОНЕЦ")

