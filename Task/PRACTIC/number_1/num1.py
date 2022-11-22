import random

# Проверяем, увеличится шанс при принятии предложения ведущего перевыбрать дверь (переменная swap)

counter_esli0 = 0
counter_esli1 = 0
total = 100000
swap = int(input('Если хотим всегда изменять выбранную дверь, пишем 1. В ином случае пишем 0: '))
while total != 0:
    behind_door_list = [0, 1, 0]
    selected_door = random.choice(behind_door_list)
    behind_door_list = [0, 1]
    if selected_door == 0:
        if swap == 1:
            counter_esli1 += 1
        else:
            counter_esli0 += 1
    elif selected_door == 1:
        if swap == 1:
            counter_esli0 += 1
        else:
            counter_esli1 += 1
    total -= 1

print("Изменяем наш выбор = ", swap, " Winrate: ", counter_esli1 / 1000, "Loserate:", counter_esli0 / 1000)
