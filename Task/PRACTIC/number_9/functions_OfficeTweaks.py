import os
import pathlib  # используется для нахождения расширения файлов
import time  # используется для ожидания во время конвертировании файла
import re

from pdf2docx import parse as pdf2docxParse
from docx2pdf import convert as docx2pdfConvert
from PIL import Image


#univercity быстрый доступ
#os.chdir(r"C:\Users\Student\Desktop\python\testingGround")
#Для домашнего пк, быстрый доступ к тестам
#os.chdir(r"C:\tmp\four2")
#os.chdir(r"C:\tmp")

# print(type())
def zero_change_catalogue():
    '''
    Проверяет существует ли каталог, затем возвращается к главному циклу
    '''
    inpud: str = input("Укажите корректный путь к каталогу: ")
    if os.path.exists(inpud) == 1:
        print("Перехожу к каталогу")
        os.chdir(inpud)
        main_cycle()
    else:
        print("Такого каталога не существует")
        zero_change_catalogue()
def one_pdf_doc():
    '''
    1 часть пдф в док, сначала выводит все файлы с расширением pdf, возвращает два списка: один со списками
    всех пдф файлов, другой с полными путями к ним.
    :return: 2 списка
    '''
    this_directory: str = os.getcwd()
    print("Список файлов с расширением pdf в текущем каталоге",this_directory)
    get_all_items: list = os.listdir(os.getcwd())
    list_for_pdf: list = []
    list_for_path: list = []
    i = 0
    for word in get_all_items:
        if pathlib.Path(word).suffix == ".pdf":
            i +=1
            list_for_pdf.append(word)
            list_for_path.append(os.path.abspath(word))
            print(i,". ",word)
    return [list_for_pdf,list_for_path]
def one_two_pdf_doc(list: list):
    '''
    2 часть пдф в док. Принимает два списка из 1 части. Дает выбор пользователю, и вследствии или преобразует один
    файл, или все сразу.
    :param list: список из 1 части
    '''
    list_for_pdf, list_for_path = list
    inpud = int(input("0 для преобразования всех файлов. Ваш выбор: "))
    if inpud == 0:
        i = 1
        for word in list_for_pdf:
            selected_path: str  = list_for_path[i - 1]
            selected_pdf: str  = list_for_pdf[i - 1]
            future_doc: str  = selected_pdf + ".doc"
            future_doc: str  = future_doc.replace('.pdf', '')
            pdf2docxParse(selected_path, future_doc)
            time.sleep(1)
            i += 1
        print("Все файлы переведены")
        main_cycle()
    else:
        selected_path: str = list_for_path[inpud-1]
        selected_pdf: str  = list_for_pdf[inpud-1]
        future_doc: str  = selected_pdf+".doc"
        future_doc: str  = future_doc.replace('.pdf', '')
        pdf2docxParse(selected_path, future_doc)
        time.sleep(1)
        main_cycle()
def two_doc2pdf():
    '''
    1 часть док в пдф, сначала выводит все файлы с расширением doc/docx, возвращает два списка: один со списками
    всех doc/docx файлов, другой с полными путями к ним.
    :return: 2 списка
    '''
    this_directory: str = os.getcwd()
    print("Список файлов с расширением doc в текущем каталоге",this_directory)
    get_all_items: list = os.listdir(os.getcwd())
    list_for_doc: list = []
    list_for_path: list = []
    i = 0
    for word in get_all_items:
        if pathlib.Path(word).suffix == ".doc" or pathlib.Path(word).suffix == ".docx":
            i +=1
            list_for_doc.append(word)
            list_for_path.append(os.path.abspath(word))
            print(i,". ",word)
    return [list_for_doc,list_for_path]
def two_two_doc2pdf(list):
    '''
    2 часть док в пдф. Принимает два списка из 1 части. Дает выбор пользователю, и вследствии или преобразует один
    файл, или все сразу.
    :param list: список из 1 части
    '''
    list_for_doc, list_for_path = list
    inpud = int(input("0 для преобразования всех файлов. Ваш выбор: "))
    if inpud == 0:
        i = 1
        for word in list_for_doc:
            selected_path: str  = list_for_path[i - 1]
            selected_pdf: str  = list_for_doc[i - 1]
            future_doc: str  = selected_pdf + ".pdf"
            future_doc: str  = future_doc.replace('.docx', '').replace('.doc', '')
            docx2pdfConvert(selected_path, future_doc)
            time.sleep(1)
            i += 1
        print("Все файлы переведены")
        main_cycle()
    else:
        selected_path: str  = list_for_path[inpud-1]
        selected_pdf: str  = list_for_doc[inpud-1]
        future_doc: str  = selected_pdf+".pdf"
        future_doc: str  = future_doc.replace('.docx', '').replace('.doc', '')
        docx2pdfConvert(selected_path, future_doc)
        time.sleep(1)
        main_cycle()
def three_image():
    '''
    1 часть сжатия картинки, сначала выводит все файлы с расширением jpg/gif/png/jpeg, возвращает два списка: один со списками
    всех картинок, другой с полными путями к ним.
    :return: 2 списка
    '''
    this_directory: str = os.getcwd()
    print("Список файлов с расширением jpg, png, gif, jpeg в текущем каталоге",this_directory)
    get_all_items: list = os.listdir(os.getcwd())
    list_for_imgs: list = []
    list_for_path: list = []
    i = 0
    for word in get_all_items:
        if pathlib.Path(word).suffix == ".jpg" or pathlib.Path(word).suffix == ".png"or \
                pathlib.Path(word).suffix == ".gif"or pathlib.Path(word).suffix == ".jpeg":
            i +=1
            list_for_imgs.append(word)
            list_for_path.append(os.path.abspath(word))
            print(i,". ",word)
    return [list_for_imgs,list_for_path]
def three_image_two(list):
    '''
    2 часть сжатия картинок. Принимает два списка из 1 части. Дает выбор пользователю, и вследствии или преобразует один
    файл, или все сразу.
    :param list: 2 списка из 1 части
    '''
    list_for_img, list_for_path = list
    inpud = int(input("0 для преобразования всех файлов. Ваш выбор: "))
    if inpud == 0:
        i = 1
        qualityMy = int(input("ВВедите качество сжатия (0-100) : "))
        for word in list_for_img:
            selected_path: str  = list_for_path[i - 1]
            selected_img: str  = list_for_img[i - 1]
            image_open: PIL.JpegImagePlugin.JpegImageFile= Image.open(selected_path)
            future_name: str = "(quality "+str(qualityMy)+")"+selected_img
            image_open.save(future_name, quality=qualityMy)
            time.sleep(1)
            i += 1
        print("\nВсе файлы сжаты\n")
        main_cycle()
    else:
        qualityMy = int(input("ВВедите качество сжатия (0-100) : "))
        selected_path: str = list_for_path[inpud-1]
        selected_img: str = list_for_img[inpud-1]
        image_open: PIL.JpegImagePlugin.JpegImageFile = Image.open(selected_path)
        future_name: str = "(quality "+str(qualityMy)+")"+selected_img
        image_open.save(future_name, quality=qualityMy)
        time.sleep(1)
        main_cycle()

def four_deleter():
    '''
    Выводит все файлы из текущей папки, предлагает выбор, в зависимости от выбора ищет по патерну, затем выводит что
    удалил и что осталось после.
    :return:
    '''
    ### ДЛЯ ТЕСТОВ, создает пустые файлы
    #test = open("output.pdf", mode='w', encoding='utf-8');test = open("doc.doc", mode='w', encoding='utf-8')
    #test = open("test.txt", mode='w', encoding='utf-8');test = open("tempy.cvs", mode='w', encoding='utf-8')
    #test = open("help.txt", mode='w', encoding='utf-8');test = open("temp2y.txt", mode='w', encoding='utf-8')
    #test.close()
    get_all_items: list = os.listdir(os.getcwd())
    print("Текущие файлы из ",os.getcwd()," : ",get_all_items)

    print("1. Удалить все файлы начинающиеся на определенную подстроку\n\
2. Удалить все файлы заканчивающиеся на определенную подстроку\n\
3. Удалить все файлы содержащие определенную подстроку\n\
4. Удалить все файлы по расширению")

    inpud = int(input("Выберите номер действия. Ваш выбор: "))
    if inpud == 1:
        directory: str = os.getcwd()
        files_in_directory: list = os.listdir(directory)
        patternOrigin: str = input("Выберите подстроку начала: ")
        pattern: str = "^" + patternOrigin
        filtered_files: list = [file for file in files_in_directory if (re.search(pattern, file))]
        for file in filtered_files:
            if file.startswith(patternOrigin):
                path_to_file = os.path.join(directory, file)
                print("Удалено: ",path_to_file)
                os.remove(path_to_file)
        get_all_items: list = os.listdir(os.getcwd())
        print("Текущие файлы из ",os.getcwd()," : ",get_all_items)
        main_cycle()

    elif inpud == 2:
        directory: str = os.getcwd()
        files_in_directory: list = os.listdir(directory)
        patternOrigin: str = input("Выберите подстроку окончания: ")
        pattern: str = patternOrigin + ".\w+$"
        filtered_files: list = [file for file in files_in_directory if (re.search(pattern, file))]
        for file in filtered_files:
            suffix: str = pathlib.Path(file).suffix
            fileFix: str = file.replace(suffix,"")
            if fileFix.endswith(patternOrigin):
                path_to_file = os.path.join(directory, file)
                print("Удалено: ",path_to_file)
                os.remove(path_to_file)
        get_all_items: list = os.listdir(os.getcwd())
        print("Текущие файлы из ",os.getcwd()," : ",get_all_items)
        main_cycle()

    elif inpud == 3:
        directory: str = os.getcwd()
        files_in_directory: list = os.listdir(directory)
        pattern: str = input("Выберите подстроку по всем: ")
        filtered_files: list = [file for file in files_in_directory if (re.search(pattern, file))]
        for file in filtered_files:
            path_to_file = os.path.join(directory, file)
            print("Удалено: ",path_to_file)
            os.remove(path_to_file)
        get_all_items: list = os.listdir(os.getcwd())
        print("Текущие файлы из ",os.getcwd()," : ",get_all_items)
        main_cycle()

    elif inpud == 4:
        directory: str  = os.getcwd()
        files_in_directory: list = os.listdir(directory)
        pattern: str = input("Выберите подстроку расширения(без точки): ")
        pattern: str = pattern + "$"
        filtered_files: list = [file for file in files_in_directory if (re.search(pattern, file))]
        for file in filtered_files:
            path_to_file = os.path.join(directory, file)
            print("Удалено: ",path_to_file)
            os.remove(path_to_file)
        get_all_items: list = os.listdir(os.getcwd())
        print("Текущие файлы из ",os.getcwd()," : ",get_all_items)
        main_cycle()
    else:
        print("ВВЕДИТЕ ОТ 1 ДО 4")
        four_deleter()
def main_cycle():
    print("Текущий каталог",os.getcwd(),"\n")
    print("Выберите действие \n")
    print("0. Сменить рабочий каталог")
    print("1. PDF в DOC")
    print("2. DOC/DOCX в PDF")
    print("3. Сжатие изображения")
    print("4. Удалить группу файлов")
    print("5. Выход\n")

    inpud = int(input("Ваш выбор: "))
    #для быстрого теста
    #inpud = 4
    if inpud == 0:
        zero_change_catalogue()
    if inpud == 1:
        one_two_pdf_doc(one_pdf_doc())
    if inpud == 2:
        two_two_doc2pdf(two_doc2pdf())
    if inpud == 3:
        three_image_two(three_image())
    if inpud == 4:
        four_deleter()
    if inpud == 5:
        return

main_cycle()
