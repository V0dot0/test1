def books_cvs_extract():
    '''
    Открывает файл books.cvs и конвертирует его в читаемый для программы текст
    :return: текст без isbn|title|author|quantity|price
    '''
    contents = open("books.cvs")
    returned_file = contents.read()
    returned_file = returned_file.replace("isbn|title|author|quantity|price", "").replace("\n", "", 1)
    return str(returned_file)


def convert_list():
    '''
    Преобразует текст в список, с маленькими буквами для удобства поиска в будущем
    :return: список
    '''
    txtfromfile = books_cvs_extract()
    txt = txtfromfile.lower()
    txt = txt.splitlines()
    txt_out = txt
    c = 0
    for word in txt:
        txt_out[c] = txt[c]
        c += 1
    return txt_out


def get_name(name):
    list = convert_list()
    new_li = []; c = 0
    for word in list:
        split_list = list[c].split("|")
        only_name = split_list[1]
        name = name.lower()
        if name in only_name.split():
            new_li.append(list[c])
        c += 1
    return new_li


def get_list(new_list):
    c = 0; newer_li = []
    for words in new_list:
        split_list = new_list[c].split("|")
        id = split_list[0]; amount = split_list[3]; cost = split_list[4]
        tempm = float(amount) * float(cost)
        split_list = id, tempm
        newer_li.append(split_list)
        c += 1
    return newer_li


def get_totals(newer_list):
    c = 0; newest_li = []
    for words in newer_list:
        current_part = newer_list[c]
        current_id = current_part[0]; temp1 = current_part[1]
        if temp1 < 200:
            temp1 += 100
        c += 1
        current_part = current_id, temp1
        newest_li.append(current_part)
    return newest_li

def printlist(list_name: list):
    '''
    :param list_name: список
    :return: выводит в консоль
    '''
    list_name = str(list_name).title()
    print(list_name)