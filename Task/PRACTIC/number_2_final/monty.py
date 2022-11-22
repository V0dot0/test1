import random


def monty_hall(iterations: int):
    '''
    Получает количество итераций; и в зависимости от того, хотим ли мы изменить выбор, вывод процент побед
    :param iterations: количество итераций
    :return: шанс победы в процентах
    '''
    total = iterations
    selected_door_0 = 0
    selected_door_1 = 0
    while iterations != 0:
        behind_door_list = [0, 1, 0]
        player_selected_door = random.choice(behind_door_list)
        # swap = 1, мы всегда изменяем выбор при возможности; swap = 0, никогда не изменяем выбор с первоначального
        swap = 1
        if player_selected_door == 0:
            if swap == 1:
                selected_door_1 += 1
            else:
                selected_door_0 += 1
        elif player_selected_door == 1:
            if swap == 1:
                selected_door_0 += 1
            else:
                selected_door_1 += 1
        iterations -= 1
    return ("Monty win chance ", selected_door_1 / (total / 100))
