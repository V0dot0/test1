def read_file(requested_file):
    '''
    Функция принимает название файла; открывает и считывает этот файл; форматирует данные файла в список и возваращает
    его
    :param requested_file: название файла (из которого мы возьмем данные)
    :return: Список слов (находящихся в файле)
    '''
    content = open(requested_file, "r+")
    returned_file = list(set(content.read().splitlines()))
    return returned_file

def save_file(returned_file, requested_file):
    '''
    Функция принимае название файла из которого мы возьмем данные и название файла в который запишем данные; сортирует
    полученный список; форматирует и записывает данные в файл, который и возвращает нам.
    :param returned_file: Название файла (в который мы запишем данные)
    :param requested_file: Название файла (из которого мы возьмем данные)
    :return: файл (с записанным в него результатом)
    '''
    content = read_file(requested_file)
    content.sort()
    count = len(content)
    words = content
    words = ' '.join(words)
    words = words.replace(" ", "\n")
    returned_file = open(returned_file, mode='w+')
    returned_file.write(str("# File content "))
    returned_file.write(str(returned_file.name))

    returned_file.write(str("\nTotal unique words: "))
    returned_file.write(str(count))
    returned_file.write(str("\n===========\n"))
    returned_file.write(str(words))
    return returned_file