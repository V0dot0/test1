import csv
import re


# print(type())

def csv_to_txt_service():
    '''
    Для упрощения обращения к файлу, создает новый текствовый файл и помещает в него текст из cvs файла
    '''

    with open('books.csv', 'r', ) as file:
        fixed_text: str = ""
        reader: csv.reader = csv.reader(file, delimiter='\t')
        books_converted_write: io.TextIOWrapper = open("books_converted.txt", mode='w', encoding='utf-8')
        for row in reader:
            fixed_text: str = ''.join(row) + "\n"
            books_converted_write.write(str(fixed_text))


def remove_unnecessary_text():
    '''
    Обращается к измененному csv_to_txt_service() файлу books_converted.txt и оставляет только важные данные
    :return: список данных
    '''
    pattern: str = r"(?P<isbn>\d+-\d+-\d+-\d+-\d+)[|](?P<title>[^|]+)[|](?P<author>[^|]+)[|](?P<quantity>\d+)[|]" \
                   r"(?P<price>\d+.*)"
    books_converted_open: io.TextIOWrapper = open("books_converted.txt", mode='r', encoding='utf-8')
    content: str = books_converted_open.read()
    list_of_books: list = re.findall(pattern, content)
    return (list_of_books)


def get_books(word: str):
    '''
    Ищет совпадения по слову с маленькой буквы, из текста с маленькой буквы
    :param word: слово, которое будем искать
    :return: список совпадений
    '''
    word_lower: str = word.lower()
    list_of_books = remove_unnecessary_text()
    with_matches: list = []
    for element in list_of_books:
        for book_element in element:
            book_element_str = ''.join(book_element)
            book_element_str_lower = book_element_str.lower()
            if word_lower in book_element_str_lower:
                with_matches.append(element)
    return (with_matches)


def get_totals(list_of_books):
    '''
    Принимает список слов из get_books() и приводит к виду [(isbn, quantity * price)];
    возвращаем отформатированный список
    :param list_of_books: Список списков из get_books()
    :return: отформатированный список
    '''
    books_elements: list = list_of_books
    books_totals: list = []
    for book_elements in books_elements:
        quantity_multiply_price: float = int(book_elements[3]) * float(book_elements[4])
        if quantity_multiply_price < 500:
            quantity_multiply_price += 100
        books_totals.append((book_elements[0], quantity_multiply_price))
    return books_totals
