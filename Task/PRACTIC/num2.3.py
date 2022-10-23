import num2_3paradox

total = 100000

while total !=0:
    a = [0, 1, 0]
    c = random.choice(a)
    #print (c)
    a = [0, 1]
    # изменяем наш выбор это 1, не изменяем 0
    swap = 1
    # заменить для проверки
    if c == 0:
        if swap == 1:
            esli1 += 1
        else:
            esli0 += 1
    elif c == 1:
        if swap == 1:
            esli0 += 1
        else:
            esli1 += 1
    total -= 1

print("Изменяем наш выбор = ", swap, " Winrate: ", esli1/1000, "Loserate:", esli0/1000)
