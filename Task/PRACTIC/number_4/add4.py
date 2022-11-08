def read_file():
    opened_file = open('data.txt')
    word_list = list(set(opened_file.read().splitlines()))
    return word_list

def save_file(txt, wrd):
    words = read_file()
    words.sort()
    print(words)
    count = len(wrd)

    return count, words

