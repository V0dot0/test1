import csv
import re


def csv_to_txt_service():
    with open('books.csv', 'r', ) as file:
        fixed_text = ""
        reader = csv.reader(file, delimiter='\t')
        books_converted_write = open("books_converted.txt", mode='w', encoding='utf-8')
        for row in reader:
            fixed_text = ''.join(row) + "\n"
            books_converted_write.write(str(fixed_text))


def remove_unnecessary_text():
    pattern8 = r"(?P<isbn>\d+-\d+-\d+-\d+-\d+)[|](?P<title>[^|]+)[|](?P<author>[^|]+)[|](?P<quantity>\d+)[|]" \
               r"(?P<price>\d+.*)"
    books_converted_open = open("books_converted.txt", mode='r', encoding='utf-8')
    content = books_converted_open.read()
    list_of_books = re.findall(pattern8, content)
    return (list_of_books)

def get_books(word):
    word_lower = word.lower()
    list_of_books = remove_unnecessary_text()
    with_matches = []
    for element in list_of_books:
        for book_element in element:
            book_element_str= ''.join(book_element)
            book_element_str_lower: str = book_element_str.lower()
            if word_lower in book_element_str_lower:
                with_matches.append(element)
    return (with_matches)

def get_totals(list_of_books):
    books_elements= list_of_books
    books_totals= []
    for book_elements in books_elements:
        quantity_multiply_price: float = int(book_elements[3]) * float(book_elements[4])
        if quantity_multiply_price < 500:
            quantity_multiply_price += 100
        books_totals.append((book_elements[0], quantity_multiply_price))
    return books_totals


