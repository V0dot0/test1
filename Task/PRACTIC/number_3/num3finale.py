import Task.PRACTIC.number_3.makeRecord as rec


import random

print("Слова взяты из файла Words.txt")
thisrecord = 0
currentRecord = 0
lst = []
lst = rec.get_words()
print("lst= ",lst)



print(rec.record(currentRecord))
print("Выберите уровень сложности")
live = int(input("3-легко (7 ❤), 2 - средне (5 ❤), 1 - сложно (1 ❤). Любое другое число даст равное вводу ❤. Ваш ввод: "))
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
        print(lstHid, "❤ = ", life)
        inpud = input("Назовите букву или все слово: ")
        k = 0
        for i in lstWord:
            if inpud == i:
                lstHid[k] = str(inpud)
                life += 1
            k += 1
        life -= 1
        if str(inpud) == str(lst[c]):
            print("\n⭐⭐⭐ ПОБЕДА!! Все сразу угадали ⭐⭐⭐")
            currentRecord += 1
            print(rec.record(currentRecord),"\n")
            lst.pop(c)
            break
        if '\u25A0' not in lstHid:
            print("\n ⭐⭐⭐ ПОБЕДА!! Угадали. Не осталось неизвестных ⭐⭐⭐")
            currentRecord += 1
            print(rec.record(currentRecord),"\n")
            lst.pop(c)
            break
    g = input("Напишите что угодно для продолжения, или напишите 'нет' для остановки ")
    if g == "нет":
        lst = []
print("\n КОНЕЦ")

