import re
import pymorphy2
from translate import Translator


translator = Translator(from_lang="ru", to_lang="en")
morph = pymorphy2.MorphAnalyzer()

def unsorted_list_creation():
    '''
    Открывает файл input.txt, оставляет слова, приводит все к словарю вида {'название': число, 'название': число,...}
    без сортировки.
    :return: словарь
    '''
    txt_open: TextIOWrapper = open('input.txt', mode='r+', encoding='utf-8')
    content: str = txt_open.read()
    content: str = content.lower()
    good_chars_pattern: str = r"(?:\я|\w+[^(\W|\d)]+)"
    good_words: list = re.findall(good_chars_pattern, content)

    slovar_unsorted: dict = {}
    for word in good_words:
        if word in slovar_unsorted:
            slovar_unsorted[word] += 1
        else:
            slovar_unsorted[word] = 1
    return slovar_unsorted


def sorting_list(requested_list):
    '''
    Сортирует список, нормализирует его, и переводит, потом заносит в output.txt
    :param requested_list: словарь из unsorted_list_creation()
    '''

    print("Начался перевод, по завершении программы будет изменен output.txt ")
    slovar_unsorted = requested_list
    alphabet_sorted: dict = dict(sorted(slovar_unsorted.items()))
    sorted_by_most: list = sorted(alphabet_sorted, key=alphabet_sorted.get, reverse=True)

    txt_write: TextIOWrapper = open("output.txt", mode='w+', encoding='utf-8')
    for sord in sorted_by_most:
        for key, value in alphabet_sorted.items():
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
    print("\nВыполено!!!!!!!!!!!!")
