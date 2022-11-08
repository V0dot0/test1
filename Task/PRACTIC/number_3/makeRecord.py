def record(currentRecord):
    new_text = open("Record.txt", mode='r+')
    found = int(new_text.read())
    if currentRecord > found:
        found = currentRecord

    new_text.seek(0)
    new_text.write(str(found))
    return("текущий рекорд ",currentRecord, "максимальный рекорд ", found)

def get_words():
    opened_file = open('Words.txt')
    word_list = opened_file.read().splitlines()
    word_list = [i.lower() for i in word_list]
    return word_list