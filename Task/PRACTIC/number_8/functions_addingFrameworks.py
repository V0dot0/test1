import pymorphy2
from translate import Translator


translator = Translator(from_lang="ru", to_lang="en")
morph = pymorphy2.MorphAnalyzer()

def unsorted_list_creation():
    '''
    Убирает из списка все не нужное, и в итоге приводит все к словарю вида {'название': число, 'название': число,...}
    без сортировки.
    :return: словарь
    '''
    lstx = []
    txt_open: io.TextIOWrapper = open("input.txt", mode='r', encoding='utf-8')
    bad_chars = [';','!', "*","?","1","2","3","4","5","6","7","8","9","0",",",":",".","-"]
    for word in txt_open:
        word = word.replace("\n", "")
        for i in bad_chars:
            word = word.replace(i, '')
        temp_word = word.split(' ')
        lstx.append(temp_word)
    ####

    lstx2 = []
    for i in lstx:
        for words in i:
            if len(words)!=0:
                lstx2.append(words.lower())

    lst2 = {}
    for i in lstx2:
        if i in lst2:
            lst2[i] += 1
        else:
            lst2[i] = 1
    return lst2


def sorting_list(requested_list):
    '''
    Сортирует список, нормализирует его, и переводит, потом заносит в output.txt
    :param requested_list: словарь из unsorted_list_creation()
    '''

    print("Начался перевод, по завершении программы будет изменен output.txt ")
    lst2 = requested_list
    lstD = dict(sorted(lst2.items()))
    lst3 = sorted(lstD, key=lstD.get, reverse=True)

    txt_write = open("output.txt", mode='w+', encoding='utf-8')
    for sord in lst3:
        for key, value in lstD.items():
            if sord == key:
                 morph1 = morph.parse(sord)[0]
                 sord = morph1.normal_form
                 sord_translated = translator.translate(sord)
                 txt_write.write(str(sord))
                 txt_write.write("|")
                 txt_write.write(str(sord_translated))
                 txt_write.write("|")
                 txt_write.write(str(value))
                 txt_write.write('\n')

