import random

life = 3;
count = 0;
while True:
    n1 = random.randint(0, 99)
    n2 = random.randint(0, 99)
    n3 = random.randint(0,1)
    print("-----------")
    print("всего жизней = ", life)
    if n3 == 0:
        n2 = n2*(-1)
        print("|", n1, n2, "=", "??? |")
    else :
        print("|",n1,"+",n2,"=","??? |")
    a = int(input("ваш ответ: "))
    if a == (n1+n2):
        count = count + 1
        print("Правильный ответ.  Текущий рекорд *",count,"*")
        continue
    elif life == 0:
        print("Проиграл. текущий рекорд", count)
        break
    else:
        life = life - 1
        print("ОШИБКА !!! одна жизнь потеряна ")
        continue
