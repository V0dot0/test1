import re


def read_log(requested_file):
    '''
    Функция принимает название файла; открывает и считывает этот файл; возвращает данные файла в виде текста
    :param requested_file: название файла (из которого мы возьмем данные)
    :return: данные из файла (в виде текста)
    '''
    content: TextIOWrapper = open(requested_file, encoding='utf-8')
    returned_file: str = content.read()
    return returned_file


def formatting_and_save_log(requested_file, returned_file):
    '''
    Функция принимает название файла; применяет на него функцию read_log(); форматирует его в нужный нам вид;
    записывает данные в заданный файл; возвращает сообщение об окончании работы.
    :param requested_file: название файла (из которого мы возьмем данные)
    :param returned_file: название файла (в который мы запишем данные)
    :return: возвращает сообщение об окончании работы
    '''
    content: str = read_log(requested_file)
    content: list = content.splitlines()
    pattern = r"(?:^Рейс) (\d+) (?:прибыл|отправился) (\w+) (\w+) (?:\w+) (\d+:\d+:\d+)"
    changed_log: TextIOWrapper = open(returned_file, mode='w+', encoding='utf-8')
    changed_log.write(str("# File content "))
    changed_log.write(str(changed_log.name))
    changed_log.write(str("\n\nTotal train log: \n"))
    for element in content:
        content: re.Pattern = re.findall(pattern, element)
        if len(content) == 1:
            res: list = content[0]
            initial_log: list = ['[', res[3], '] - Поезд № ', res[0], ' ',
                                 res[1], ' ', res[2]]
            final_log: str = ''.join(initial_log)
            changed_log.write(str(final_log))
            changed_log.write(str("\n"))
        else:
            continue
    return "===Данные отформатированы и сохранены в указанный файл==="
