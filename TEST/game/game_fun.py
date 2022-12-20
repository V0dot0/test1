import random
import datetime
import re

def record(currentRecord: int):
    record_in_file: TextIOWrapper = open("Record.txt", mode='r+')
    max_record: int = int(record_in_file.read())
    if currentRecord > max_record:
        max_record: int = currentRecord
    record_in_file.seek(0)
    record_in_file.write(str(max_record))
    print("      Current record:", currentRecord, "=== Max record:", max_record)
    separator: str = "=============================================="
    return separator

def writing(strin: str):
    with open("gamelog.txt", mode="a+", encoding='utf-8') as requested_file:
        time = str(datetime.datetime.today())
        time_pattern = r"(?:^\d+\-\d+\-\d+\s)([^\.]+)"
        match_time = re.findall(time_pattern, time)
        total_time = ''.join(match_time)
        total_row = ["[", total_time, "]", strin]
        row = ''.join(total_row)
        requested_file.write(row)
        requested_file.seek(2)



writing(" Начало игры")
global сurrentRecord
сurrentRecord = 0
while True:
    сurrentRecord = 0
    n = random.randint(0, 2)    # программа выбирает 0 - камень, 1 - ножницы, 2 - бумага
    my_n = int(input("Введите выбранное число (0 - камень, 1 - ножницы, 2 - бумага, -1 - чтобы закончить): "))
    if my_n == 0:
        writing(" Игрок выбрал камень")
    elif my_n == 1:
        writing(" Игрок выбрал ножницы")
    else:
        writing(" Игрок выбрал бумагу")
    if n == 0:
        writing(" Компьютер выбрал камень")
    elif n == 1:
        writing(" Компьютер выбрал ножницы")
    else:
        writing(" Компьютер выбрал бумагу")
    #result_cur_rec = [" Количество очков:", сurrentRecord]
    #writing(result_cur_rec)


    ex = my_n
    if ex == -1:
        break
    result = 0
    print(n)
    print(my_n)
    if n == my_n:
        result = "Ничья"
    if (n == 0 and my_n == 1) or (n == 1 and my_n == 2) or (n == 2 and my_n == 0):
        result = "Поражение"
    else:
        result = "Победа"

    print(result)
    if result == "Победа":
        currentRecord += 1
        record(currentRecord)
    elif result == "Поражение":
        currentRecord = 0
        record(currentRecord)






