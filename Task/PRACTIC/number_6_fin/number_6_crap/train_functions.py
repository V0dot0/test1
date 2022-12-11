def readable(requested_file: str):
    '''
    Считывает и удаляет лишний текст, оставляя только первую строку
    :param requested_file: название файлп
    :return: отформатировынный список
    '''
    content: TextIOWrapper = open(requested_file, encoding='utf-8')
    returned_file: str = content.read()
    #print(type(returned_file))
    returned_file: list = returned_file.splitlines()
    del returned_file[1::3]
    del returned_file[1::2]
    return returned_file


def transfer_save(requested_file: str, save_location: str):
    '''
    Берет отформатированный список, проходится по нему и отбирает важные данные, занося их постепенно в новый текстовый
    файл, который выбран пользователем.
    :param requested_file: отформатированный список с данными (из первой функции)
    :param save_location: название файла, в которого сохранится текст
    :return: текстовое уведомление о сохранении
    '''
    counter = 0
    temp = []
    txtfile: TextIOWrapper = open(save_location, mode='w+', encoding='utf-8')
    for word in requested_file:
        temp: list = requested_file[counter].split()
        vagon: str = temp[1]
        city: str = temp[4]
        date: str = temp[6]
        text: str = "[" + date + "]", "- Поезд №", vagon, "из", city
        text: str = str(text).replace("'", "").replace(",", "").replace("(", "").replace(")", "")
        txtfile.write(text)
        txtfile.write("\n")
        # print(f"[{date}] - Поезд # {vagon} из {city}")

        counter += 1
    return "Сохранено в файл", save_location
