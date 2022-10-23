import random

def monty_hall(total):
    esli0 = 0
    esli1 = 0
    total = 100000
    while total != 0:
        a = [0, 1, 0]
        c = random.choice(a)
        # print (c)
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
    #print("Изменяем наш выбор = ", swap, " Winrate: ", esli1 / 1000, "Loserate:", esli0 / 1000)
    return(format((esli1 / 1000),'.1f'))
def birthday(count):
    not_sharing = 1
    for i in range(1, count):
        probability = i / 365
        not_sharing *= (1 - probability)
        result = 1 - not_sharing
    result = format((result*100), '.1f')
    return (result)

