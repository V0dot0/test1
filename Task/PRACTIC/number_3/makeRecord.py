def record(currentRecord: int):
    '''
    Получает текущий рекорд; считывает файл, где хранится максимальный рекорд; если текущий рекорд больше, то
    перезаписывает максимальный рекорд в файле Record.txt
    :param currentRecord: текущий рекорд
    :return: текущий рекорд и максимальный рекорд из файла Record.txt
    '''
    new_text: TextIOWrapper = open("Record.txt", mode='r+')
    found = int(new_text.read())
    if currentRecord > found:
        found = currentRecord

    new_text.seek(0)
    new_text.write(str(found))
    return("текущий рекорд ",currentRecord, "максимальный рекорд ", found)

def get_words():
    '''
    Функция открывает и  считывает файл, который является словарем игры; Записывает слова, разделяя их в список
    по одному слову; этот список является словарем игры; Возвращает словарь игры в виде списка.
    :return: Возвращает список слов
    '''
    opened_file = open('Words.txt')
    word_list = opened_file.read().splitlines()
    word_list = [i.lower() for i in word_list]
    return word_list