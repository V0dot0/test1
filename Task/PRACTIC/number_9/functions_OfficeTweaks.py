import os
import pdf2docx
import pathlib


os.chdir(r"C:\Users\Student\Desktop\python\testingGround")

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
    print("Список файлов с расширением pdf в текущем каталоге",os.getcwd())
    get_all_items = os.listdir(os.getcwd())
    list_for_pdf = []
    i = 0
    for word in get_all_items:
        if pathlib.Path(word).suffix == ".pdf":
            i +=1
            list_for_pdf.append(word)
            print(i,". ",word)
    inpud = int(input("0 для выхода. Ваш выбор: "))
    print(list_for_pdf[inpud-1])
    #print(pathlib.Path('yourPath.example').suffix)

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

    if inpud == 0:
        zero_change_catalogue()
    if inpud == 1:
        one_pdf_doc()







main_cycle()
