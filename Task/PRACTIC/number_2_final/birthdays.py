import random


def find_chance(group: int, iterations: int):
    '''
    Получает количество студентов в группе и количество итераций; считает совпадение дней рождений студентов в группе;
    возвращает процент совпадений дней рождений в зависимости от количества студентов в группе и количество проверок
    :param group: Количество студентов
    :param iterations: Количество проверок
    :return: Процент совпадания дней рождения
    '''
    number_of_iterations = iterations
    count_yes = 0
    count_no = 0
    while iterations != 0:
        was_match = "No"
        birthdays_list = [random.randint(1, 365) for i in range(group)]
        for i in range(0, len(birthdays_list)):
            if i != birthdays_list.index(birthdays_list[i]):
                was_match = "Yes"
        if was_match == "Yes":
            count_yes += 1
        else:
            count_no += 1
        iterations -= 1
    return ("День рождения совпадают в", count_yes / (number_of_iterations / 100), "% случаев", "а не совпадают",
            count_no / (number_of_iterations / 100), "% случаев")
