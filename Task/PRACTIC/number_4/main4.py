from Task.PRACTIC.number_4 import add4 as ad


#ad.get_word_list()
sv = ad.save_file('data.txt', ad.get_word_list())
count = sv[0]
words = sv[1]
words = ' '.join(words)
words = words.replace(" ", "\n")
#print(count, words)


text_to_write = count, words
# представим что это тот же файл, что бы не перезаписывать старый
new_text = open("dataAf.txt", mode='w+')
new_text.write(str("# File content 'data.txt'\n"))
new_text.write(str("Total unique words: "))
new_text.write(str(count))
new_text.write(str("\n=========================\n"))
new_text.write(str(words))