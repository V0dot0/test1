import random

lst = ["книга","месяц","ручка","шарик","олень","носок"]
lstHid = []
a = [0, 1, 2, 3, 4, 5]
c = int(random.choice(a))
lstWord = list(lst[c])
for i in lstWord:
    lstHid.append('\u25A0')
print ("DEBUG",lstWord)
life = 5
while life > 0 :
    print (lstHid, "life = ",life)
    inpud = input("Назовите букву или все слово: ")
    k = 0
    for i in lstWord:
        if inpud == i:
            lstHid[k] = str(inpud)
            life += 1
        k += 1
    life -= 1

    if '\u25A0' not in lstHid:
        life = -1
        print("ПОБЕДА")
        break
