import Task.PRACTIC.number_3.makeRecord as rec


import random

print("Слова взяты из файла Words.txt")
list_of_all_words = 0
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
    list_of_all_words = []
    for i in range(0, len(lst)):
        list_of_all_words.append(i)
    random_word = int(random.choice(list_of_all_words))
    guess_this_words = list(lst[random_word])
    for i in guess_this_words:
        lstHid.append('\u25A0')
    print("DEBUG !!!!", guess_this_words, "DEBUG !!!!")
    life = live
    while life > 0:
        print(lstHid, "❤ = ", life)
        inpud = input("Назовите букву или все слово: ")
        counter = 0
        for i in guess_this_words:
            if inpud == i:
                lstHid[counter] = str(inpud)
                life += 1
            counter += 1
        life -= 1
        if str(inpud) == str(lst[random_word]):
            print("\n⭐⭐⭐ ПОБЕДА!! Все сразу угадали ⭐⭐⭐")
            currentRecord += 1
            print(rec.record(currentRecord),"\n")
            lst.pop(random_word)
            break
        if '\u25A0' not in lstHid:
            print("\n ⭐⭐⭐ ПОБЕДА!! Угадали. Не осталось неизвестных ⭐⭐⭐")
            currentRecord += 1
            print(rec.record(currentRecord),"\n")
            lst.pop(random_word)
            break
    game_over = input("Напишите что угодно для продолжения, или напишите 'нет' для остановки ")
    if game_over == "нет":
        lst = []
print("\n КОНЕЦ")

