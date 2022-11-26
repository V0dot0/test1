def readable(requested_file):
    '''
    Считывает и удаляет лишний текст, оставляя только первую строку
    :param requested_file: название файлп
    :return: отформатировынный список
    '''
    content = open(requested_file, encoding='utf-8')
    returned_file = content.read()
    returned_file = returned_file.splitlines()
    del returned_file[1::3]
    del returned_file[1::2]
    return returned_file

def transfer_save(requested_file, save_location):
    '''
    Берет отформатированный список, проходится по нему и отбирает важные данные, занося их постепенно в новый текстовый
    файл, который выбран пользователем.
    :param requested_file: отформатированный список с данными (из первой функции)
    :param save_location: название файла, в которого сохранится текст
    :return: текстовое уведомление о сохранении
    '''
    c = 0
    temp = []
    txtfile = open(save_location, mode='w+', encoding='utf-8')
    for word in requested_file:
        temp = requested_file[c].split()
        vagon = temp[1]
        city = temp[4]
        date = temp[6]
        text = "["+date+"]","- Поезд №",vagon,"из",city
        text = str(text).replace("'","").replace(",","").replace("(","").replace(")","")
        txtfile.write(text)
        txtfile.write("\n")
        #print(f"[{date}] - Поезд # {vagon} из {city}")


        c += 1
    return "Сохранено в файл", save_location