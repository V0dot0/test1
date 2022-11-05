import random

doReset = 0
lst = ["книга","месяц","ручка","шарик","олень","носок"]
while len(lst) != 0:
    print("\nОсталось слов \n", len(lst))
    lstHid = []
    a = []
    for i in range(0, len(lst)):
        a.append(i)
    c = int(random.choice(a))
    lstWord = list(lst[c])
    for i in lstWord:
        lstHid.append('\u25A0')
    print("DEBUG !!!!", lstWord, "DEBUG !!!!")
    life = 5
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

