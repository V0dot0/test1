import os
#import pdf2docx
import pathlib
import time
import re

from pdf2docx import parse as pdf2docxParse
from docx2pdf import convert as docx2pdfConvert
from PIL import Image


# univercity starting location os.chdir(r"C:\Users\Student\Desktop\python\testingGround")
#  my pc starting location
os.chdir(r"C:\tmp\four2")
def zero_change_catalogue():
    inpud = input("Укажите корректный путь к каталогу: ")
    if os.path.exists(inpud) == 1:
        print("Перехожу к каталогу")
        os.chdir(inpud)
        main_cycle()
    else:
        print("Такого каталога не существует")
        zero_change_catalogue()

def one_pdf_doc():
    this_directory = os.getcwd()
    print("Список файлов с расширением pdf в текущем каталоге",this_directory)
    get_all_items = os.listdir(os.getcwd())
    list_for_pdf = []
    list_for_path = []
    i = 0
    for word in get_all_items:
        if pathlib.Path(word).suffix == ".pdf":
            i +=1
            list_for_pdf.append(word)
            list_for_path.append(os.path.abspath(word))
            print(i,". ",word)
    return [list_for_pdf,list_for_path]
def one_two_pdf_doc(list):
    list_for_pdf, list_for_path = list
    inpud = int(input("0 для преобразования всех файлов. Ваш выбор: "))
    if inpud == 0:
        i = 1
        for word in list_for_pdf:
            selected_path = list_for_path[i - 1]
            selected_pdf = list_for_pdf[i - 1]
            future_doc = selected_pdf + ".doc"
            future_doc = future_doc.replace('.pdf', '')
            pdf2docxParse(selected_path, future_doc)
            time.sleep(1)
            i += 1
        print("Все файлы переведены")
        main_cycle()
    else:
        selected_path = list_for_path[inpud-1]
        selected_pdf = list_for_pdf[inpud-1]
        future_doc = selected_pdf+".doc"
        future_doc = future_doc.replace('.pdf', '')
        pdf2docxParse(selected_path, future_doc)
        time.sleep(1)
        main_cycle()
def two_doc2pdf():
    this_directory = os.getcwd()
    print("Список файлов с расширением doc в текущем каталоге",this_directory)
    get_all_items = os.listdir(os.getcwd())
    list_for_doc = []
    list_for_path = []
    i = 0
    for word in get_all_items:
        if pathlib.Path(word).suffix == ".doc" or pathlib.Path(word).suffix == ".docx":
            i +=1
            list_for_doc.append(word)
            list_for_path.append(os.path.abspath(word))
            print(i,". ",word)
    return [list_for_doc,list_for_path]
def two_two_doc2pdf(list):
    list_for_doc, list_for_path = list
    inpud = int(input("0 для преобразования всех файлов. Ваш выбор: "))
    if inpud == 0:
        i = 1
        for word in list_for_doc:
            selected_path = list_for_path[i - 1]
            selected_pdf = list_for_doc[i - 1]
            future_doc = selected_pdf + ".pdf"
            future_doc = future_doc.replace('.docx', '').replace('.doc', '')
            docx2pdfConvert(selected_path, future_doc)
            time.sleep(1)
            i += 1
        print("Все файлы переведены")
        main_cycle()
    else:
        selected_path = list_for_path[inpud-1]
        selected_pdf = list_for_doc[inpud-1]
        future_doc = selected_pdf+".pdf"
        future_doc = future_doc.replace('.docx', '').replace('.doc', '')
        docx2pdfConvert(selected_path, future_doc)
        time.sleep(1)
        main_cycle()

def three_image():
    this_directory = os.getcwd()
    print("Список файлов с расширением jpg, png, gif, jpeg в текущем каталоге",this_directory)
    get_all_items = os.listdir(os.getcwd())
    list_for_imgs = []
    list_for_path = []
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
    list_for_img, list_for_path = list
    inpud = int(input("0 для преобразования всех файлов. Ваш выбор: "))
    if inpud == 0:
        i = 1
        qualityMy = int(input("ВВедите качество сжатия (0-100) : "))
        for word in list_for_img:
            selected_path = list_for_path[i - 1]
            selected_img = list_for_img[i - 1]
            image_open = Image.open(selected_path)
            future_img = "(quality "+str(qualityMy)+")"+selected_img
            image_open.save(future_img, quality=qualityMy)
            time.sleep(1)
            i += 1
        print("Все файлы переведены")
        main_cycle()
    else:
        qualityMy = int(input("ВВедите качество сжатия (0-100) : "))
        selected_path = list_for_path[inpud-1]
        selected_img = list_for_img[inpud-1]
        image_open = Image.open(selected_path)
        future_img = "(quality "+str(qualityMy)+")"+selected_img
        image_open.save(future_img, quality=qualityMy)
        time.sleep(1)
        main_cycle()

def four_deleter():
    test = open("output.pdf", mode='w', encoding='utf-8');test = open("doc.doc", mode='w', encoding='utf-8')
    test = open("test.txt", mode='w', encoding='utf-8');test = open("tempy.cvs", mode='w', encoding='utf-8')
    test = open("help.txt", mode='w', encoding='utf-8');test = open("temp2y.txt", mode='w', encoding='utf-8')
    test.close()
    get_all_items = os.listdir(os.getcwd())
    print("Текущие файлы из ",os.getcwd()," : ",get_all_items)

    print("1. Удалить все файлы начинающиеся на определенную подстроку\n\
2. Удалить все файлы заканчивающиеся на определенную подстроку\n\
3. Удалить все файлы содержащие определенную подстроку\n\
4. Удалить все файлы по расширению")

    inpud = int(input("Выберите номер действия. Ваш выбор: "))
    if inpud == 1:
        directory = os.getcwd()
        files_in_directory = os.listdir(directory)
        patternOrigin = input("Выберите подстроку начала: ")
        pattern = "^" + patternOrigin
        filtered_files = [file for file in files_in_directory if (re.search(pattern, file))]
        for file in filtered_files:
            if file.startswith(patternOrigin):
                path_to_file = os.path.join(directory, file)
                print("Удалено: ",path_to_file)
                os.remove(path_to_file)
        get_all_items = os.listdir(os.getcwd())
        print("Текущие файлы из ",os.getcwd()," : ",get_all_items)

    elif inpud == 2:
        directory = os.getcwd()
        files_in_directory = os.listdir(directory)
        patternOrigin = input("Выберите подстроку окончания: ")
        pattern = patternOrigin + ".\w+$"
        filtered_files = [file for file in files_in_directory if (re.search(pattern, file))]
        for file in filtered_files:
            a = pathlib.Path(file).suffix
            fileFix = file.replace(a,"")
            if fileFix.endswith(patternOrigin):
                path_to_file = os.path.join(directory, file)
                print("Удалено: ",path_to_file)
                os.remove(path_to_file)
        get_all_items = os.listdir(os.getcwd())
        print("Текущие файлы из ",os.getcwd()," : ",get_all_items)

    elif inpud == 3:
        directory = os.getcwd()
        files_in_directory = os.listdir(directory)
        pattern = input("Выберите подстроку по всем: ")
        filtered_files = [file for file in files_in_directory if (re.search(pattern, file))]
        for file in filtered_files:
            path_to_file = os.path.join(directory, file)
            print("Удалено: ",path_to_file)
            os.remove(path_to_file)
        get_all_items = os.listdir(os.getcwd())
        print("Текущие файлы из ",os.getcwd()," : ",get_all_items)
    elif inpud == 4:
        directory = os.getcwd()
        files_in_directory = os.listdir(directory)
        pattern = input("Выберите подстроку расширения(без точки): ")
        pattern = pattern + "$"
        filtered_files = [file for file in files_in_directory if (re.search(pattern, file))]
        for file in filtered_files:
            path_to_file = os.path.join(directory, file)
            print("Удалено: ",path_to_file)
            os.remove(path_to_file)
        get_all_items = os.listdir(os.getcwd())
        print("Текущие файлы из ",os.getcwd()," : ",get_all_items)
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

    #inpud = int(input("Ваш выбор: "))
    inpud = 4

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
main_cycle()
